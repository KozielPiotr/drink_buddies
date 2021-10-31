"""Factories for application models."""
import factory

from drinking_buddies.drinking_auth import models


class UserFactory(factory.django.DjangoModelFactory):
    """Creates new User object."""

    class Meta:
        model = models.User
        django_get_or_create = ("username", "email")

    username = factory.Sequence(lambda n: f"User {n}")
    email = factory.Faker("free_email", locale="pl_PL")
    is_staff = False
    is_superuser = False
