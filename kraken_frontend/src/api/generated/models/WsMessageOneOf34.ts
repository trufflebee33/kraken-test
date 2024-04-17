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
import type { UpdateFindingAffectedRequest } from './UpdateFindingAffectedRequest';
import {
    UpdateFindingAffectedRequestFromJSON,
    UpdateFindingAffectedRequestFromJSONTyped,
    UpdateFindingAffectedRequestToJSON,
} from './UpdateFindingAffectedRequest';

/**
 * A finding's affected has been updated
 * @export
 * @interface WsMessageOneOf34
 */
export interface WsMessageOneOf34 {
    /**
     * The workspace the updated finding is in
     * @type {string}
     * @memberof WsMessageOneOf34
     */
    workspace: string;
    /**
     * The finding which has been updated
     * @type {string}
     * @memberof WsMessageOneOf34
     */
    finding: string;
    /**
     * The affected's uuid
     * @type {string}
     * @memberof WsMessageOneOf34
     */
    affectedUuid: string;
    /**
     * 
     * @type {UpdateFindingAffectedRequest}
     * @memberof WsMessageOneOf34
     */
    update: UpdateFindingAffectedRequest;
    /**
     * 
     * @type {string}
     * @memberof WsMessageOneOf34
     */
    type: WsMessageOneOf34TypeEnum;
}


/**
 * @export
 */
export const WsMessageOneOf34TypeEnum = {
    UpdatedFindingAffected: 'UpdatedFindingAffected'
} as const;
export type WsMessageOneOf34TypeEnum = typeof WsMessageOneOf34TypeEnum[keyof typeof WsMessageOneOf34TypeEnum];


/**
 * Check if a given object implements the WsMessageOneOf34 interface.
 */
export function instanceOfWsMessageOneOf34(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "workspace" in value;
    isInstance = isInstance && "finding" in value;
    isInstance = isInstance && "affectedUuid" in value;
    isInstance = isInstance && "update" in value;
    isInstance = isInstance && "type" in value;

    return isInstance;
}

export function WsMessageOneOf34FromJSON(json: any): WsMessageOneOf34 {
    return WsMessageOneOf34FromJSONTyped(json, false);
}

export function WsMessageOneOf34FromJSONTyped(json: any, ignoreDiscriminator: boolean): WsMessageOneOf34 {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'workspace': json['workspace'],
        'finding': json['finding'],
        'affectedUuid': json['affected_uuid'],
        'update': UpdateFindingAffectedRequestFromJSON(json['update']),
        'type': json['type'],
    };
}

export function WsMessageOneOf34ToJSON(value?: WsMessageOneOf34 | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'workspace': value.workspace,
        'finding': value.finding,
        'affected_uuid': value.affectedUuid,
        'update': UpdateFindingAffectedRequestToJSON(value.update),
        'type': value.type,
    };
}
