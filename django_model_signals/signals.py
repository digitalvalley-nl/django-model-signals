# Django
from django.db.models.signals import (
    pre_init,
    post_init,
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed
)
from django.dispatch import Signal


pre_bulk_save = Signal()
post_bulk_save = Signal()
pre_full_clean = Signal()
post_full_clean = Signal()


MODEL_SIGNALS = {
    'pre_init': pre_init,
    'post_init': post_init,
    'pre_full_clean': pre_full_clean,
    'post_full_clean': post_full_clean,
    'pre_save': pre_save,
    'post_save': post_save,
    'pre_delete': pre_delete,
    'post_delete': post_delete,
    'm2m_changed': m2m_changed,
    'pre_bulk_save': pre_bulk_save,
    'post_bulk_save': post_bulk_save
}
