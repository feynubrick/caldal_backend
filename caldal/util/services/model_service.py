from abc import ABC
from typing import Generic, Type, TypeVar

from django.db.models import Model, QuerySet

T = TypeVar("T", bound=Model)


class ModelService(Generic[T], ABC):
    _model: Type[T]

    def get_queryset(self):
        return self._model.objects.all()

    def exists(self, **kwargs) -> bool:
        return self.get_queryset().filter(**kwargs).exists()

    def create(self, **kwargs):
        self._validate_create(**kwargs)
        return self.get_queryset().create(**kwargs)

    def get(self, **kwargs):
        return self.get_queryset().get(**kwargs)

    def update(self, instance_id: int, **kwargs):
        self._validate_update(**kwargs)
        return self.get_queryset().filter(id=instance_id).update(**kwargs)

    def delete(self, instance_id: int):
        return self.get_queryset().filter(id=instance_id).delete()

    def _validate_create(self, **kwargs):
        return

    def _validate_update(self, **kwargs):
        return
