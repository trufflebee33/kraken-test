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
import type { Change } from './Change';
import {
    ChangeFromJSON,
    ChangeFromJSONTyped,
    ChangeToJSON,
} from './Change';
import type { EditorTarget } from './EditorTarget';
import {
    EditorTargetFromJSON,
    EditorTargetFromJSONTyped,
    EditorTargetToJSON,
} from './EditorTarget';
import type { SimpleUser } from './SimpleUser';
import {
    SimpleUserFromJSON,
    SimpleUserFromJSONTyped,
    SimpleUserToJSON,
} from './SimpleUser';

/**
 * A finding definition was updated
 * @export
 * @interface WsMessageOneOf29
 */
export interface WsMessageOneOf29 {
    /**
     * 
     * @type {Change}
     * @memberof WsMessageOneOf29
     */
    change: Change;
    /**
     * 
     * @type {SimpleUser}
     * @memberof WsMessageOneOf29
     */
    user: SimpleUser;
    /**
     * 
     * @type {EditorTarget}
     * @memberof WsMessageOneOf29
     */
    target: EditorTarget;
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
    EditorChangedContent: 'EditorChangedContent'
} as const;
export type WsMessageOneOf29TypeEnum = typeof WsMessageOneOf29TypeEnum[keyof typeof WsMessageOneOf29TypeEnum];


/**
 * Check if a given object implements the WsMessageOneOf29 interface.
 */
export function instanceOfWsMessageOneOf29(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "change" in value;
    isInstance = isInstance && "user" in value;
    isInstance = isInstance && "target" in value;
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
        
        'change': ChangeFromJSON(json['change']),
        'user': SimpleUserFromJSON(json['user']),
        'target': EditorTargetFromJSON(json['target']),
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
        
        'change': ChangeToJSON(value.change),
        'user': SimpleUserToJSON(value.user),
        'target': EditorTargetToJSON(value.target),
        'type': value.type,
    };
}

