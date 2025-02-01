from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(FAQ, FAQAdmin)