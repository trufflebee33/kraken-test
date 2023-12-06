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

from datetime import datetime
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from kraken_sdk.models.simple_aggregation_source import SimpleAggregationSource
from kraken_sdk.models.simple_tag import SimpleTag
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FullDomain(BaseModel):
    """
    A full representation of a domain in a workspace
    """ # noqa: E501
    uuid: StrictStr = Field(description="The primary key of the domain")
    domain: StrictStr = Field(description="The domain's name")
    comment: StrictStr = Field(description="A comment")
    workspace: StrictStr = Field(description="The workspace this domain is in")
    tags: List[SimpleTag] = Field(description="The list of tags this domain has attached to")
    sources: SimpleAggregationSource
    created_at: datetime = Field(description="The point in time, the record was created")
    __properties: ClassVar[List[str]] = ["uuid", "domain", "comment", "workspace", "tags", "sources", "created_at"]

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
        """Create an instance of FullDomain from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of sources
        if self.sources:
            _dict['sources'] = self.sources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FullDomain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "domain": obj.get("domain"),
            "comment": obj.get("comment"),
            "workspace": obj.get("workspace"),
            "tags": [SimpleTag.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "sources": SimpleAggregationSource.from_dict(obj.get("sources")) if obj.get("sources") is not None else None,
            "created_at": obj.get("created_at")
        })
        return _obj


