import graphene
from graphene_django import DjangoObjectType
from .schemas.users import schema as user_schema
from .schemas.profiles import schema as profile_schema
from .schemas.teams import schema as team_schema
from graphql_auth.schema import MeQuery, UserQuery
from graphql_auth import mutations

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()


class Query(user_schema.Query, profile_schema.Query, team_schema.Query, UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, profile_schema.Mutation, team_schema.Mutation, AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, )
