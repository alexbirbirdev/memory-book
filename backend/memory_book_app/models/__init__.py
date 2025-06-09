# Импортируем все модели для удобного доступа
from .user import User
from .veteran import (
    Veteran,
    MilitaryRank,
    BranchOfService,
    Conflict,
    Battle,
    Reward,
    VeteranReward
)
from .log import LogEntry
from .article import Article
from .banner import Banner
from .document import Document
from .event import Event
from .news import News
from .page import Page

__all__ = [
    'User',
    'Veteran',
    'MilitaryRank',
    'BranchOfService',
    'Conflict',
    'Battle',
    'Reward',
    'VeteranReward',
    'LogEntry',
    'Article',
    'Banner',
    'Document',
    'Event',
    'News',
    'Page'
]