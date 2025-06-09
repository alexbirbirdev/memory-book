# Импортируем все представления для удобного доступа
from .banner import BannerViewSet
from .news import NewsViewSet
from .article import ArticleViewSet
from .document import DocumentViewSet
from .event import EventViewSet
from .page import PageViewSet
from .user import UserViewSet
from .veteran import (
    VeteranViewSet,
    MilitaryRankViewSet,
    BranchOfServiceViewSet,
    ConflictViewSet,
    BattleViewSet,
    RewardViewSet,
    VeteranRewardViewSet
)

__all__ = [
    'BannerViewSet',
    'NewsViewSet',
    'ArticleViewSet',
    'DocumentViewSet',
    'EventViewSet',
    'PageViewSet',
    'UserViewSet',
    'VeteranViewSet',
    'MilitaryRankViewSet',
    'BranchOfServiceViewSet',
    'ConflictViewSet',
    'BattleViewSet',
    'RewardViewSet',
    'VeteranRewardViewSet'
]