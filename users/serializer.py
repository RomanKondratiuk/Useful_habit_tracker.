from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            # username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            city=validated_data.get('city'),
            avatar=validated_data.get('avatar'),
            telegram_chat_id=validated_data.get('telegram_chat_id'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
