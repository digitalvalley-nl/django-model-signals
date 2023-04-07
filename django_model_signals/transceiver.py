from django_model_signals.signals import pre_full_clean, post_full_clean


class ModelSignalsTransceiver:

    @classmethod
    def pre_init(cls, **kwargs):
        pass

    def post_init(self, **kwargs):
        pass

    def pre_full_clean(self, **kwargs):
        pass

    def post_full_clean(self, **kwargs):
        pass

    def pre_save(self, **kwargs):
        pass

    def post_save(self, **kwargs):
        pass

    def pre_delete(self, **kwargs):
        pass

    def post_delete(self, **kwargs):
        pass

    def m2m_changed(self, **kwargs):
        pass

    def full_clean(self, *args, **kwargs):
        signal_kwargs = {
            'instance': self
        }
        if 'pre_full_clean' in self.ModelSignalsMeta.signals:
            pre_full_clean.send(sender=self.__class__, **signal_kwargs)
        result = super().full_clean(*args, **kwargs)
        signal_kwargs['result'] = result
        if 'post_full_clean' in self.ModelSignalsMeta.signals:
            post_full_clean.send(sender=self.__class__, **signal_kwargs)
        return result

    @classmethod
    def pre_bulk_save(cls, **kwargs):
      pass

    @classmethod
    def post_bulk_save(cls, **kwargs):
      pass

    class ModelSignalsMeta:
        signals = []
