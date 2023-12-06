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

class HostsAliveRequest(BaseModel):
    """
    Host Alive check request
    """ # noqa: E501
    leech_uuid: Optional[StrictStr] = Field(default=None, description="The leech to use  Leave empty to use a random leech")
    targets: List[StrictStr] = Field(description="The ip addresses / networks to scan")
    timeout: Annotated[int, Field(strict=True, ge=0)] = Field(description="The time to wait until a host is considered down.  The timeout is specified in milliseconds.")
    concurrent_limit: Annotated[int, Field(strict=True, ge=0)] = Field(description="The concurrent task limit")
    workspace_uuid: StrictStr = Field(description="The workspace to execute the attack in")
    __properties: ClassVar[List[str]] = ["leech_uuid", "targets", "timeout", "concurrent_limit", "workspace_uuid"]

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
        """Create an instance of HostsAliveRequest from a JSON string"""
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
        # set to None if leech_uuid (nullable) is None
        # and model_fields_set contains the field
        if self.leech_uuid is None and "leech_uuid" in self.model_fields_set:
            _dict['leech_uuid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of HostsAliveRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "leech_uuid": obj.get("leech_uuid"),
            "targets": obj.get("targets"),
            "timeout": obj.get("timeout"),
            "concurrent_limit": obj.get("concurrent_limit"),
            "workspace_uuid": obj.get("workspace_uuid")
        })
        return _obj


