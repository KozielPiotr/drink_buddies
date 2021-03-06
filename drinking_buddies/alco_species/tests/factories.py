"""Factories for application models."""
import factory

from drinking_buddies.alco_species import models


class AlcoholTypeFactory(factory.django.DjangoModelFactory):
    """Creates new AlcoholType object."""

    class Meta:
        model = models.AlcoholType
        django_get_or_create = ("name", "description")

    name = factory.Sequence(lambda n: f"AlcoholType {n}")
    description = factory.Sequence(lambda n: f"AlcoholType description {n}")


class AlcoholGroupFactory(factory.django.DjangoModelFactory):
    """Creates new AlcoholGroup object."""

    class Meta:
        model = models.AlcoholGroup
        django_get_or_create = ("name", "type")

    name = factory.Sequence(lambda n: f"AlcoholGroup {n}")
    type = factory.SubFactory(AlcoholTypeFactory)
