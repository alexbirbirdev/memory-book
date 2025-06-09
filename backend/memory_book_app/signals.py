from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.db import connection
from .models import LogEntry

User = get_user_model()


def table_exists(table_name):
    return table_name in connection.introspection.table_names()


@receiver(post_save)
def log_object_creation_or_update(sender, instance, created, **kwargs):
    if sender.__name__ == 'LogEntry' or isinstance(instance, (User, Session)):
        return

    if not table_exists('memory_book_app_logentry'):
        return

    action = 'create' if created else 'update'
    LogEntry.objects.create(
        model=sender.__name__,
        object_id=getattr(instance, 'id', None),
        action=action,
        details=f"{sender.__name__} was {action}d"
    )


@receiver(post_delete)
def log_object_deletion(sender, instance, **kwargs):
    if sender.__name__ == 'LogEntry' or isinstance(instance, (User, Session)):
        return

    if not table_exists('memory_book_app_logentry'):
        return

    LogEntry.objects.create(
        model=sender.__name__,
        object_id=getattr(instance, 'id', None),
        action='delete',
        details=f"{sender.__name__} was deleted"
    )
