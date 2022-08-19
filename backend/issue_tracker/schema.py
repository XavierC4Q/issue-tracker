import graphene
from graphene_django import DjangoObjectType
from .schemas.users import schema as user_schema
from .schemas.profiles import schema as profile_schema
from .schemas.teams import schema as team_schema


class Query(user_schema.Query, profile_schema.Query, team_schema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, profile_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, )
