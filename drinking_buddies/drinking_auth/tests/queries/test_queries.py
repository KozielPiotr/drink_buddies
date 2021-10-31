# pylint: disable=missing-docstring
"""
Queries tests.
"""

import collections
import json

from drinking_buddies.drinking_auth.models import User
from drinking_buddies.drinking_auth.tests.mixins import UserQueryMixin
from drinking_buddies.tests.utils import AuthTestCase


class TestUsersQuery(AuthTestCase, UserQueryMixin):
    """Tests for users queries."""

    query_name = "allUsers"

    def test_retrieve_all_users(self):
        expected_fields = ["id", "username", "email"]
        count_users = User.objects.count()
        resp = self.retrieve_all_users_query__staff(self.query_name)
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        assert len(content["data"][self.query_name]) == count_users + 1
        retrieved_fields = content["data"][self.query_name][0].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert len(content["data"][self.query_name]) == User.objects.count()

    def test_retrieve_all_users__unauthenticated_user_raises_error(self):
        resp = self.retrieve_all_users_query__unauth(self.query_name)
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseHasErrors(resp)
        assert content["errors"][0]["message"] == self.AUTH_ERROR_MSG
        assert content["errors"][0]["path"][0] == self.query_name

    def test_retrieve_all_users__not_staff_user_raises_error(self):
        resp = self.retrieve_all_users_query__not_staff(self.query_name)
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseHasErrors(resp)
        assert content["errors"][0]["message"] == self.AUTH_ERROR_MSG
        assert content["errors"][0]["path"][0] == self.query_name
