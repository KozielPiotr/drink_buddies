"""Models for alco_species application."""
import uuid

from django.db import models


class AlcoholType(models.Model):
    """Alcohol type, for example strong alcohols."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __repr__(self):
        return f"<AlcoholType {self.name}, id={self.id}"

    def __str__(self):
        return self.name


class AlcoholGroup(models.Model):
    """Alcohol group, for example absinthe, rakia, rum. Can be also sub group of other AlcoholGroup object."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    parent = models.ForeignKey(
        "self",
        related_name="sub_groups",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    type = models.ForeignKey(
        AlcoholType,
        related_name="groups",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        if self.parent:
            return (
                f"<AlcoholGroup {self.name}, id={self.id}, parent={self.parent.name}>"
            )
        return f"<AlcoholGroup {self.name}, id={self.id}>"

    def __str__(self):
        return self.name
