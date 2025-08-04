from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Data")


@_attrs_define
class Data:
    """Data of powers and frequencies with their timestamps

    Attributes:
        power (float):  Example: 50.0.
        frequency (float):  Example: 106.2.
        time (Union[Unset, str]):  Example: 06-06-2025 12:13:36.
    """

    power: float
    frequency: float
    time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        power = self.power

        frequency = self.frequency

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "power": power,
                "frequency": frequency,
            }
        )
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        power = d.pop("power")

        frequency = d.pop("frequency")

        time = d.pop("time", UNSET)

        data = cls(
            power=power,
            frequency=frequency,
            time=time,
        )

        data.additional_properties = d
        return data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
