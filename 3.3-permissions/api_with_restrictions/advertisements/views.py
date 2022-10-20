from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        return []

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Advertisement.objects.exclude(draft=True)
        else:
            return Advertisement.objects.filter(Q(draft=False) | Q(creator=self.request.user) & Q(draft=True))


    # @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    # def add_favorite(self, request, pk=None):
    #     favorite = Advertisement.objects.get(id=pk)
    #     validated_data =
