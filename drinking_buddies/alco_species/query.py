# pylint: disable=no-self-argument, unused-argument, no-self-use, too-few-public-methods
"""All alco_species application queries."""
import graphene
from graphene_django import DjangoListField

from drinking_buddies.alco_species.models import AlcoholGroup, AlcoholType
from drinking_buddies.alco_species.types import AlcoGroupType, AlcoTypeType


class AlcoTypeQuery(graphene.ObjectType):
    """Schema for full AlcoholType model."""

    all_types = DjangoListField(AlcoTypeType)

    def resolve_all_types(root, info, **kwargs):
        """Returns all alcohol types."""

        return AlcoholType.objects.all()


class AlcoGroupQuery(graphene.ObjectType):
    """Schema for full AlcoholGroup model."""

    all_groups_no_parent = DjangoListField(AlcoGroupType)

    def resolve_all_groups_no_parent(root, info, **kwargs):
        """Returns all alcohol groups without parent."""

        return AlcoholGroup.objects.filter(parent=None).all()
