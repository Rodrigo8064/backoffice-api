from http import HTTPStatus
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from category.models import Family
from .models import Attribute
from .schemas import (
    AttributePublicSchema,
    AttributeSchema,
    AttributeUpdateSchema
)


router = Router(tags=['attributes'])


@router.post(
    path='/',
    response={HTTPStatus.CREATED: AttributePublicSchema},
    summary='Adicionar atributo'
)
def create_attribute(
    request,
    attribute: AttributeSchema
):
    families_id = attribute.families_id

    new_attribute = Attribute.objects.create(
        name=attribute.name,
        expected_value=attribute.expected_value,
        is_active=attribute.is_active,
    )

    new_attribute.families.set(
        Family.objects.filter(id__in=families_id)
    )

    return new_attribute


@router.get(
        path='/',
        response={HTTPStatus.OK: List[AttributePublicSchema]},
        summary='Listar atributos'
)
def list_attributes(
    request,
):
    queryset = Attribute.objects.prefetch_related('families')

    return queryset


@router.get(
    path='/{attribute_id}',
    response={HTTPStatus.OK: AttributePublicSchema},
    summary='Buscar atributo por id'
)
def get_attribute(
    request,
    attribute_id: int
):
    attribute = get_object_or_404(
        Attribute.objects.prefetch_related('families'),
        id=attribute_id
    )
    return attribute


@router.put(
    '/{attribute_id}',
    response={HTTPStatus.OK: AttributePublicSchema},
    summary='Atualizar atributo',
)
def update_attribute(
    request,
    attribute_id: int,
    attribute_update: AttributeUpdateSchema
):
    attribute = get_object_or_404(
        Attribute.objects.prefetch_related('families'), id=attribute_id
    )
    update_data = attribute_update.dict(exclude_unset=True)
    families_id = update_data.pop('families_id', None)

    for attr, value in update_data.items():
        setattr(attribute, attr, value)

    attribute.save()

    if families_id is not None:
        attribute.families.set(
            Family.objects.filter(id__in=families_id)
        )

    return attribute


@router.delete(
    '/{attribute_id}',
    response={HTTPStatus.NO_CONTENT: None},
    summary='Deletar atributo',
)
def delete_attributo(
    request,
    attribute_id: int
):
    attribute = get_object_or_404(Attribute, id=attribute_id)
    attribute.delete()
    return
