from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import *

from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """Администрирования категории"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    """Коментарии для фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShotInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120">')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    """Жанры"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    """Администрирование фильмов"""
    list_display = ('id', 'title', 'category', 'url', 'draft')
    list_display_links = ('title',)
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [MovieShotInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ["publish", "unpublish"]
    form = MovieAdminForm
    # fields = (('actors','directors', 'genres'),)
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
        }),
        (None, {
            "fields": (("year", "world_premier", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (('actors', 'directors', 'genres', "category"),)
        }),
        (None, {
            "fields": (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        (None, {
            "fields": (('url', 'draft'),)
        })
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="120">')

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись было обнавлена"
        else:
            message_bit = f"{row_update} записей были обнавлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись было обнавлена"
        else:
            message_bit = f"{row_update} записей были обнавлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ("change",)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ("change",)

    get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Администрирование отзывов"""
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


@admin.register(MovieShots)
class MovieShotsAdmin(TranslationAdmin):
    """Администрирование кадров из фильма"""
    list_display = ("id", "title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"


@admin.register(Actor)
class ActorAdmin(TranslationAdmin):
    """Администрирование модели актеров"""
    list_display = ("id", "name", "age", "description", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    """Администрирование рейтингов"""
    list_display = ("ip", "star", "movie")


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ("value", )


admin.site.site_title = "Django Admin Nurbek"
admin.site.site_header = "Django Admin Nurbek"