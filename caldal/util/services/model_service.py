from abc import ABC
from typing import Generic, List, Type, TypeVar

from django.db.models import Model, QuerySet

T = TypeVar("T", bound=Model)


class ModelService(Generic[T], ABC):
    _model: Type[T]

    def __init__(self, instance: T | None = None) -> None:
        self._instance = instance

    def get_queryset(self):
        return self._model.objects.all()

    def exists(self, **kwargs) -> bool:
        return self.get_queryset().filter(**kwargs).exists()

    def create(self, **kwargs):
        self._validate_create(**kwargs)
        return self.get_queryset().create(**kwargs)

    def bulk_create(self, objs: List[T], **kwargs):
        self._validate_bulk_create(objs, **kwargs)
        kwargs.setdefault("batch_size", 1000)
        return self.get_queryset().bulk_create(
            objs=objs,
            **kwargs,
        )

    def get(self, **kwargs):
        return self.get_queryset().get(**kwargs)

    def update(self, **kwargs):
        self._validate_update(**kwargs)
        self.get_queryset().filter(id=self._instance.id).update(**kwargs)
        self._instance.refresh_from_db()
        return self._instance

    def delete(self):
        self._validate_delete()
        return self.get_queryset().filter(id=self._instance.id).delete()

    def _validate_create(self, **kwargs):
        return

    def _validate_update(self, **kwargs):
        assert self._instance is not None
        return

    def _validate_delete(self, **kwargs):
        assert self._instance is not None
        return

    def _validate_bulk_create(self, objs: List[T], **kwargs):
        return
