from abc import ABC

from django.apps import apps
from rest_framework import serializers


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Header')
        fields = ('about_us', 'projects', 'contacts', 'logo')


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Choices')
        fields = ('id', 'type')


class FooterSerializer(serializers.ModelSerializer):
    footer_choices = ChoicesSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Footer')
        fields = ('text_us', 'interests', 'about_u', 'company_name', 'company_description',
                  'tiktok_url', 'instagram_url', 'mail_field', 'contact_info', 'services',
                  'about_us', 'phone', 'footer_choices')


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Form')
        exclude = ('id', )


class ProjectMainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Project')
        fields = ('name', 'projects_foto')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Partner')
        fields = ('partner_logo', )


class BasePageSerializer(serializers.Serializer):
    header = HeaderSerializer(many=False, read_only=True)
    footer = FooterSerializer(many=False, read_only=True)


class MainPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    main_page_projects = ProjectMainPageSerializer(many=True, read_only=True)
    main_page_partners = PartnerSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='MainPage')
        fields = ('header', 'main_photo', 'main_video', 'who_are_we', 'who_are_we_desc', 'learn_more',
                  'projects', 'statistics', 'influencers', 'influencers_info', 'subscribers',
                  'subscribers_info', 'likes', 'likes_info', 'views', 'views_info', 'partners',
                  'main_page_projects', 'main_page_partners', 'footer')


class VideoProductionPageContentSerializer(serializers.ModelSerializer):
    fields_to_be_removed = ['content_video']

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Content')
        exclude = ('id', 'page')

    def to_representation(self, instance):
        rep = super(VideoProductionPageContentSerializer, self).to_representation(instance)
        for field in self.fields_to_be_removed:
            if not rep[field]:
                rep.pop(field)
        return rep


class VideoProductionPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    page_content = VideoProductionPageContentSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='VideoProductionPage')
        fields = ('header', 'title', 'what_we_filming', 'page_content', 'first_product', 'first_product_desc',
                  'second_product', 'second_product_desc', 'third_product', 'third_product_desc', 'fourth_product',
                  'fourth_product_desc', 'offer', 'footer')


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='People')
        fields = ('name', 'position', 'photo')


class AboutUsPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    about_us_people = PeopleSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='AboutUsPage')
        fields = ('header', 'title', 'about_us_people', 'first_text', 'second_text', 'third_text', 'fourth_text',
                  'fifth_text', 'sixth_text', 'seventh_text', 'eighth_text', 'photo_background1', 'photo_background2',
                  'photo_background3', 'photo_background4', 'photo_background5', 'photo_background6', 'footer')


class ProjectProjectsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Project')
        fields = ('name', 'description', 'projects_foto', 'projects_video')


class ProjectsPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    project_page_projects = ProjectProjectsPageSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='ProjectsPage')
        fields = ('header', 'title', 'project_page_projects', 'footer')


class InfluncerPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='InfluncerPhoto')
        fields = ('photo', 'description')


class InfluencerMembersSerializer(serializers.ModelSerializer):
    fields_to_be_removed = ('instagram_statistics', 'instagram', 'tiktok_statistics',
                            'tiktok', 'youtube_statistics', 'youtube')

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='InfluencerMembers')
        fields = ('name', 'instagram_statistics', 'instagram', 'tiktok_statistics', 'tiktok', 'youtube_statistics',
                  'youtube', 'photo')

    def to_representation(self, instance):
        rep = super(InfluencerMembersSerializer, self).to_representation(instance)
        for field in self.fields_to_be_removed:
            if not rep[field]:
                rep.pop(field)
        return rep


class InfluencerDetailSerializer(BasePageSerializer, serializers.ModelSerializer):
    influencer_photo = InfluncerPhotoSerializer(many=True, read_only=True)
    influencer_member = InfluencerMembersSerializer(many=True, read_only=True)
    fields_to_be_removed = ('influencer_photo', 'influencer_member', 'instagram_statistics', 'instagram',
                            'tiktok_statistics', 'tiktok', 'youtube_statistics', 'youtube')

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Influencer')
        fields = ('header', 'logo', 'name', 'statistics', 'instagram_statistics', 'instagram', 'tiktok_statistics',
                  'tiktok', 'youtube_statistics', 'youtube', 'description', 'influencer_photo', 'influencer_member',
                  'footer')

    def to_representation(self, instance):
        rep = super(InfluencerDetailSerializer, self).to_representation(instance)
        for field in self.fields_to_be_removed:
            if not rep[field]:
                rep.pop(field)
        return rep


class InfluencerSerializer(serializers.ModelSerializer):
    fields_to_be_removed = ('instagram_statistics', 'instagram', 'tiktok_statistics',
                            'tiktok', 'youtube_statistics', 'youtube')

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Influencer')
        fields = ('id', 'name', 'instagram_statistics', 'instagram', 'tiktok_statistics', 'tiktok',
                  'youtube_statistics', 'youtube')

    def to_representation(self, instance):
        rep = super(InfluencerSerializer, self).to_representation(instance)
        for field in self.fields_to_be_removed:
            if not rep[field]:
                rep.pop(field)
        return rep


class InfluencersPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    influencer = InfluencerSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='InfluencersPage')
        fields = ('header', 'title', 'influencer', 'first_text', 'second_text', 'third_text', 'footer')


class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Voice')
        fields = ('name', 'photo', 'voice')


class StudioSerializer(serializers.ModelSerializer):
    voice = VoiceSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Studio')
        fields = ('logo', 'voice')


class DubSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='DubSeries')
        fields = ('photo', 'preview', 'name', 'total_series', 'dub_series', 'dub_language',
                  'translated_by', 'button', 'url')


class DubMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='DubMovies')
        fields = ('photo', 'preview', 'name', 'duration', 'dub_language',
                  'translated_by', 'button', 'url')


class DubStudioPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    studio = StudioSerializer(many=True, read_only=True)
    series_projects = DubSeriesSerializer(many=True, read_only=True)
    movie_projects = DubMoviesSerializer(many=True, read_only=True)
    fields_to_be_removed = ('series_projects', 'movie_projects',)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='DubStudioPage')
        fields = ('header', 'photo', 'video', 'studio', 'first_text', 'first_text_desc', 'second_text',
                  'second_text_desc', 'third_text', 'third_text_desc', 'projects', 'series_projects',
                  'movie_projects', 'footer')

    def to_representation(self, instance):
        rep = super(DubStudioPageSerializer, self).to_representation(instance)
        for field in self.fields_to_be_removed:
            if not rep[field]:
                rep.pop(field)
        return rep


class AnimationStudioPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='AnimationStudioPage')
        fields = ('header', 'title', 'field', 'footer')


class SeriesFilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='SeriesFilms')
        fields = ('name', 'age', 'series_number', 'language', 'genre',
                  'button', 'url', 'photo', 'preview')


class SeriesFilmsPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    series_films = SeriesFilmsSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='SeriesFilmsPage')
        fields = ('header', 'photo', 'title', 'description', 'projects', 'series_films', 'footer')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Game')
        fields = ('name', 'photo', 'statistics', 'ios_statistics', 'ios', 'android_statistics',
                  'android', 'title', 'appstore_url', 'googleplay_url')


class GameDevPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='GameDevPage')
        fields = ('header', 'title', 'games', 'first_text', 'first_text_desc', 'second_text',
                  'second_text_desc', 'photo_background1', 'photo_background2', 'photo_background3', 'footer')
