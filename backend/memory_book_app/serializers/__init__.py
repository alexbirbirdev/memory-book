# Импортируем все сериализаторы для удобного доступа
from .veteran import (
    VeteranSerializer,
    VeteranCreateUpdateSerializer,
    VeteranRewardSerializer,
    MilitaryRankSerializer,
    BranchOfServiceSerializer,
    ConflictSerializer,
    BattleSerializer,
    RewardSerializer
)
from .banner import BannerSerializer
from .news import NewsSerializer
from .article import ArticleSerializer
from .document import DocumentSerializer
from .event import EventSerializer
from .page import PageSerializer
from .user import UserSerializer

__all__ = [
    'VeteranSerializer',
    'VeteranCreateUpdateSerializer',
    'VeteranRewardSerializer',
    'MilitaryRankSerializer',
    'BranchOfServiceSerializer',
    'ConflictSerializer',
    'BattleSerializer',
    'RewardSerializer',
    'BannerSerializer',
    'NewsSerializer',
    'ArticleSerializer',
    'DocumentSerializer',
    'EventSerializer',
    'PageSerializer',
    'UserSerializer'
]