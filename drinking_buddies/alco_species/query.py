# pylint: disable=no-self-argument, unused-argument, no-self-use, too-few-public-methods, invalid-name
"""All alco_species application queries."""
import graphene
from graphene_django import DjangoListField
from graphql_jwt.decorators import login_required

from drinking_buddies.alco_species.models import AlcoholGroup, AlcoholType
from drinking_buddies.alco_species.types import AlcoGroupType, AlcoTypeType


class AlcoTypeQuery(graphene.ObjectType):
    """Schema for full AlcoholType model."""

    type_by_id = graphene.Field(AlcoTypeType, type_id=graphene.UUID())
    all_types = DjangoListField(AlcoTypeType)

    @login_required
    def resolve_type_by_id(root, info, type_id):
        """Returns alcohol type by given id."""

        return AlcoholType.objects.get(pk=type_id)

    @login_required
    def resolve_all_types(root, info, **kwargs):
        """Returns all alcohol types."""

        return AlcoholType.objects.all()


class AlcoGroupQuery(graphene.ObjectType):
    """Schema for full AlcoholGroup model."""

    group_by_id = graphene.Field(AlcoGroupType, group_id=graphene.UUID())
    all_groups = DjangoListField(AlcoGroupType)

    @login_required
    def resolve_group_by_id(root, info, group_id):
        """Returns alcohol group by given id."""

        return AlcoholGroup.objects.get(pk=group_id)

    @login_required
    def resolve_all_groups(root, info, **kwargs):
        """Returns all alcohol groups."""

        return AlcoholGroup.objects.all()
