# Python Standard Library
import sys

# Django
from django.apps import apps, AppConfig
from django.db.models.signals import (
    pre_init,
    post_init,
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed
)

# Django Model Signals
from django_model_signals.dispatcher import ModelSignalsDispatcher
from django_model_signals.signals import pre_bulk_save, post_bulk_save
from django_model_signals.transceiver import ModelSignalsTransceiver


class DjangoModelSignalsConfig(AppConfig):
    name = 'django_model_signals'

    def ready(self):

        # Don't bind signals when applying migrations
        if 'manage.py' in sys.argv and 'migrate' in sys.argv:
            return

        models = apps.get_models()
        for model in models:
            if issubclass(model, ModelSignalsTransceiver):
                if 'pre_init' in model.ModelSignalsMeta.signals:
                    pre_init.connect(ModelSignalsDispatcher.pre_init)
                if 'post_init' in model.ModelSignalsMeta.signals:
                    post_init.connect(ModelSignalsDispatcher.post_init)
                if 'pre_save' in model.ModelSignalsMeta.signals:
                    pre_save.connect(ModelSignalsDispatcher.pre_save)
                if 'post_save' in model.ModelSignalsMeta.signals:
                    post_save.connect(ModelSignalsDispatcher.post_save)
                if 'pre_delete' in model.ModelSignalsMeta.signals:
                    pre_delete.connect(ModelSignalsDispatcher.pre_delete)
                if 'post_delete' in model.ModelSignalsMeta.signals:
                    post_delete.connect(ModelSignalsDispatcher.post_delete)
                if 'm2m_changed' in model.ModelSignalsMeta.signals:
                    m2m_changed.connect(ModelSignalsDispatcher.m2m_changed)
                if 'pre_bulk_save' in model.ModelSignalsMeta.signals:
                    pre_bulk_save.connect(ModelSignalsDispatcher.pre_bulk_save)
                if 'post_bulk_save' in model.ModelSignalsMeta.signals:
                    post_bulk_save.connect(
                        ModelSignalsDispatcher.post_bulk_save)
