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
import type { AggregationType } from './AggregationType';
import {
    AggregationTypeFromJSON,
    AggregationTypeFromJSONTyped,
    AggregationTypeToJSON,
} from './AggregationType';

/**
 * An affected has been added to a finding
 * @export
 * @interface WsMessageOneOf29
 */
export interface WsMessageOneOf29 {
    /**
     * The workspace the updated finding is in
     * @type {string}
     * @memberof WsMessageOneOf29
     */
    workspace: string;
    /**
     * The finding which has been updated
     * @type {string}
     * @memberof WsMessageOneOf29
     */
    finding: string;
    /**
     * The affected's uuid
     * @type {string}
     * @memberof WsMessageOneOf29
     */
    affectedUuid: string;
    /**
     * 
     * @type {AggregationType}
     * @memberof WsMessageOneOf29
     */
    affectedType: AggregationType;
    /**
     * 
     * @type {string}
     * @memberof WsMessageOneOf29
     */
    type: WsMessageOneOf29TypeEnum;
}


/**
 * @export
 */
export const WsMessageOneOf29TypeEnum = {
    AddedFindingAffected: 'AddedFindingAffected'
} as const;
export type WsMessageOneOf29TypeEnum = typeof WsMessageOneOf29TypeEnum[keyof typeof WsMessageOneOf29TypeEnum];


/**
 * Check if a given object implements the WsMessageOneOf29 interface.
 */
export function instanceOfWsMessageOneOf29(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "workspace" in value;
    isInstance = isInstance && "finding" in value;
    isInstance = isInstance && "affectedUuid" in value;
    isInstance = isInstance && "affectedType" in value;
    isInstance = isInstance && "type" in value;

    return isInstance;
}

export function WsMessageOneOf29FromJSON(json: any): WsMessageOneOf29 {
    return WsMessageOneOf29FromJSONTyped(json, false);
}

export function WsMessageOneOf29FromJSONTyped(json: any, ignoreDiscriminator: boolean): WsMessageOneOf29 {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'workspace': json['workspace'],
        'finding': json['finding'],
        'affectedUuid': json['affected_uuid'],
        'affectedType': AggregationTypeFromJSON(json['affected_type']),
        'type': json['type'],
    };
}

export function WsMessageOneOf29ToJSON(value?: WsMessageOneOf29 | null): any {
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
        'affected_type': AggregationTypeToJSON(value.affectedType),
        'type': value.type,
    };
}

