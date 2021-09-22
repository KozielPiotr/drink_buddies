# pylint: disable=missing-docstring
"""
Mutations tests.
"""
import json

from graphene_django.utils import GraphQLTestCase

from drinking_buddies.drinking_auth.models import User


class TestUserCreation(GraphQLTestCase):
    """Test for User mutations."""

    @staticmethod
    def missing_field_error_msg(field, argument, field_type):
        return f'Field "{field}" argument "{argument}" of type "{field_type}" is required but not provided.'

    def test_create_user_mutation(self):
        username = "test_username"
        email = "test_email@test.com"
        password = "test password"

        assert not User.objects.first()
        resp = self.query(
            """
            mutation createUser($username: String!, $email: String!, $password: String!){
              createUser(
                username: $username
                email: $email
                password: $password
              ){
                user{
                  id
                  username
                  email
                }
              }
            }
            """,
            op_name="createUser",
            variables={"username": username, "email": email, "password": password},
        )
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        assert content["data"]["createUser"]["user"]["id"]
        assert content["data"]["createUser"]["user"]["username"] == username
        assert content["data"]["createUser"]["user"]["email"] == email
        new_user = User.objects.first()
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

        assert not User.objects.first()
        resp = self.query(
            """
            mutation createUser($email: String!, $password: String!){
              createUser(
                email: $email
                password: $password
              ){
                user{
                  id
                  username
                  email
                }
              }
            }
            """,
            op_name="createUser",
            variables={"email": email, "password": password},
        )
        content = json.loads(resp.content)
        assert resp.status_code == 400
        self.assertResponseHasErrors(resp)
        assert expected_error_msg == content["errors"][0]["message"]
        assert not User.objects.first()

    def test_create_user_mutation__no_email_raises_error(self):
        username = "test_username"
        password = "test password"
        missing_field = "createUser"
        missing_argument = "email"
        missing_type = "String!"
        expected_error_msg = self.missing_field_error_msg(missing_field, missing_argument, missing_type)

        assert not User.objects.first()
        resp = self.query(
            """
            mutation createUser($username: String!, $password: String!){
              createUser(
                username: $username
                password: $password
              ){
                user{
                  id
                  username
                  email
                }
              }
            }
            """,
            op_name="createUser",
            variables={"username": username, "password": password},
        )
        content = json.loads(resp.content)
        assert resp.status_code == 400
        self.assertResponseHasErrors(resp)
        assert expected_error_msg == content["errors"][0]["message"]
        assert not User.objects.first()

    def test_create_user_mutation__no_password_raises_error(self):
        username = "test_username"
        email = "test_email@test.com"
        missing_field = "createUser"
        missing_argument = "password"
        missing_type = "String!"
        expected_error_msg = self.missing_field_error_msg(missing_field, missing_argument, missing_type)

        assert not User.objects.first()
        resp = self.query(
            """
            mutation createUser($username: String!, $email: String!){
              createUser(
                username: $username
                email: $email
              ){
                user{
                  id
                  username
                  email
                }
              }
            }
            """,
            op_name="createUser",
            variables={"username": username, "email": email},
        )
        content = json.loads(resp.content)
        assert resp.status_code == 400
        self.assertResponseHasErrors(resp)
        assert expected_error_msg == content["errors"][0]["message"]
        assert not User.objects.first()

    def test_create_user_mutation__no_arguments_raises_error(self):
        username = "test_username"
        email = "test_email@test.com"

        assert not User.objects.first()
        resp = self.query(
            """
            mutation createUser(){
              createUser(
              ){
                user{
                  id
                  username
                  email
                }
              }
            }
            """,
            op_name="createUser",
            variables={"username": username, "email": email},
        )
        assert resp.status_code == 400
        self.assertResponseHasErrors(resp)
        assert not User.objects.first()
