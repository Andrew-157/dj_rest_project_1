from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,\
    UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    print('serializer')

    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id', 'username', 'email', 'user_image', 'password'
        ]


class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = [
            'id', 'username', 'email', 'user_image',
        ]
