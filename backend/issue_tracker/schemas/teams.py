import graphene
from graphene_django import DjangoObjectType
from issue_tracker.models import Team, Profile


class TeamType(DjangoObjectType):
    class Meta:
        model = Team


class Query(graphene.ObjectType):
    teams = graphene.List(TeamType)

    team_by_id = graphene.Field(
        TeamType, team_id=graphene.String(required=True))

    team_by_name = graphene.Field(
        TeamType, name=graphene.String(required=True))

    teams_for_profile = graphene.List(
        TeamType, profile_id=graphene.String(required=True))

    def resolve_teams(root, info):
        return Team.objects.all()

    def resolve_team_by_id(root, info, team_id):
        return Team.objects.get(team_id=team_id)

    def resolve_team_by_name(root, info, name):
        return Team.objects.get(name=name)

    def resolve_teams_for_profile(root, info, profile_id):
        return Team.objects.filter(profiles__profile_id=profile_id)


class CreateTeamMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    new_team = graphene.Field(TeamType)

    @classmethod
    def mutate(cls, root, info, name, description):
        new_team = Team.objects.create(name=name, description=description)
        new_team.save()
        return CreateTeamMutation(new_team=new_team)


class AddProfileMutation(graphene.Mutation):
    class Arguments:
        profile_id = graphene.String(required=True)
        team_id = graphene.String(required=True)

    team = graphene.Field(TeamType)

    @classmethod
    def mutate(cls, root, info, profile_id, team_id):
        profile = Profile.objects.get(profile_id=profile_id)
        team = Team.objects.get(team_id=team_id)
        team.profiles.add(profile)
        team.save()

        return AddProfileMutation(team=team)


class Mutation(graphene.ObjectType):
    create_team = CreateTeamMutation.Field()
    add_profile_to_team = AddProfileMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, )
