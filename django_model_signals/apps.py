# Python Standard Library
import sys

# Django
from django.apps import apps, AppConfig

# Django Model Signals
from django_model_signals.dispatcher import ModelSignalsDispatcher
from django_model_signals.signals import MODEL_SIGNALS
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
                for signal_name, signal in MODEL_SIGNALS.items():
                    if signal_name in model.ModelSignalsMeta.signals:
                        signal.connect(
                            ModelSignalsDispatcher.get_signal_method(
                                signal_name
                            )
                        )
