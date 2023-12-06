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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from kraken_sdk.models.simple_tcp_port_scan_result import SimpleTcpPortScanResult
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SearchResultEntryOneOf5(BaseModel):
    """
    SearchResultEntryOneOf5
    """ # noqa: E501
    tcp_port_scan_result_entry: SimpleTcpPortScanResult = Field(alias="TcpPortScanResultEntry")
    __properties: ClassVar[List[str]] = ["TcpPortScanResultEntry"]

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
        """Create an instance of SearchResultEntryOneOf5 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tcp_port_scan_result_entry
        if self.tcp_port_scan_result_entry:
            _dict['TcpPortScanResultEntry'] = self.tcp_port_scan_result_entry.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SearchResultEntryOneOf5 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TcpPortScanResultEntry": SimpleTcpPortScanResult.from_dict(obj.get("TcpPortScanResultEntry")) if obj.get("TcpPortScanResultEntry") is not None else None
        })
        return _obj


