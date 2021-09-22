# pylint: disable=too-few-public-methods
"""Mutations for all project applications."""
from drinking_buddies.drinking_auth.mutations import AuthMutation


class Mutation(AuthMutation):
    """Class, that inherits from mutations from all apps."""
