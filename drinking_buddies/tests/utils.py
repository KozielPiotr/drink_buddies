"""Utils for tests."""
from graphene_django.utils import GraphQLTestCase
from graphql_jwt.shortcuts import get_token

from drinking_buddies.drinking_auth.models import User


class AuthTestCase(GraphQLTestCase):
    """Class used in tests that require authentication."""

    AUTH_ERROR_MSG = "You do not have permission to perform this action"

    @staticmethod
    def authenticate_user(user: User):
        """Creates authentication header for given user."""
        token = get_token(user)
        return {"HTTP_AUTHORIZATION": f"JWT {token}"}
