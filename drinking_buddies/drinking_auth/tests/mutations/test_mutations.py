# pylint: disable=missing-docstring
"""
Mutations tests.
"""
import json

from django.contrib.auth import get_user_model

from drinking_buddies.drinking_auth.tests.mixins import UserMutationMixin
from drinking_buddies.tests.utils import AuthTestCase


class TestUserCreation(AuthTestCase, UserMutationMixin):
    """Test for new user creation."""

    mutation_name = "createUser"

    @staticmethod
    def missing_field_error_msg(field, argument, field_type):
        return f'Field "{field}" argument "{argument}" of type "{field_type}" is required but not provided.'

    def test_create_user_mutation_(self):
        username = "test_username"
        email = "test_email@test.com"
        password = "test password"
        assert not get_user_model().objects.first()
        resp = self.create_user_mutation__unauth(self.mutation_name, username, email, password)
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        assert content["data"][self.mutation_name]["user"]["id"]
        assert content["data"][self.mutation_name]["user"]["username"] == username
        assert content["data"][self.mutation_name]["user"]["email"] == email
        new_user = get_user_model().objects.first()
        assert new_user
        assert new_user.username == username
        assert new_user.email == email

    def test_create_user_mutation__no_username_raises_error(self):
        email = "test_email@test.com"
        password = "test password"
        missing_field = "createUser"
        missing_argument = "username"
        missing_type = "String!"
        expected_error_msg = self.missing_field_error_msg(missing_field, missing_argument, missing_type)

        assert get_user_model().objects.count() == 0
        resp = self.create_user_mutation_no_username(self.mutation_name, email, password)
        content = json.loads(resp.content)
        assert resp.status_code == 400
        self.assertResponseHasErrors(resp)
        assert expected_error_msg == content["errors"][0]["message"]
        assert get_user_model().objects.count() == 0

    def test_create_user_mutation__no_email_raises_error(self):
        username = "test_username"
        password = "test password"
        missing_field = "createUser"
        missing_argument = "email"
        missing_type = "String!"
        expected_error_msg = self.missing_field_error_msg(missing_field, missing_argument, missing_type)

        assert get_user_model().objects.count() == 0
        resp = self.create_user_mutation_no_email(self.mutation_name, username, password)
        content = json.loads(resp.content)
        assert resp.status_code == 400
        self.assertResponseHasErrors(resp)
        assert expected_error_msg == content["errors"][0]["message"]
        assert get_user_model().objects.count() == 0

    def test_create_user_mutation__no_password_raises_error(self):
        username = "test_username"
        email = "test_email@test.com"
        missing_field = "createUser"
        missing_argument = "password"
        missing_type = "String!"
        expected_error_msg = self.missing_field_error_msg(missing_field, missing_argument, missing_type)

        assert get_user_model().objects.count() == 0
        resp = self.create_user_mutation_no_password(self.mutation_name, username, email)
        content = json.loads(resp.content)
        assert resp.status_code == 400
        self.assertResponseHasErrors(resp)
        assert expected_error_msg == content["errors"][0]["message"]
        assert get_user_model().objects.count() == 0

    def test_create_user_mutation__no_arguments_raises_error(self):
        assert get_user_model().objects.count() == 0
        resp = self.create_user_mutation_no_arguments(self.mutation_name)
        assert resp.status_code == 400
        self.assertResponseHasErrors(resp)
        assert get_user_model().objects.count() == 0

    def test_create_user_mutation__authenticated_user_raises_error(self):
        username = "example_username"
        email = "example_email@test.com"
        password = "example password"

        users_count = get_user_model().objects.count()
        resp = self.create_user_mutation__auth(self.mutation_name, username, email, password)
        content = json.loads(resp.content)
        assert resp.status_code == 200
        self.assertResponseHasErrors(resp)
        assert content["errors"][0]["message"] == self.AUTH_ERROR_MSG
        assert content["errors"][0]["path"][0] == self.mutation_name
        assert content["data"][self.mutation_name] is None
        assert get_user_model().objects.count() == users_count + 1  # no user created except the one sending request
