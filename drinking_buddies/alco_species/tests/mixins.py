# pylint: disable=missing-docstring
"""Mixins for types and groups queries and mutations"""

from drinking_buddies.drinking_auth.tests.factories import UserFactory


class TypeQueryMixin:
    def retrieve_alco_type_by_id_query__auth(self, obj_id, query_name):
        logged_user = UserFactory(is_staff=True)
        headers = self.authenticate_user(logged_user)
        return self.query(
            """
            query typeById($typeId: UUID!){
              typeById(typeId: $typeId){
                id
                name
                description
                groups{
                  id
                }
              }
            }
            """,
            op_name=query_name,
            variables={"typeId": str(obj_id)},
            headers=headers,
        )

    def retrieve_alco_type_by_id_query__unauth(self, obj_id, query_name):
        return self.query(
            """
            query typeById($typeId: UUID!){
              typeById(typeId: $typeId){
                id
                name
                description
                groups{
                  id
                }
              }
            }
            """,
            op_name=query_name,
            variables={"typeId": str(obj_id)},
        )

    def retrieve_all_alco_types_query__auth(self, query_name):
        logged_user = UserFactory(is_staff=True)
        headers = self.authenticate_user(logged_user)
        return self.query(
            """
            query allTypes{
              allTypes{
                id
                name
                description
                groups{
                  id
                }
              }
            }
            """,
            op_name=query_name,
            headers=headers,
        )

    def retrieve_all_alco_types_query__unauth(self, query_name):
        return self.query(
            """
            query allTypes{
              allTypes{
                id
                name
                description
                groups{
                  id
                }
              }
            }
            """,
            op_name=query_name,
        )


class GroupQueryMixin:
    def retrieve_alco_group_by_id_query__auth(self, obj_id, query_name):
        logged_user = UserFactory(is_staff=True)
        headers = self.authenticate_user(logged_user)
        return self.query(
            """
            query groupById($groupId: UUID!){
              groupById(groupId: $groupId){
                id
                name
                type{
                  id
                }
                parentGroup{
                  id
                }
                subGroups{
                  id
                }
              }
            }
            """,
            op_name=query_name,
            variables={"groupId": str(obj_id)},
            headers=headers,
        )

    def retrieve_alco_group_by_id_query__unauth(self, obj_id, query_name):
        return self.query(
            """
            query groupById($groupId: UUID!){
              groupById(groupId: $groupId){
                id
                name
                type{
                  id
                }
                parentGroup{
                  id
                }
                subGroups{
                  id
                }
              }
            }
            """,
            op_name=query_name,
            variables={"groupId": str(obj_id)},
        )

    def retrieve_all_alco_groups_query__auth(self, query_name):
        logged_user = UserFactory(is_staff=True)
        headers = self.authenticate_user(logged_user)
        return self.query(
            """
            query allGroups{
              allGroups{
                id
                name
                type{
                  id
                }
                parentGroup{
                  id
                }
                subGroups{
                  id
                }
              }
            }
            """,
            op_name=query_name,
            headers=headers,
        )

    def retrieve_all_alco_groups_query__unauth(self, query_name):
        return self.query(
            """
            query allGroups{
              allGroups{
                id
                name
                type{
                  id
                }
                parentGroup{
                  id
                }
                subGroups{
                  id
                }
              }
            }
            """,
            op_name=query_name,
        )
