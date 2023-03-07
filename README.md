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
receive bulk signals.
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

    def pre_init(self, **kwargs):
        pass

    def post_init(self, **kwargs):
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
            'pre_save',
            'post_save',
            'pre_delete',
            'post_delete',
            'm2m_changed',
            'pre_bulk_save',
            'post_bulk_save'
        ]
```

## Resources

- Django: https://www.djangoproject.com/
