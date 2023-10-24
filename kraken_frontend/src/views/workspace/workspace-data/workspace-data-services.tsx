import { Api } from "../../../api/api";
import React from "react";
import WorkspaceDataTable from "./workspace-data-table";
import { FullService, SimpleService } from "../../../api/generated";

export type WorkspaceDataServicesProps = {
    workspace: string;
    onSelect: (uuid: string) => void;
};

export function WorkspaceDataServices(props: WorkspaceDataServicesProps) {
    const { workspace, onSelect } = props;
    return (
        <WorkspaceDataTable<FullService>
            query={(limit, offset) => Api.workspaces.services.all(workspace, limit, offset)}
            queryDeps={[workspace]}
        >
            <div className={"workspace-data-table-header pane"}>
                <span>Name</span>
                <span>Host</span>
                <span>Number</span>
                <span>Comment</span>
            </div>
            {(service) => (
                <div className={"workspace-data-table-row pane"} onClick={() => onSelect(service.uuid)}>
                    <span>{service.name}</span>
                    <span>{service.host.ipAddr}</span>
                    <span>{service.port}</span>
                    <span>{service.comment}</span>
                </div>
            )}
        </WorkspaceDataTable>
    );
}
