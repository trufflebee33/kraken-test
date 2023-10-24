//! This module holds the aggregated data of services

use std::collections::HashMap;

use actix_toolbox::tb_middleware::Session;
use actix_web::get;
use actix_web::web::{Data, Json, Path, Query};
use futures::TryStreamExt;
use rorm::conditions::{BoxedCondition, Condition, DynamicCollection};
use rorm::{and, query, Database, FieldAccess, Model};
use serde::{Deserialize, Serialize};
use utoipa::{IntoParams, ToSchema};
use uuid::Uuid;

use crate::api::handler::hosts::SimpleHost;
use crate::api::handler::{
    get_page_params, ApiError, ApiResult, PageParams, PathUuid, ServiceResultsPage, SimpleTag,
    TagType,
};
use crate::models::{
    Certainty, GlobalTag, Host, Service, ServiceGlobalTag, ServiceWorkspaceTag, Workspace,
    WorkspaceTag,
};
use crate::query_tags;

/// Query parameters for filtering the services to get
#[derive(Deserialize, IntoParams)]
pub struct GetAllServicesQuery {
    /// Only get services associated with a specific host
    pub host: Option<Uuid>,
}

/// A simple representation of a service
#[derive(Serialize, ToSchema)]
pub struct SimpleService {
    uuid: Uuid,
    #[schema(example = "postgresql")]
    name: String,
    #[schema(example = "13.0.1")]
    version: Option<String>,
    host: Uuid,
    port: Option<Uuid>,
    #[schema(example = "Holds all relevant information")]
    comment: String,
    workspace: Uuid,
}

/// A full representation of a service
#[derive(Serialize, ToSchema)]
pub struct FullService {
    uuid: Uuid,
    #[schema(example = "postgresql")]
    name: String,
    #[schema(example = "13.0.1")]
    version: Option<String>,
    certainty: Certainty,
    host: SimpleHost,
    port: Option<Uuid>,
    #[schema(example = "Holds all relevant information")]
    comment: String,
    workspace: Uuid,
    tags: Vec<SimpleTag>,
}

/// List the services of a workspace
#[utoipa::path(
    tag = "Services",
    context_path = "/api/v1",
    responses(
        (status = 200, description = "Retrieve all services of a workspace", body = ServiceResultsPage),
        (status = 400, description = "Client error", body = ApiErrorResponse),
        (status = 500, description = "Server error", body = ApiErrorResponse),
    ),
    params(PathUuid, PageParams, GetAllServicesQuery),
    security(("api_key" = []))
)]
#[get("/workspaces/{uuid}/services")]
pub async fn get_all_services(
    path: Path<PathUuid>,
    page_params: Query<PageParams>,
    filter_params: Query<GetAllServicesQuery>,
    db: Data<Database>,
    session: Session,
) -> ApiResult<Json<ServiceResultsPage>> {
    let path = path.into_inner();
    let user_uuid: Uuid = session.get("uuid")?.ok_or(ApiError::SessionCorrupt)?;

    let mut tx = db.start_transaction().await?;

    if !Workspace::is_user_member_or_owner(&mut tx, path.uuid, user_uuid).await? {
        return Err(ApiError::MissingPrivileges);
    }

    let (limit, offset) = get_page_params(page_params).await?;

    fn build_condition(workspace: Uuid, filter_params: &GetAllServicesQuery) -> BoxedCondition<'_> {
        match filter_params {
            GetAllServicesQuery { host: Some(host) } => and![
                Service::F.workspace.equals(workspace),
                Service::F.host.equals(*host)
            ]
            .boxed(),
            GetAllServicesQuery { host: None } => Service::F.workspace.equals(workspace).boxed(),
        }
    }

    let (total,) = query!(&mut tx, (Service::F.uuid.count()))
        .condition(build_condition(path.uuid, &filter_params))
        .one()
        .await?;

    let services = query!(
        &mut tx,
        (
            Service::F.uuid,
            Service::F.name,
            Service::F.version,
            Service::F.certainty,
            Service::F.comment,
            Service::F.host as Host,
            Service::F.port,
            Service::F.workspace,
        )
    )
    .condition(build_condition(path.uuid, &filter_params))
    .limit(limit)
    .offset(offset)
    .all()
    .await?;

    let mut tags = HashMap::new();

    query_tags!(
        tags,
        tx,
        (
            ServiceWorkspaceTag::F.workspace_tag as WorkspaceTag,
            ServiceWorkspaceTag::F.service
        ),
        ServiceWorkspaceTag::F.service,
        (
            ServiceGlobalTag::F.global_tag as GlobalTag,
            ServiceGlobalTag::F.service
        ),
        ServiceGlobalTag::F.service,
        services.iter().map(|x| x.0)
    );

    tx.commit().await?;

    let items = services
        .into_iter()
        .map(
            |(uuid, name, version, certainty, comment, host, port, workspace)| FullService {
                uuid,
                name,
                version,
                certainty,
                comment,
                host: SimpleHost {
                    uuid: host.uuid,
                    ip_addr: host.ip_addr.to_string(),
                    os_type: host.os_type,
                    comment: host.comment,
                    workspace: *host.workspace.key(),
                },
                port: port.map(|y| *y.key()),
                workspace: *workspace.key(),
                tags: tags.remove(&uuid).unwrap_or_default(),
            },
        )
        .collect();

    Ok(Json(ServiceResultsPage {
        items,
        limit,
        offset,
        total: total as u64,
    }))
}
