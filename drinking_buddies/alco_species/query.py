# pylint: disable=no-self-argument, unused-argument, no-self-use, too-few-public-methods
"""All alco_species application queries."""
import graphene
from graphene_django import DjangoListField

from drinking_buddies.alco_species.models import AlcoholGroup, AlcoholType
from drinking_buddies.alco_species.types import AlcoGroupType, AlcoTypeType


class AlcoTypeQuery(graphene.ObjectType):
    """Schema for full AlcoholType model."""

    type_by_id = graphene.Field(AlcoTypeType, id=graphene.UUID())
    all_types = DjangoListField(AlcoTypeType)

    def resolve_type_by_id(root, info, id):
        """Returns alcohol type by given id."""

        return AlcoholType.objects.get(pk=id)

    def resolve_all_types(root, info, **kwargs):
        """Returns all alcohol types."""

        return AlcoholType.objects.all()


class AlcoGroupQuery(graphene.ObjectType):
    """Schema for full AlcoholGroup model."""

    group_by_id = graphene.Field(AlcoGroupType, id=graphene.UUID())
    all_groups = DjangoListField(AlcoGroupType)

    def resolve_group_by_id(root, info, id):
        """Returns alcohol group by given id."""

        return AlcoholGroup.objects.get(pk=id)

    def resolve_all_groups(root, info, **kwargs):
        """Returns all alcohol groups."""

        return AlcoholGroup.objects.all()
