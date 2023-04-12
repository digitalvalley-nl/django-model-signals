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

    def post_full_clean_error(self, **kwargs):
        raise kwargs['error']

    def pre_save(self, **kwargs):
        pass

    def post_save(self, **kwargs):
        pass

    def post_save_error(self, **kwargs):
        raise kwargs['error']

    def pre_delete(self, **kwargs):
        pass

    def post_delete(self, **kwargs):
        pass

    def m2m_changed(self, **kwargs):
        pass

    def full_clean(self, *args, **kwargs):
        try:
            signal_kwargs = {
                'instance': self
            }
            if 'pre_full_clean' in self.ModelSignalsMeta.signals:
                pre_full_clean.send(sender=self.__class__, **signal_kwargs)
            super().full_clean(*args, **kwargs)
            if 'post_full_clean' in self.ModelSignalsMeta.signals:
                post_full_clean.send(sender=self.__class__, **signal_kwargs)
            return True
        except Exception as error:
            if 'post_full_clean_error' in self.ModelSignalsMeta.signals:
                return self.post_full_clean_error(
                    error=error,
                    created=self.pk is None
                )
            else:
                raise error

    def save(self, **kwargs):
        try:
            super().save()
        except Exception as error:
            if 'post_save_error' in self.ModelSignalsMeta.signals:
                self.post_save_error(
                    error=error,
                    created=self.pk is None
                )
            else:
                raise error

    @classmethod
    def pre_bulk_save(cls, **kwargs):
      pass

    @classmethod
    def post_bulk_save(cls, **kwargs):
      pass

    class ModelSignalsMeta:
        signals = []
