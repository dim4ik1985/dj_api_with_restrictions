from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


# class FavoriteAdvertisementSerializer(serializers.Serializer):
#     class Meta:
#         model = FavoriteAdvertisement
#         fields = ['user', 'favorite']


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )
    # favorites = FavoriteAdvertisementSerializer(many=True)

    class Meta:
        model = Advertisement
        fields = '__all__'

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        fields = '__all__'
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        if Advertisement.objects.filter(creator=self.context["request"].user).filter(status='OPEN').count() >= 3 \
            and not data.get("status") == 'CLOSED':
            raise ValidationError('Превышен лимит открытых объявлений!')

        return data
