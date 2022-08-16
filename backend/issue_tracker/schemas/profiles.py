import graphene
from graphene_django import DjangoObjectType
from issue_tracker.models import Profile, User


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ('fullname', 'profile_id', 'title', 'user', )


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)

    def resolve_all_profiles(root, info):
        return Profile.objects.all()


class CreateProfileMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        fullname = graphene.String(required=True)
        title = graphene.String(default_value='Contractor')

    new_profile = graphene.Field(ProfileType)

    @classmethod
    def mutate(cls, root, info, email, fullname, title):
        try:
            user = User.objects.get(email=email)
            new_profile = Profile.objects.create(
                fullname=fullname, title=title, user=user)
            new_profile.save()
            return CreateProfileMutation(new_profile=new_profile)
        except:
            return None


class Mutation(graphene.ObjectType):
    create_profile = CreateProfileMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, )
