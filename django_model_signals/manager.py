# Django
from django.db.models.manager import Manager

# Django Model Signals
from django_model_signals.signals import pre_bulk_save, post_bulk_save


class ModelSignalsManager(Manager):

    def bulk_create(
        self,
        objs,
        batch_size=None,
        ignore_conflicts=False,
        update_conflicts=False,
        update_fields=None,
        unique_fields=None
    ):
        pre_bulk_save.send(
            sender=self.get_queryset().model,
            objs=objs,
            created=True,
            batch_size=batch_size,
            ignore_conflicts=ignore_conflicts,
            update_conflicts=update_conflicts,
            update_fields=update_fields,
            unique_fields=unique_fields
        )
        result = super().bulk_create(
            objs,
            batch_size,
            ignore_conflicts,
            update_conflicts,
            update_fields,
            unique_fields
        )
        post_bulk_save.send(
            sender=self.get_queryset().model,
            objs=objs,
            created=True,
            batch_size=batch_size,
            ignore_conflicts=ignore_conflicts,
            update_conflicts=update_conflicts,
            update_fields=update_fields,
            unique_fields=unique_fields,
            result=result
        )
        return result

    def bulk_update(self, objs, fields, batch_size=None):
        pre_bulk_save.send(
            sender=self.get_queryset().model,
            objs=objs,
            fields=fields,
            created=False,
            batch_size=batch_size
        )
        result = super().bulk_update(objs, fields, batch_size)
        post_bulk_save.send(
            sender=self.get_queryset().model,
            objs=objs,
            fields=fields,
            created=False,
            batch_size=batch_size,
            result=result
        )
        return result
