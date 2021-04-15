# pylint: disable=missing-docstring, no-self-use, too-few-public-methods
"""Tests for proper model work."""

import pytest

from drinking_buddies.alco_species.models import AlcoholGroup, AlcoholType
from drinking_buddies.alco_species.tests.factories import (
    AlcoholGroupFactory,
    AlcoholTypeFactory,
)


class TestAlcoholType:
    """AlcoholType model tests."""

    @pytest.mark.django_db
    def test_create_type(self):
        alco_type = AlcoholTypeFactory()

        assert len(AlcoholType.objects.all()) == 1
        new_type = AlcoholType.objects.first()
        assert new_type.name == alco_type.name
        assert new_type.description == alco_type.description
        assert len(new_type.groups.all()) == 0


class TestAlcoholGroup:
    """AlcoholGroup model tests."""

    @pytest.mark.django_db
    def test_create_group(self):
        group = AlcoholGroupFactory()

        assert len(AlcoholGroup.objects.all()) == 1
        new_group = AlcoholGroup.objects.first()
        assert new_group.parent is None
        assert new_group.name == group.name
        assert new_group.type is not None
        assert len(new_group.sub_groups.all()) == 0

    @pytest.mark.django_db
    def test_group_with_subgroup(self):
        sub_group = AlcoholGroupFactory()
        sub_group.parent = AlcoholGroupFactory()
        sub_group.save()

        parent = sub_group.parent

        assert len(AlcoholGroup.objects.all()) == 2
        sub = AlcoholGroup.objects.get(id=sub_group.id)
        assert sub.parent.id == parent.id

    @pytest.mark.django_db
    def test_group_repr_with_parent(self):
        sub_group = AlcoholGroupFactory()
        sub_group.parent = AlcoholGroupFactory()
        sub_group.save()

        assert (
            repr(sub_group)
            == f"<AlcoholGroup {sub_group.name}, id={sub_group.id}, parent={sub_group.parent.name}>"
        )

    @pytest.mark.django_db
    def test_group_repr_no_parent(self):
        group = AlcoholGroupFactory()

        assert repr(group) == f"<AlcoholGroup {group.name}, id={group.id}>"
