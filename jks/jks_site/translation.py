from modeltranslation.translator import translator, TranslationOptions
from .models import *


class HeaderTranslationOptions(TranslationOptions):
    fields = ('about_us', 'projects', 'contacts')


class FooterTranslationOptions(TranslationOptions):
    fields = ('text_us', 'interests', 'about_u', 'company_name',
              'company_description', 'contact_info', 'services', 'about_us')


class ChoicesTranslationOptions(TranslationOptions):
    fields = ('type', )


class MainPageTranslationOptions(TranslationOptions):
    fields = ('who_are_we', 'who_are_we_desc', 'learn_more', 'projects',
              'statistics', 'influencers', 'subscribers', 'likes',
              'views', 'partners')


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class VideoProductionPageTranslationOptions(TranslationOptions):
    fields = ('title', 'what_we_filming', 'first_product', 'first_product_desc',
              'second_product', 'second_product_desc', 'third_product', 'third_product_desc',
              'fourth_product', 'fourth_product_desc', 'offer')


class AboutUsPageTranslationOptions(TranslationOptions):
    fields = ('title', 'first_text', 'second_text', 'third_text',
              'fourth_text', 'fifth_text', 'sixth_text', 'seventh_text', 'eighth_text')


class PeopleTranslationOptions(TranslationOptions):
    fields = ('name', 'position')


class ProjectsPageTranslationOptions(TranslationOptions):
    fields = ('title', )


class InfluencersPageTranslationOptions(TranslationOptions):
    fields = ('title', 'first_text', 'second_text', 'third_text')


class InfluencerTranslationOptions(TranslationOptions):
    fields = ('name', 'statistics', 'instagram_statistics', 'tiktok_statistics',
              'youtube_statistics', 'description')


class InfluncerPhotoTranslationOptions(TranslationOptions):
    fields = ('description', )


class InfluencerMembersTranslationOptions(TranslationOptions):
    fields = ('name', 'instagram_statistics', 'tiktok_statistics', 'youtube_statistics')


class DubStudioPageTranslationOptions(TranslationOptions):
    fields = ('first_text', 'first_text_desc', 'second_text', 'second_text_desc',
              'third_text', 'third_text_desc', 'projects')


class DubMoviesTranslationOptions(TranslationOptions):
    fields = ('name', 'dub_language', 'translated_by', 'button', 'duration')


class DubSeriesTranslationOptions(TranslationOptions):
    fields = ('name', 'dub_language', 'translated_by', 'button', 'total_series', 'dub_series')


class VoiceTranslationOptions(TranslationOptions):
    fields = ('name', )


class AnimationStudioPageTranslationOptions(TranslationOptions):
    fields = ('title', 'field')


class SeriesFilmsPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'projects')


class SeriesFilmsTranslationOptions(TranslationOptions):
    fields = ('name', 'age', 'series_number', 'language', 'genre', 'button')


class GameDevPageTranslationOptions(TranslationOptions):
    fields = ('title', 'first_text', 'first_text_desc', 'second_text', 'second_text_desc')


class GameTranslationOptions(TranslationOptions):
    fields = ('statistics', 'ios', 'android', 'title')


translator.register(Header, HeaderTranslationOptions)
translator.register(Footer, FooterTranslationOptions)
translator.register(Choices, ChoicesTranslationOptions)
translator.register(MainPage, MainPageTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(VideoProductionPage, VideoProductionPageTranslationOptions)
translator.register(AboutUsPage, AboutUsPageTranslationOptions)
translator.register(People, PeopleTranslationOptions)
translator.register(ProjectsPage, ProjectsPageTranslationOptions)
translator.register(InfluencersPage, InfluencersPageTranslationOptions)
translator.register(Influencer, InfluencerTranslationOptions)
translator.register(InfluncerPhoto, InfluncerPhotoTranslationOptions)
translator.register(InfluencerMembers, InfluencerMembersTranslationOptions)
translator.register(DubStudioPage, DubStudioPageTranslationOptions)
translator.register(DubMovies, DubMoviesTranslationOptions)
translator.register(DubSeries, DubSeriesTranslationOptions)
translator.register(Voice, VoiceTranslationOptions)
translator.register(AnimationStudioPage, AnimationStudioPageTranslationOptions)
translator.register(SeriesFilmsPage, SeriesFilmsPageTranslationOptions)
translator.register(SeriesFilms, SeriesFilmsTranslationOptions)
translator.register(GameDevPage, GameDevPageTranslationOptions)
translator.register(Game, GameTranslationOptions)
