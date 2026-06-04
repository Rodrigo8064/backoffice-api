from ninja import Schema
from pydantic import ConfigDict


class ProductTypeSchema(Schema):
    name: str
    is_active: bool = True
    parent_id: None | int = None


class ProductTypePublicSchema(Schema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    is_active: bool
    full_path: str


class ProductTypeUpdateSchema(Schema):
    name: None | str
    is_active: None | str = None
    parent: None | int = None
