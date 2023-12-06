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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from kraken_sdk.models.ws_message_one_of import WsMessageOneOf
from kraken_sdk.models.ws_message_one_of1 import WsMessageOneOf1
from kraken_sdk.models.ws_message_one_of10 import WsMessageOneOf10
from kraken_sdk.models.ws_message_one_of2 import WsMessageOneOf2
from kraken_sdk.models.ws_message_one_of3 import WsMessageOneOf3
from kraken_sdk.models.ws_message_one_of4 import WsMessageOneOf4
from kraken_sdk.models.ws_message_one_of5 import WsMessageOneOf5
from kraken_sdk.models.ws_message_one_of6 import WsMessageOneOf6
from kraken_sdk.models.ws_message_one_of7 import WsMessageOneOf7
from kraken_sdk.models.ws_message_one_of8 import WsMessageOneOf8
from kraken_sdk.models.ws_message_one_of9 import WsMessageOneOf9
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

WSMESSAGE_ONE_OF_SCHEMAS = ["WsMessageOneOf", "WsMessageOneOf1", "WsMessageOneOf10", "WsMessageOneOf2", "WsMessageOneOf3", "WsMessageOneOf4", "WsMessageOneOf5", "WsMessageOneOf6", "WsMessageOneOf7", "WsMessageOneOf8", "WsMessageOneOf9"]

class WsMessage(BaseModel):
    """
    Message that is sent via websocket
    """
    # data type: WsMessageOneOf
    oneof_schema_1_validator: Optional[WsMessageOneOf] = None
    # data type: WsMessageOneOf1
    oneof_schema_2_validator: Optional[WsMessageOneOf1] = None
    # data type: WsMessageOneOf2
    oneof_schema_3_validator: Optional[WsMessageOneOf2] = None
    # data type: WsMessageOneOf3
    oneof_schema_4_validator: Optional[WsMessageOneOf3] = None
    # data type: WsMessageOneOf4
    oneof_schema_5_validator: Optional[WsMessageOneOf4] = None
    # data type: WsMessageOneOf5
    oneof_schema_6_validator: Optional[WsMessageOneOf5] = None
    # data type: WsMessageOneOf6
    oneof_schema_7_validator: Optional[WsMessageOneOf6] = None
    # data type: WsMessageOneOf7
    oneof_schema_8_validator: Optional[WsMessageOneOf7] = None
    # data type: WsMessageOneOf8
    oneof_schema_9_validator: Optional[WsMessageOneOf8] = None
    # data type: WsMessageOneOf9
    oneof_schema_10_validator: Optional[WsMessageOneOf9] = None
    # data type: WsMessageOneOf10
    oneof_schema_11_validator: Optional[WsMessageOneOf10] = None
    actual_instance: Optional[Union[WsMessageOneOf, WsMessageOneOf1, WsMessageOneOf10, WsMessageOneOf2, WsMessageOneOf3, WsMessageOneOf4, WsMessageOneOf5, WsMessageOneOf6, WsMessageOneOf7, WsMessageOneOf8, WsMessageOneOf9]] = None
    one_of_schemas: List[str] = Literal["WsMessageOneOf", "WsMessageOneOf1", "WsMessageOneOf10", "WsMessageOneOf2", "WsMessageOneOf3", "WsMessageOneOf4", "WsMessageOneOf5", "WsMessageOneOf6", "WsMessageOneOf7", "WsMessageOneOf8", "WsMessageOneOf9"]

    model_config = {
        "validate_assignment": True
    }


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = WsMessage.model_construct()
        error_messages = []
        match = 0
        # validate data type: WsMessageOneOf
        if not isinstance(v, WsMessageOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf`")
        else:
            match += 1
        # validate data type: WsMessageOneOf1
        if not isinstance(v, WsMessageOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf1`")
        else:
            match += 1
        # validate data type: WsMessageOneOf2
        if not isinstance(v, WsMessageOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf2`")
        else:
            match += 1
        # validate data type: WsMessageOneOf3
        if not isinstance(v, WsMessageOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf3`")
        else:
            match += 1
        # validate data type: WsMessageOneOf4
        if not isinstance(v, WsMessageOneOf4):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf4`")
        else:
            match += 1
        # validate data type: WsMessageOneOf5
        if not isinstance(v, WsMessageOneOf5):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf5`")
        else:
            match += 1
        # validate data type: WsMessageOneOf6
        if not isinstance(v, WsMessageOneOf6):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf6`")
        else:
            match += 1
        # validate data type: WsMessageOneOf7
        if not isinstance(v, WsMessageOneOf7):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf7`")
        else:
            match += 1
        # validate data type: WsMessageOneOf8
        if not isinstance(v, WsMessageOneOf8):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf8`")
        else:
            match += 1
        # validate data type: WsMessageOneOf9
        if not isinstance(v, WsMessageOneOf9):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf9`")
        else:
            match += 1
        # validate data type: WsMessageOneOf10
        if not isinstance(v, WsMessageOneOf10):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WsMessageOneOf10`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in WsMessage with oneOf schemas: WsMessageOneOf, WsMessageOneOf1, WsMessageOneOf10, WsMessageOneOf2, WsMessageOneOf3, WsMessageOneOf4, WsMessageOneOf5, WsMessageOneOf6, WsMessageOneOf7, WsMessageOneOf8, WsMessageOneOf9. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in WsMessage with oneOf schemas: WsMessageOneOf, WsMessageOneOf1, WsMessageOneOf10, WsMessageOneOf2, WsMessageOneOf3, WsMessageOneOf4, WsMessageOneOf5, WsMessageOneOf6, WsMessageOneOf7, WsMessageOneOf8, WsMessageOneOf9. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into WsMessageOneOf
        try:
            instance.actual_instance = WsMessageOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf1
        try:
            instance.actual_instance = WsMessageOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf2
        try:
            instance.actual_instance = WsMessageOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf3
        try:
            instance.actual_instance = WsMessageOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf4
        try:
            instance.actual_instance = WsMessageOneOf4.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf5
        try:
            instance.actual_instance = WsMessageOneOf5.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf6
        try:
            instance.actual_instance = WsMessageOneOf6.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf7
        try:
            instance.actual_instance = WsMessageOneOf7.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf8
        try:
            instance.actual_instance = WsMessageOneOf8.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf9
        try:
            instance.actual_instance = WsMessageOneOf9.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WsMessageOneOf10
        try:
            instance.actual_instance = WsMessageOneOf10.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into WsMessage with oneOf schemas: WsMessageOneOf, WsMessageOneOf1, WsMessageOneOf10, WsMessageOneOf2, WsMessageOneOf3, WsMessageOneOf4, WsMessageOneOf5, WsMessageOneOf6, WsMessageOneOf7, WsMessageOneOf8, WsMessageOneOf9. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into WsMessage with oneOf schemas: WsMessageOneOf, WsMessageOneOf1, WsMessageOneOf10, WsMessageOneOf2, WsMessageOneOf3, WsMessageOneOf4, WsMessageOneOf5, WsMessageOneOf6, WsMessageOneOf7, WsMessageOneOf8, WsMessageOneOf9. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


