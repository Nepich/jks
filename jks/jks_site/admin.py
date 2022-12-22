from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    fields = ('about_us', 'projects', 'contacts', 'logo')


@admin.register(ProjectsPage)
class ProjectsPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Choices)
class ChoicesAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(VideoProductionPage)
class VideoProductionPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(InfluencersPage)
class InfluencersPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Influencer)
class InfluencerAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(InfluencerMembers)
class InfluencersPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(InfluncerPhoto)
class InfluncerPhotoAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(DubStudioPage)
class DubStudioPagePhotoAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(DubMovies)
class DubMoviesAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(DubSeries)
class DubSeriesAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Voice)
class VoiceAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(AnimationStudioPage)
class AnimationStudioPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(SeriesFilms)
class SeriesFilmsAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(SeriesFilmsPage)
class SeriesFilmsPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(GameDevPage)
class GameDevPageAdmin(admin.ModelAdmin):
    exclude = ('id', )


admin.site.register(Form)
admin.site.register(Manager)

