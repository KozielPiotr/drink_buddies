# pylint: disable=too-few-public-methods, unused-argument, missing-function-docstring, no-self-use
"""All drinking_auth application queries."""
import graphene
import graphql_jwt

from drinking_buddies.decorators import login_forbidden
from drinking_buddies.drinking_auth.models import User
from drinking_buddies.drinking_auth.types import UserType


class CreateUser(graphene.Mutation):
    """Creates new user."""

    user = graphene.Field(UserType)

    class Arguments:
        """Mutation fields."""

        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    @login_forbidden
    def mutate(self, info, username, password, email):
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class AuthMutation(graphene.ObjectType):
    """Mutations for drinking_auth app."""

    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
