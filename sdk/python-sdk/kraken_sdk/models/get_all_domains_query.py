# coding: utf-8

"""
    kraken

    The core component of kraken-project

    The version of the OpenAPI document: 0.1.0
    Contact: git@omikron.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetAllDomainsQuery(BaseModel):
    """
    Query parameters for filtering the domains to get
    """ # noqa: E501
    limit: Annotated[int, Field(strict=True, ge=0)] = Field(description="Number of items to retrieve")
    offset: Annotated[int, Field(strict=True, ge=0)] = Field(description="Position in the whole list to start retrieving from")
    host: Optional[StrictStr] = Field(default=None, description="Only get domains pointing to a specific host  This includes domains which point to another domain which points to this host.")
    global_filter: Optional[StrictStr] = Field(default=None, description="An optional general filter to apply")
    domain_filter: Optional[StrictStr] = Field(default=None, description="An optional domain specific filter to apply")
    __properties: ClassVar[List[str]] = ["limit", "offset", "host", "global_filter", "domain_filter"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GetAllDomainsQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if host (nullable) is None
        # and model_fields_set contains the field
        if self.host is None and "host" in self.model_fields_set:
            _dict['host'] = None

        # set to None if global_filter (nullable) is None
        # and model_fields_set contains the field
        if self.global_filter is None and "global_filter" in self.model_fields_set:
            _dict['global_filter'] = None

        # set to None if domain_filter (nullable) is None
        # and model_fields_set contains the field
        if self.domain_filter is None and "domain_filter" in self.model_fields_set:
            _dict['domain_filter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetAllDomainsQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "host": obj.get("host"),
            "global_filter": obj.get("global_filter"),
            "domain_filter": obj.get("domain_filter")
        })
        return _obj


