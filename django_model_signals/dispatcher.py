# Python standard library
from functools import partial


class ModelSignalsDispatcher:

    @staticmethod
    def signal_method(signal_name, sender, **kwargs):
        if 'instance' in kwargs \
            and hasattr(kwargs['instance'], 'ModelSignalsMeta') \
            and signal_name in kwargs['instance'].ModelSignalsMeta.signals:
                getattr(kwargs['instance'], signal_name)(**kwargs)
        elif hasattr(sender, 'ModelSignalsMeta') \
            and signal_name in sender.ModelSignalsMeta.signals:
            getattr(sender, signal_name)(**kwargs)

    @classmethod
    def get_signal_method(cls, name):
        return partial(cls.signal_method, signal_name=name)
