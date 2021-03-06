# pylint: disable=unused-argument, no-self-argument, no-self-use
"""All drinking_auth application queries."""
import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoListField
from graphql_jwt.decorators import staff_member_required

from drinking_buddies.drinking_auth.types import UserType


class UserQuery(graphene.ObjectType):
    """Query for User model."""

    all_users = DjangoListField(UserType)

    @staff_member_required
    def resolve_all_users(root, info, **kwargs):
        """Returns all users types."""
        return get_user_model().objects.all()
