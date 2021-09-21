# pylint: disable=missing-docstring
"""
Queries tests.
"""

import collections
import json

from graphene_django.utils import GraphQLTestCase

from drinking_buddies.alco_species.models import AlcoholGroup, AlcoholType


class TestAlcoTypeQuery(GraphQLTestCase):
    """Tests for alcohol types queries."""

    fixtures = ["species.json"]

    def retrieve_alco_type_by_id_query(self, obj_id):
        return self.query(
            """
            query typeById($id: UUID!){
              typeById(id: $id){
                id
                name
                description
                groups{
                  id
                }
              }
            }
            """,
            op_name="typeById",
            variables={"id": str(obj_id)},
        )

    def retrieve_all_alco_types_query(self):
        return self.query(
            """
            query{
              allTypes{
                id
                name
                description
                groups{
                  id
                }
              }
            }
            """
        )

    def test_retrieve_alco_type_by_id(self):
        obj = AlcoholType.objects.all()[0]
        resp = self.retrieve_alco_type_by_id_query(obj.id)
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "description", "groups"]

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"]["typeById"].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert content["data"]["typeById"]["id"] == str(obj.id)
        assert content["data"]["typeById"]["name"] == obj.name
        assert content["data"]["typeById"]["description"] == obj.description
        assert len(content["data"]["typeById"]["groups"]) == len(obj.groups.all())

    def test_retrieve_all_types(self):
        resp = self.retrieve_all_alco_types_query()
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "description", "groups"]

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"]["allTypes"][0].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert len(content["data"]["allTypes"]) == AlcoholType.objects.count()


class TestAlcoGroupQuery(GraphQLTestCase):
    """Tests for alcohol types queries."""

    fixtures = ["species.json"]

    def retrieve_alco_group_by_id_query(self, obj_id):
        return self.query(
            """
            query groupById($id: UUID!){
              groupById(id: $id){
                id
                name
                type{
                  id
                }
                parent{
                  id
                }
                subGroups{
                  id
                }
              }
            }
            """,
            op_name="groupById",
            variables={"id": str(obj_id)},
        )

    def retrieve_all_alco_groups_query(self):
        return self.query(
            """
            query{
              allGroups{
                id
                name
                type{
                  id
                }
                parent{
                  id
                }
                subGroups{
                  id
                }
              }
            }
            """
        )

    def test_retrieve_alco_group_by_id(self):
        obj = AlcoholGroup.objects.all()[0]
        resp = self.retrieve_alco_group_by_id_query(obj.id)
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "type", "parent", "subGroups"]

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"]["groupById"].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert content["data"]["groupById"]["id"] == str(obj.id)
        assert content["data"]["groupById"]["name"] == obj.name
        assert content["data"]["groupById"]["type"]["id"] == str(obj.type.id)
        if obj.parent:
            assert content["data"]["groupById"]["parent"]["id"] == str(obj.parent.id)
        else:
            assert content["data"]["groupById"]["parent"] is None
        assert len(content["data"]["groupById"]["subGroups"]) == len(obj.sub_groups.all())

    def test_retrieve_all_groups(self):
        resp = self.retrieve_all_alco_groups_query()
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "type", "parent", "subGroups"]

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"]["allGroups"][0].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert len(content["data"]["allGroups"]) == AlcoholGroup.objects.count()
