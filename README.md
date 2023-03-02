# Django Model Signals

Django Model Signals makes it easier to keep model related business logic in
your Django models by allowing them to become transceivers of their own
signals.

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

- Add the `ModelSignalTransceiver` class to your Django model.
- Add a `ModelSignalsMeta` inner class to your Django model and specify which
signals you're interested in.
- Implement the signal receiver methods in your Django model.

## Example
```python
from django.db.models import Model
from django_model_signals import ModelSignalTransceiver

class MyModel(
    ModelSignalTransceiver,
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

    class ModelSignalsMeta:
        signals = [
            'pre_init',
            'post_init',
            'pre_save',
            'post_save',
            'pre_delete',
            'post_delete',
            'm2m_changed'
        ]
```

## Resources

- Django: https://www.djangoproject.com/
