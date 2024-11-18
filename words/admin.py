from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("text", "language", "level")
    list_filter = ("language", "level")
    search_fields = ("text",)