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
import type { FullQueryCertificateTransparencyResult } from './FullQueryCertificateTransparencyResult';
import {
    FullQueryCertificateTransparencyResultFromJSON,
    FullQueryCertificateTransparencyResultFromJSONTyped,
    FullQueryCertificateTransparencyResultToJSON,
} from './FullQueryCertificateTransparencyResult';

/**
 * 
 * @export
 * @interface SearchResultEntryOneOf8
 */
export interface SearchResultEntryOneOf8 {
    /**
     * 
     * @type {FullQueryCertificateTransparencyResult}
     * @memberof SearchResultEntryOneOf8
     */
    certificateTransparencyResultEntry: FullQueryCertificateTransparencyResult;
}

/**
 * Check if a given object implements the SearchResultEntryOneOf8 interface.
 */
export function instanceOfSearchResultEntryOneOf8(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "certificateTransparencyResultEntry" in value;

    return isInstance;
}

export function SearchResultEntryOneOf8FromJSON(json: any): SearchResultEntryOneOf8 {
    return SearchResultEntryOneOf8FromJSONTyped(json, false);
}

export function SearchResultEntryOneOf8FromJSONTyped(json: any, ignoreDiscriminator: boolean): SearchResultEntryOneOf8 {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'certificateTransparencyResultEntry': FullQueryCertificateTransparencyResultFromJSON(json['CertificateTransparencyResultEntry']),
    };
}

export function SearchResultEntryOneOf8ToJSON(value?: SearchResultEntryOneOf8 | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'CertificateTransparencyResultEntry': FullQueryCertificateTransparencyResultToJSON(value.certificateTransparencyResultEntry),
    };
}

