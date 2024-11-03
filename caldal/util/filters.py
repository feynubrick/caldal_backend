from functools import wraps

from django.db.models import Q


def handle_filter_empty_value(func):
    @wraps(func)
    def wrapper(self, value, *args, **kwargs):
        if value is None:
            return Q()
        return func(self, value, *args, **kwargs)

    return wrapper
