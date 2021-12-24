# pylint: disable=missing-docstring, no-member
"""Queries tests."""

import collections
import json

from drinking_buddies.alco_species.models import AlcoholGroup, AlcoholType
from drinking_buddies.alco_species.tests.mixins import GroupQueryMixin, TypeQueryMixin
from drinking_buddies.tests.utils import AuthTestCase


class TestAlcoTypeQuery(AuthTestCase, TypeQueryMixin):
    """Tests for alcohol types queries."""

    fixtures = ["species.json"]
    retrieve_query_name = "typeById"
    list_query_name = "allTypes"

    def test_retrieve_alco_type_by_id(self):
        obj = AlcoholType.objects.first()
        resp = self.retrieve_alco_type_by_id_query__auth(obj.id, self.retrieve_query_name)
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "description", "groups"]

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"]["typeById"].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert content["data"][self.retrieve_query_name]["id"] == str(obj.id)
        assert content["data"][self.retrieve_query_name]["name"] == obj.name
        assert content["data"][self.retrieve_query_name]["description"] == obj.description
        assert len(content["data"][self.retrieve_query_name]["groups"]) == len(obj.groups.all())

    def test_retrieve_alco_type_by_id__unauthenticated_user_raises_error(self):
        obj = AlcoholType.objects.first()
        resp = self.retrieve_alco_type_by_id_query__unauth(obj.id, self.retrieve_query_name)
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseHasErrors(resp)
        assert content["errors"][0]["message"] == self.AUTH_ERROR_MSG
        assert content["errors"][0]["path"][0] == self.retrieve_query_name

    def test_retrieve_all_types(self):
        resp = self.retrieve_all_alco_types_query__auth(self.list_query_name)
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "description", "groups"]
        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"][self.list_query_name][0].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert len(content["data"][self.list_query_name]) == AlcoholType.objects.count()

    def test_retrieve_all_types__unauthenticated_user_raises_error(self):
        resp = self.retrieve_all_alco_types_query__unauth(self.list_query_name)
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseHasErrors(resp)
        assert content["errors"][0]["message"] == self.AUTH_ERROR_MSG
        assert content["errors"][0]["path"][0] == self.list_query_name


class TestAlcoGroupQuery(AuthTestCase, GroupQueryMixin):
    """Tests for alcohol types queries."""

    fixtures = ["species.json"]
    retrieve_query_name = "groupById"
    list_query_name = "allGroups"

    def test_retrieve_alco_group_by_id(self):
        obj = AlcoholGroup.objects.first()
        resp = self.retrieve_alco_group_by_id_query__auth(obj.id, self.retrieve_query_name)
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "type", "parentGroup", "subGroups"]
        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"]["groupById"].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert content["data"][self.retrieve_query_name]["id"] == str(obj.id)
        assert content["data"][self.retrieve_query_name]["name"] == obj.name
        assert content["data"][self.retrieve_query_name]["type"]["id"] == str(obj.type.id)
        if obj.parent_group:
            assert content["data"][self.retrieve_query_name]["parentGroup"]["id"] == str(obj.parent_group.id)
        else:
            assert content["data"][self.retrieve_query_name]["parentGroup"] is None
        assert len(content["data"][self.retrieve_query_name]["subGroups"]) == len(obj.sub_groups.all())

    def test_retrieve_alco_group_by_id__unauthenticated_user_raises_error(self):
        obj = AlcoholGroup.objects.first()
        resp = self.retrieve_alco_group_by_id_query__unauth(obj.id, self.retrieve_query_name)
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseHasErrors(resp)
        assert content["errors"][0]["message"] == self.AUTH_ERROR_MSG
        assert content["errors"][0]["path"][0] == self.retrieve_query_name

    def test_retrieve_all_groups(self):
        resp = self.retrieve_all_alco_groups_query__auth(self.list_query_name)
        content = json.loads(resp.content)
        expected_fields = ["id", "name", "type", "parentGroup", "subGroups"]

        assert resp.status_code == 200
        self.assertResponseNoErrors(resp)
        retrieved_fields = content["data"][self.list_query_name][0].keys()
        assert collections.Counter(expected_fields) == collections.Counter(retrieved_fields)
        assert len(content["data"][self.list_query_name]) == AlcoholGroup.objects.count()

    def test_retrieve_all_groups__unauthenticated_user_raises_error(self):
        resp = self.retrieve_all_alco_groups_query__unauth(self.list_query_name)
        content = json.loads(resp.content)

        assert resp.status_code == 200
        self.assertResponseHasErrors(resp)
        assert content["errors"][0]["message"] == self.AUTH_ERROR_MSG
        assert content["errors"][0]["path"][0] == self.list_query_name
