# pylint: disable=missing-docstring
"""
Queries tests.
"""

import collections
import json

from graphene_django.utils import GraphQLTestCase

from drinking_buddies.drinking_auth.models import User
from drinking_buddies.drinking_auth.tests.factories import UserFactory


class TestUserQuery(GraphQLTestCase):
    """Tests for users queries."""

    def test_retrieve_all_users(self):
        UserFactory()
        expected_fields = ["id", "username", "email"]
        resp = self.query(
            """
            query{
              allUsers{
                id
                username
                email
              }
            }
            """
        )
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"]["allUsers"][0].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert len(content["data"]["allUsers"]) == User.objects.count()
