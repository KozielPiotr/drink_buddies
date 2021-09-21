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

    def test_retrieve_all_groups(self):
        resp = self.retrieve_all_alco_groups_query()
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "type", "parent", "subGroups"]

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"]["allGroups"][0].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert len(content["data"]["allGroups"]) == AlcoholGroup.objects.count()
