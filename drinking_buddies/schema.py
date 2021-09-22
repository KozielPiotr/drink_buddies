"""Schemas for all project applications."""
import graphene

from drinking_buddies.mutations import Mutation
from drinking_buddies.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
