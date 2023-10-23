/* tslint:disable */
/* eslint-disable */
/**
 * kraken
 * The core component of kraken-project
 *
 * The version of the OpenAPI document: 0.1.0
 * Contact: git@omikron.dev
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * The request to invite a user to the workspace
 * @export
 * @interface InviteToWorkspace
 */
export interface InviteToWorkspace {
    /**
     * The user to invite
     * @type {string}
     * @memberof InviteToWorkspace
     */
    user: string;
}

/**
 * Check if a given object implements the InviteToWorkspace interface.
 */
export function instanceOfInviteToWorkspace(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "user" in value;

    return isInstance;
}

export function InviteToWorkspaceFromJSON(json: any): InviteToWorkspace {
    return InviteToWorkspaceFromJSONTyped(json, false);
}

export function InviteToWorkspaceFromJSONTyped(json: any, ignoreDiscriminator: boolean): InviteToWorkspace {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'user': json['user'],
    };
}

export function InviteToWorkspaceToJSON(value?: InviteToWorkspace | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'user': value.user,
    };
}

