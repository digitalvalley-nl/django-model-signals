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
from django_model_signals.dispatcher import ModelSignalDispatcher
from django_model_signals.transceiver import ModelSignalTransceiver


class DjangoModelSignalsConfig(AppConfig):
    name = 'django_model_signals'

    def ready(self):
        models = apps.get_models()
        for model in models:
            if issubclass(model, ModelSignalTransceiver):
                if 'pre_init' in model.ModelSignalsMeta.signals:
                    pre_init.connect(ModelSignalDispatcher.pre_init)
                if 'post_init' in model.ModelSignalsMeta.signals:
                    post_init.connect(ModelSignalDispatcher.post_init)
                if 'pre_save' in model.ModelSignalsMeta.signals:
                    pre_save.connect(ModelSignalDispatcher.pre_save)
                if 'post_save' in model.ModelSignalsMeta.signals:
                    post_save.connect(ModelSignalDispatcher.post_save)
                if 'pre_delete' in model.ModelSignalsMeta.signals:
                    pre_delete.connect(ModelSignalDispatcher.pre_delete)
                if 'post_delete' in model.ModelSignalsMeta.signals:
                    post_delete.connect(ModelSignalDispatcher.post_delete)
                if 'm2m_changed' in model.ModelSignalsMeta.signals:
                    m2m_changed.connect(ModelSignalDispatcher.m2m_changed)
