"""Queries for all project applications."""
from drinking_buddies.alco_species.query import AlcoGroupQuery, AlcoTypeQuery
from drinking_buddies.drinking_auth.query import UserQuery


class Query(AlcoGroupQuery, AlcoTypeQuery, UserQuery):
    """Class, that inherits from queries from all apps."""
