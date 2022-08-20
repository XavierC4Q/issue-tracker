import graphene
from graphene_django import DjangoObjectType
from issue_tracker.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password', )


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    user_by_uid = graphene.Field(UserType, uid=graphene.String(required=True))

    user_by_email = graphene.Field(
        UserType, email=graphene.String(required=True))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_by_uid(root, info, uid):
        return User.objects.get(uid=uid)

    def resolve_user_by_email(root, info, email):
        return User.objects.get(email=email)


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        is_superuser = graphene.Boolean(default_value=False)

    new_user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, email, password, is_superuser):
        if is_superuser:
            new_user = User.objects.create_superuser(
                email=email, password=password)
        else:
            new_user = User.objects.create_user(email=email, password=password)

        new_user.save()
        return CreateUserMutation(new_user=new_user)


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, )
