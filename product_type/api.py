from http import HTTPStatus
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.pagination import PageNumberPagination, paginate

from .models import ProductType
from .schemas import (
    ProductTypePublicSchema,
    ProductTypeSchema,
    ProductTypeUpdateSchema,
)

router = Router(tags=['Products_type'])


@router.post(
    path='/',
    response={HTTPStatus.CREATED: ProductTypePublicSchema},
    summary='Adicionar tipo de produto',
)
def create_product_type(request, product_type: ProductTypeSchema):
    new_product_type = ProductType.objects.create(**product_type.dict())

    return new_product_type


@router.get(
    path='/',
    response={HTTPStatus.OK: List[ProductTypePublicSchema]},
    summary='Listar tipos de produto',
)
@paginate(PageNumberPagination)
def list_products_type(request, parent: int | None = None):
    queryset = ProductType.objects.all()

    if parent:
        try:
            parent_object = ProductType.objects.get(pk=parent)
            queryset = parent_object.get_descendants(include_self=True)
        except ProductType.DoesNotExist:
            queryset.none()

    return queryset


@router.get(
    path='/{product_type_id}',
    response={HTTPStatus.OK: ProductTypePublicSchema},
    summary='Buscar tipo de produto por id',
)
def get_product_type(
    request,
    product_type_id: int,
):
    product_type = get_object_or_404(ProductType, id=product_type_id)

    return product_type


@router.get(
    path='/name/{str:product_type_name}',
    response={HTTPStatus.OK: ProductTypePublicSchema},
    summary='Buscar tipo de produto por nome',
)
def get_product_type_by_name(request, product_type_name: str):
    product_type = get_object_or_404(
        ProductType, name__iexact=product_type_name
    )

    return product_type


@router.put(
    path='/{product_type_id}',
    response={HTTPStatus.OK: ProductTypePublicSchema},
    summary='Atualizar tipo de produto',
)
def update_product_type(
    request,
    product_type_id: int,
    product_type_update: ProductTypeUpdateSchema,
):
    product = get_object_or_404(ProductType, id=product_type_id)

    update_data = product_type_update.model_dump(exclude_unset=True)

    for attr, value in update_data.items():
        setattr(product, attr, value)

    product.save()
    return product


@router.delete(
    path='/{product_type_id}',
    response={HTTPStatus.NO_CONTENT: None},
    summary='Deletar tipo de produto',
)
def delete_product_type(request, product_type_id: int):
    product = get_object_or_404(ProductType, id=product_type_id)

    product.delete()
