from django_model_signals.signals import pre_full_clean, post_full_clean


class FullCleanSignalsMixin:

    def full_clean(self, *args, **kwargs):
        try:
            signal_kwargs = {
                'instance': self,
                'created': self._state.adding == True
            }
            if 'pre_full_clean' in self.ModelSignalsMeta.signals:
                pre_full_clean.send(sender=self.__class__, **signal_kwargs)
            result = super().full_clean(*args, **kwargs)
            signal_kwargs['result'] = result
            if 'post_full_clean' in self.ModelSignalsMeta.signals:
                post_full_clean.send(sender=self.__class__, **signal_kwargs)
            return result
        except Exception as error:
            if 'post_full_clean_error' in self.ModelSignalsMeta.signals:
                signal_kwargs['error'] = error
                return self.post_full_clean_error(**signal_kwargs)
            else:
                raise error


class PostSaveErrorSignalMixin:
    def save(self, **kwargs):
        try:
            return super().save()
        except Exception as error:
            if 'post_save_error' in self.ModelSignalsMeta.signals:
                return self.post_save_error(
                    error=error,
                    created=self._state.adding == True
                )
            else:
                raise error
