# pylint: disable=too-few-public-methods
"""Types for alco_species schemas."""
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    """Type for User model."""

    class Meta:
        model = get_user_model()
