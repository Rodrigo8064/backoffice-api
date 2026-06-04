from ninja import Schema
from pydantic import ConfigDict


class CategorySchema(Schema):
    name: str
    url: str
    is_active: bool = True
    notes: str | None = None
    parent_id: None | int = None


class CategoryPublicSchema(Schema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    url: str
    is_active: bool
    notes: str
    full_path: str


class CategoryUpdateSchema(Schema):
    name: None | str = None
    url: None | str = None
    is_active: None | str = None
    notes: None | str = None
    parent: None | int = None


class FamilyPublicSchema(Schema):
    id: int
    name: str
