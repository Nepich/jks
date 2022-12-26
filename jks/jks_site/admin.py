from django.contrib import admin
from modeltranslation.admin import TranslationStackedInline, TabbedTranslationAdmin

from .models import *


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    fields = ('about_us', 'projects', 'contacts', 'logo', 'logo_image')
    readonly_fields = ('logo_image', )


class ChoicesAdminInstanceInline(TranslationStackedInline):
    model = Choices
    extra = 0


class FooterAdmin(TabbedTranslationAdmin):
    model = Footer
    extra = 0
    inlines = [ChoicesAdminInstanceInline]


class PartnerAdminInstanceInline(admin.TabularInline):
    model = Partner
    extra = 0
    readonly_fields = ('logo_image', )


class ProjectAdminInline(TranslationStackedInline):
    model = Project
    exclude = ('id', )
    extra = 0
    readonly_fields = ('projects_foto_image', )


class MainPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )
    inlines = [PartnerAdminInstanceInline, ProjectAdminInline]


class ContentAdminInline(admin.TabularInline):
    model = Content
    extra = 0
    exclude = ('id',)
    readonly_fields = ('content_photo_image', )


class VideoProductionPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )
    inlines = [ContentAdminInline]


class PeopleAdmin(TranslationStackedInline):
    model = People
    extra = 0
    readonly_fields = ('photo_image', )


class AboutUsPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )
    inlines = [PeopleAdmin]


class ProjectsPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )
    inlines = [ProjectAdminInline]


class InfluencersMembersAdminInline(TranslationStackedInline):
    model = InfluencerMembers
    extra = 0
    readonly_fields = ('photo_image', )


class InfluncerPhotoAdminInline(TranslationStackedInline):
    model = InfluncerPhoto
    extra = 0
    readonly_fields = ('photo_image', )


class InfluencerAdmin(TabbedTranslationAdmin):
    exclude = ('id', )
    inlines = [InfluencersMembersAdminInline, InfluncerPhotoAdminInline]


class InfluencersPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )


class VoiceAdminInline(TranslationStackedInline):
    model = Voice
    exclude = ('id', )
    extra = 0
    readonly_fields = ('photo_image',)


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    exclude = ('id', )
    inlines = [VoiceAdminInline]


class DubMoviesAdminInline(TranslationStackedInline):
    model = DubMovies
    exclude = ('id', )
    extra = 0
    readonly_fields = ('photo_image',)


class DubSeriesAdminInline(TranslationStackedInline):
    model = DubSeries
    exclude = ('id', )
    extra = 0
    readonly_fields = ('photo_image',)


class DubStudioPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )
    inlines = [DubSeriesAdminInline, DubMoviesAdminInline]


class AnimationStudioPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )


class SeriesFilmsAdminInline(TranslationStackedInline):
    model = SeriesFilms
    exclude = ('id', )
    extra = 0
    readonly_fields = ('photo_image', )


class SeriesFilmsPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )
    inlines = [SeriesFilmsAdminInline]


class GameAdminInline(TranslationStackedInline):
    model = Game
    exclude = ('id', )
    extra = 0
    readonly_fields = ('photo_image', )


class GameDevPageAdmin(TabbedTranslationAdmin):
    exclude = ('id', )
    inlines = [GameAdminInline]


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'company', 'type')
    search_fields = ('name', 'phone')


admin.site.register(Footer, FooterAdmin)
admin.site.register(MainPage, MainPageAdmin)
admin.site.register(VideoProductionPage, VideoProductionPageAdmin)
admin.site.register(AboutUsPage, AboutUsPageAdmin)
admin.site.register(ProjectsPage, ProjectsPageAdmin)
admin.site.register(Influencer, InfluencerAdmin)
admin.site.register(InfluencersPage, InfluencersPageAdmin)
admin.site.register(DubStudioPage, DubStudioPageAdmin)
admin.site.register(AnimationStudioPage, AnimationStudioPageAdmin)
admin.site.register(SeriesFilmsPage, SeriesFilmsPageAdmin)
admin.site.register(GameDevPage, GameDevPageAdmin)

