import graphene
from graphene_django import DjangoObjectType
from issue_tracker.models import Team


class TeamType(DjangoObjectType):
    class Meta:
        model = Team


class Query(graphene.ObjectType):
    teams = graphene.List(TeamType)
    team_by_id = graphene.Field(TeamType, team_id=graphene.String(required=True))
    team_by_name = graphene.Field(TeamType, name=graphene.String(required=True))

    def resolve_teams(root, info):
      return Team.objects.all()

    def resolve_team_by_id(root, info, team_id):
      return Team.objects.get(team_id=team_id)

    def resolve_team_by_name(root, info, name):
      return Team.objects.get(name=name)


# class Mutation(graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query, )
