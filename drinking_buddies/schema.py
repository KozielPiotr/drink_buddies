"""Schemas for all project applications."""
import graphene

from drinking_buddies.query import Query

schema = graphene.Schema(query=Query)
