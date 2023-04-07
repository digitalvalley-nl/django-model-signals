# Django Model Signals

Django Model Signals makes it easier to keep business logic in your Django
models by allowing them to become transceivers of their own signals, including
bulk signals.

## Installation

```
pip install django-model-signals
```

## Configuration

Add the `django_model_signals` app to your `INSTALLED_APPS`:
```
INSTALLED_APPS = [
    # ...
    'django_model_signals',
]
```

## Usage

- Add the `ModelSignalsTransceiver` class to your Django model.
- Add a `ModelSignalsMeta` inner class to your Django model and specify which
signals you're interested in.
- Add the `ModelSignalsManager` to your Django model's `objects` property to
enable bulk signals.
- Implement the signal receiver methods in your Django model.


## Example
```python
from django.db.models import Model
from django_model_signals.manager import ModelSignalsManager
from django_model_signals.transceiver import ModelSignalsTransceiver

class MyModel(
    ModelSignalsTransceiver,
    Model
):

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

    @classmethod
    def pre_bulk_save(cls, **kwargs):
      pass

    @classmethod
    def post_bulk_save(cls, **kwargs):
      pass

    objects = ModelSignalsManager()

    class ModelSignalsMeta:
        signals = [
            'pre_init',
            'post_init',
            'pre_full_clean',
            'post_full_clean',
            'pre_save',
            'post_save',
            'pre_delete',
            'post_delete',
            'm2m_changed',
            'pre_bulk_save',
            'post_bulk_save'
        ]
```

## Notes

- The following actions are supported for triggering the implemented signals:
  - Creating or loading an model instance from the database will trigger the `pre_init` and `post_init` signals.
  - Calling `Model.full_clean` will trigger the `pre_full_clean` and `post_full_clean` signals.
  - Calling `Model.save` will trigger the `pre_save` and `post_save` signals.
  - Calling `Model.delete` will trigger the `pre_delete` and `post_delete` signals.
  - Calling `Model.objects.create` will trigger the `pre_save` and `post_save` signals.
  - Calling `Model.objects.get_or_create` will trigger the `pre_save` and `post_save` signals.
  - Calling `Model.objects.update_or_create` will trigger the `pre_save` and `post_save` signals.
  - Calling `Model.objects.bulk_create` will trigger the `pre_bulk_save` and `post_bulk_save` signals.
  - Calling `Model.objects.bulk_update` will trigger the `pre_bulk_save` and `post_bulk_save` signals.
  - Calling `QuerySet.delete` will trigger the `pre_delete` and `post_delete` signals.

- To implement the `pre_full_clean` and `post_full_clean` signals, this library
  overrides the `full_clean` method of Django models and calls the original
  method in a backwards compatible way. However, make sure the order of the
  classes inherited from is the same as the above example to ensure the proper
  method resolution order.

## Resources

- Django: https://www.djangoproject.com/
