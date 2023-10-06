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
import type { FullApiKey } from './FullApiKey';
import {
    FullApiKeyFromJSON,
    FullApiKeyFromJSONTyped,
    FullApiKeyToJSON,
} from './FullApiKey';

/**
 * The response that contains all api keys
 * @export
 * @interface GetApiKeysResponse
 */
export interface GetApiKeysResponse {
    /**
     * 
     * @type {Array<FullApiKey>}
     * @memberof GetApiKeysResponse
     */
    keys: Array<FullApiKey>;
}

/**
 * Check if a given object implements the GetApiKeysResponse interface.
 */
export function instanceOfGetApiKeysResponse(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "keys" in value;

    return isInstance;
}

export function GetApiKeysResponseFromJSON(json: any): GetApiKeysResponse {
    return GetApiKeysResponseFromJSONTyped(json, false);
}

export function GetApiKeysResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): GetApiKeysResponse {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'keys': ((json['keys'] as Array<any>).map(FullApiKeyFromJSON)),
    };
}

export function GetApiKeysResponseToJSON(value?: GetApiKeysResponse | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'keys': ((value.keys as Array<any>).map(FullApiKeyToJSON)),
    };
}

