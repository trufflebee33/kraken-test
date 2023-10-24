import { Api } from "../../../api/api";
import React from "react";
import { FullHost, SimpleDomain, SimpleHost } from "../../../api/generated";
import WorkspaceDataTable from "./workspace-data-table";
import { handleApiError } from "../../../utils/helper";

export type WorkspaceDataHostsProps = {
    workspace: string;
    onSelect: (uuid: string) => void;
};

export function WorkspaceDataHosts(props: WorkspaceDataHostsProps) {
    const { workspace, onSelect } = props;
    return (
        <WorkspaceDataTable<FullHost>
            query={(limit, offset) => Api.workspaces.hosts.all(workspace, limit, offset)}
            queryDeps={[workspace]}
        >
            <div className={"workspace-data-table-header pane"}>
                <span>IP</span>
                <span>Comment</span>
            </div>
            {(host) => (
                <div className={"workspace-data-table-row pane"} onClick={() => onSelect(host.uuid)}>
                    <span>{host.ipAddr}</span>
                    <span>{host.comment}</span>
                </div>
            )}
        </WorkspaceDataTable>
    );
}
