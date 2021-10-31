# pylint: disable=missing-docstring
"""Mixins for User queries and mutations"""

from drinking_buddies.drinking_auth.tests.factories import UserFactory


class UserQueryMixin:
    def retrieve_all_users_query__staff(self, query_name):
        logged_user = UserFactory(is_staff=True)
        headers = self.authenticate_user(logged_user)
        return self.query(
            """
            query allUsers{
              allUsers{
                id
                username
                email
              }
            }
            """,
            op_name=query_name,
            headers=headers,
        )

    def retrieve_all_users_query__unauth(self, query_name):
        return self.query(
            """
            query allUsers{
              allUsers{
                id
                username
                email
              }
            }
            """,
            op_name=query_name,
        )

    def retrieve_all_users_query__not_staff(self, query_name):
        logged_user = UserFactory()
        headers = self.authenticate_user(logged_user)
        return self.query(
            """
            query allUsers{
              allUsers{
                id
                username
                email
              }
            }
            """,
            op_name=query_name,
            headers=headers,
        )


class UserMutationMixin:
    def create_user_mutation__unauth(self, mutation_name, username, email, password):
        return self.query(
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
            op_name=mutation_name,
            variables={"username": username, "email": email, "password": password},
        )

    def create_user_mutation_no_username(self, mutation_name, email, password):
        return self.query(
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
            op_name=mutation_name,
            variables={"email": email, "password": password},
        )

    def create_user_mutation_no_email(self, mutation_name, username, password):
        return self.query(
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
            op_name=mutation_name,
            variables={"username": username, "password": password},
        )

    def create_user_mutation_no_password(self, mutation_name, username, email):
        return self.query(
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
            op_name=mutation_name,
            variables={"username": username, "email": email},
        )

    def create_user_mutation_no_arguments(self, mutation_name):
        return self.query(
            """
            mutation createUser{
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
            op_name=mutation_name,
            variables={},
        )

    def create_user_mutation__auth(self, mutation_name, username, email, password):
        logged_user = UserFactory()
        headers = self.authenticate_user(logged_user)
        return self.query(
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
            op_name=mutation_name,
            variables={"username": username, "email": email, "password": password},
            headers=headers,
        )
