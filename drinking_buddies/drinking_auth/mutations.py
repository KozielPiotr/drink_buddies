# pylint: disable=too-few-public-methods, unused-argument, missing-function-docstring, no-self-use
"""All drinking_auth application queries."""
import graphene
from django.contrib.auth import get_user_model

from drinking_buddies.drinking_auth.types import UserType


class CreateUser(graphene.Mutation):
    """Creates new user."""

    user = graphene.Field(UserType)

    class Arguments:
        """Mutation fields."""

        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class AuthMutation(graphene.ObjectType):
    """Mutations for drinking_auth app."""

    create_user = CreateUser.Field()
