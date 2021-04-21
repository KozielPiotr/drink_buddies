"""Queries for all project applications."""
from drinking_buddies.alco_species.query import AlcoGroupQuery, AlcoTypeQuery


class Query(AlcoGroupQuery, AlcoTypeQuery):
    """Class, that inherits from queries from all apps."""
