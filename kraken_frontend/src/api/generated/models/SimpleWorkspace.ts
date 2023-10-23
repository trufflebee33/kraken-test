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
import type { SimpleUser } from './SimpleUser';
import {
    SimpleUserFromJSON,
    SimpleUserFromJSONTyped,
    SimpleUserToJSON,
} from './SimpleUser';

/**
 * A simple version of a workspace
 * @export
 * @interface SimpleWorkspace
 */
export interface SimpleWorkspace {
    /**
     * 
     * @type {string}
     * @memberof SimpleWorkspace
     */
    uuid: string;
    /**
     * 
     * @type {string}
     * @memberof SimpleWorkspace
     */
    name: string;
    /**
     * 
     * @type {string}
     * @memberof SimpleWorkspace
     */
    description?: string | null;
    /**
     * 
     * @type {SimpleUser}
     * @memberof SimpleWorkspace
     */
    owner: SimpleUser;
    /**
     * 
     * @type {Date}
     * @memberof SimpleWorkspace
     */
    createdAt: Date;
}

/**
 * Check if a given object implements the SimpleWorkspace interface.
 */
export function instanceOfSimpleWorkspace(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "uuid" in value;
    isInstance = isInstance && "name" in value;
    isInstance = isInstance && "owner" in value;
    isInstance = isInstance && "createdAt" in value;

    return isInstance;
}

export function SimpleWorkspaceFromJSON(json: any): SimpleWorkspace {
    return SimpleWorkspaceFromJSONTyped(json, false);
}

export function SimpleWorkspaceFromJSONTyped(json: any, ignoreDiscriminator: boolean): SimpleWorkspace {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'uuid': json['uuid'],
        'name': json['name'],
        'description': !exists(json, 'description') ? undefined : json['description'],
        'owner': SimpleUserFromJSON(json['owner']),
        'createdAt': (new Date(json['created_at'])),
    };
}

export function SimpleWorkspaceToJSON(value?: SimpleWorkspace | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'uuid': value.uuid,
        'name': value.name,
        'description': value.description,
        'owner': SimpleUserToJSON(value.owner),
        'created_at': (value.createdAt.toISOString()),
    };
}

