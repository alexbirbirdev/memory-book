from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VeteranViewSet,
    MilitaryRankViewSet,
    BranchOfServiceViewSet,
    ConflictViewSet,
    BattleViewSet,
    RewardViewSet,
    VeteranRewardViewSet,
    BannerViewSet,
    NewsViewSet,
    ArticleViewSet,
    DocumentViewSet,
    EventViewSet,
    PageViewSet,
    UserViewSet
)

router = DefaultRouter()
router.register(r'veterans', VeteranViewSet)
router.register(r'military-ranks', MilitaryRankViewSet)
router.register(r'branches-of-service', BranchOfServiceViewSet)
router.register(r'conflicts', ConflictViewSet)
router.register(r'battles', BattleViewSet)
router.register(r'rewards', RewardViewSet)
router.register(r'veteran-rewards', VeteranRewardViewSet)
router.register(r'banners', BannerViewSet)
router.register(r'news', NewsViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'events', EventViewSet)
router.register(r'pages', PageViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]