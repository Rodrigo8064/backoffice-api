from typing import List

from ninja import Schema
from pydantic import ConfigDict, Field

from category.schemas import FamilyPublicSchema

class AttributeSchema(Schema):
    name: str
    expected_value: None | str = None
    is_active: bool = True
    families_id: List[int] = Field(default_factory=list)


class AttributePublicSchema(Schema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    expected_value: None | str = None
    is_active: bool
    families: List[FamilyPublicSchema] = Field(default_factory=list)


class AttributeUpdateSchema(Schema):
    name: None | str
    expected_value: None | str
    is_active: None | bool = True
    families_id: List[int] = []
