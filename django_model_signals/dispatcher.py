# Python standard library
from functools import partial

# Django Model Signals
from django_model_signals.transceiver import ModelSignalsTransceiver


class ModelSignalsDispatcher:

    @staticmethod
    def signal_method(signal_name, sender, **kwargs):
        if 'instance' in kwargs \
            and isinstance(kwargs['instance'], ModelSignalsTransceiver):
            getattr(kwargs['instance'], signal_name)(**kwargs)
        elif issubclass(sender, ModelSignalsTransceiver):
            getattr(sender, signal_name)(**kwargs)

    @classmethod
    def get_signal_method(cls, name):
        return partial(cls.signal_method, signal_name=name)
