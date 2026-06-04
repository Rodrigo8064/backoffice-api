from http import HTTPStatus
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Category
from .schemas import (
    CategoryPublicSchema,
    CategorySchema,
    CategoryUpdateSchema
)


router = Router(tags=['Cotegories'])


@router.post(
    path='/',
    response={HTTPStatus.CREATED: CategoryPublicSchema},
    summary='Adicionar categoria'
)
def create_category(
    request,
    category: CategorySchema
):
    parent = None

    if category.parent_id:
        parent = get_object_or_404(
            Category,
            id=category.parent_id
        )

    new_category = Category.objects.create(
        **category.dict()
    )

    return new_category


@router.get(
    path='/',
    response={HTTPStatus.OK: List[CategoryPublicSchema]},
    summary='Listar categorias'
)
def list_categories(
    request,
    parent: int | None = None
):
    queryset = Category.objects.all()

    if parent:
        try:
            parent_object = Category.objects.get(pk=parent)
            queryset = parent_object.get_descendants(include_self=True)
        except Category.DoesNotExist:
            queryset.none()

    return queryset


@router.get(
    path='/{category_id}',
    response={HTTPStatus.OK: CategoryPublicSchema},
    summary='Buscar categoria por id'
)
def get_category(
    request,
    category_id: int,
):
    category = get_object_or_404(
        Category, id=category_id
    )

    return category


@router.get(
    path='/name/{str:category_name}',
    response={HTTPStatus.OK: CategoryPublicSchema},
    summary='Buscar categoria por nome'
)
def get_category_by_name(
    request,
    category_name: str
):
    category = get_object_or_404(
        Category, name__iexact=category_name
    )

    return category


@router.put(
    path='/{category_id}',
    response={HTTPStatus.CREATED: CategoryPublicSchema},
    summary='Atualizar categoria'
)
def update_category(
    request,
    category_id: int,
    category_update: CategoryUpdateSchema,
):
    category = get_object_or_404(
        Category, id=category_id
    )

    update_data = category_update.model_dump(exclude_unset=True)

    for attr, value in update_data.items():
        setattr(category, attr, value)
    
    category.save()
    return category


@router.delete(
    path='/{category_id}',
    response={HTTPStatus.NO_CONTENT: None},
    summary='Deletar categoria'
)
def delete_category(
    request,
    category_id: int
):
    category = get_object_or_404(
        Category, id=category_id
    )

    category.delete()
    return 
