import graphene
from graphene_django import DjangoObjectType
from issue_tracker.models import Profile, User


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ('fullname', 'profile_id', 'title', 'user', )


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)
    profile = graphene.Field(
        ProfileType, profile_id=graphene.String(required=True))

    def resolve_all_profiles(root, info):
        return Profile.objects.all()

    def resolve_profile(root, info, profile_id):
        return Profile.objects.get(profile_id=profile_id)


class CreateProfileMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        fullname = graphene.String(required=True)
        title = graphene.String(default_value='Contractor')

    new_profile = graphene.Field(ProfileType)

    @classmethod
    def mutate(cls, root, info, email, fullname, title):
        user = User.objects.get(email=email)
        new_profile = Profile.objects.create(
            fullname=fullname, title=title, user=user)
        new_profile.save()
        return CreateProfileMutation(new_profile=new_profile)


class EditProfileMutation(graphene.Mutation):
    class Arguments:
        profile_id = graphene.String(required=True)
        fullname = graphene.String()
        title = graphene.String()

    profile = graphene.Field(ProfileType)

    @classmethod
    def mutate(cls, root, info, profile_id, fullname, title):
        profile = Profile.objects.get(profile_id=profile_id)

        if title:
            profile.title = title
        if fullname:
            profile.fullname = fullname

        profile.save()
        return EditProfileMutation(profile=profile)


class Mutation(graphene.ObjectType):
    create_profile = CreateProfileMutation.Field()
    edit_profile = EditProfileMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, )
