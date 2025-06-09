from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from ..models import (
    Veteran,
    MilitaryRank,
    BranchOfService,
    Conflict,
    Battle,
    Reward,
    VeteranReward
)
from ..serializers import (
    VeteranSerializer,
    VeteranCreateUpdateSerializer,
    MilitaryRankSerializer,
    BranchOfServiceSerializer,
    ConflictSerializer,
    BattleSerializer,
    RewardSerializer,
    VeteranRewardSerializer
)

class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator

class VeteranViewSet(viewsets.ModelViewSet):
    queryset = Veteran.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = {
        'last_name': ['exact', 'icontains'],
        'first_name': ['exact', 'icontains'],
        'middle_name': ['exact', 'icontains'],
        'veteran_type': ['exact'],
        'military_rank__id': ['exact'],
        'branch_of_service__id': ['exact'],
        'conflict__id': ['exact'],
        'birth_date': ['gte', 'lte', 'exact'],
        'death_date': ['gte', 'lte', 'exact'],
        'is_approved': ['exact'],
    }
    search_fields = [
        'last_name',
        'first_name',
        'middle_name',
        'call_place',
        'service_place',
        'military_unit'
    ]
    ordering_fields = [
        'last_name',
        'first_name',
        'birth_date',
        'death_date',
        'created_at'
    ]
    ordering = ['last_name', 'first_name']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return VeteranCreateUpdateSerializer
        return VeteranSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'approve', 'reject']:
            permission_classes = [permissions.IsAuthenticated & (permissions.IsAdminUser | IsModerator)]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_authenticated:
            return queryset.filter(is_approved=True)
        if user.is_superuser:
            return queryset
        if user.is_moderator:
            return queryset.filter(Q(is_approved=False) | Q(created_by=user))
        return queryset.filter(Q(is_approved=True) | Q(created_by=user))

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated & (permissions.IsAdminUser | IsModerator)])
    def approve(self, request, pk=None):
        veteran = self.get_object()
        veteran.is_approved = True
        veteran.modified_by = request.user
        veteran.save()
        return Response({'status': 'approved'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated & (permissions.IsAdminUser | IsModerator)])
    def reject(self, request, pk=None):
        veteran = self.get_object()
        veteran.is_approved = False
        veteran.modified_by = request.user
        veteran.save()
        return Response({'status': 'rejected'}, status=status.HTTP_200_OK)

class MilitaryRankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MilitaryRank.objects.all()
    serializer_class = MilitaryRankSerializer

class BranchOfServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BranchOfService.objects.all()
    serializer_class = BranchOfServiceSerializer

class ConflictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conflict.objects.all()
    serializer_class = ConflictSerializer

class BattleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer

class RewardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

class VeteranRewardViewSet(viewsets.ModelViewSet):
    queryset = VeteranReward.objects.all()
    serializer_class = VeteranRewardSerializer
    permission_classes = [permissions.IsAuthenticated & (permissions.IsAdminUser | IsModerator)]