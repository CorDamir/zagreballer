from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget
from . import models


@admin.register(models.FutsalField)
class FutsalFieldAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(models.FutsalGame)
