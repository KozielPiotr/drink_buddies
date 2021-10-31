"""Decorators used across the project."""
from graphql_jwt.decorators import user_passes_test

login_forbidden = user_passes_test(lambda u: u.is_authenticated is False)
