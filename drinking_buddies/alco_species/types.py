# pylint: disable=too-few-public-methods
"""Types for alco_species schemas."""
from graphene_django import DjangoObjectType

from drinking_buddies.alco_species.models import AlcoholGroup, AlcoholType


class AlcoTypeType(DjangoObjectType):
    """Type for AlcoholType model."""

    class Meta:
        model = AlcoholType
        fields = ("id", "name", "groups", "description")


class AlcoGroupType(DjangoObjectType):
    """Type for AlcoholType model."""

    class Meta:
        model = AlcoholGroup
        fields = ("id", "name", "type", "parent", "sub_groups")
