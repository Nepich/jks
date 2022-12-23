from abc import ABC

from django.apps import apps
from rest_framework import serializers


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Header')
        exclude = ('id', )


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Choices')
        exclude = ('footer', )


class FooterSerializer(serializers.ModelSerializer):
    footer_choices = ChoicesSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Footer')
        exclude = ('id', )


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
        exclude = ('id', 'page')


class BasePageSerializer(serializers.Serializer):
    header = HeaderSerializer(many=False, read_only=True)
    footer = FooterSerializer(many=False, read_only=True)


class MainPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    main_page_projects = ProjectMainPageSerializer(many=True, read_only=True)
    main_page_partners = PartnerSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='MainPage')
        exclude = ('id',)


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
        exclude = ('id', )


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='People')
        exclude = ('id', 'page')


class AboutUsPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    about_us_people = PeopleSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='AboutUsPage')
        exclude = ('id', )


class ProjectProjectsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Project')
        exclude = ('id', 'main_page', 'project_page')


class ProjectsPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    project_page_projects = ProjectProjectsPageSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='ProjectsPage')
        exclude = ('id', )


class InfluncerPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='InfluncerPhoto')
        exclude = ('id', 'influencer')


class InfluencerMembersSerializer(serializers.ModelSerializer):
    fields_to_be_removed = ('instagram_statistics',
                            'instagram',
                            'tiktok_statistics',
                            'tiktok',
                            'youtube_statistics',
                            'youtube')

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='InfluencerMembers')
        exclude = ('id', 'influencer')

    def to_representation(self, instance):
        rep = super(InfluencerMembersSerializer, self).to_representation(instance)
        for field in self.fields_to_be_removed:
            if not rep[field]:
                rep.pop(field)
        return rep


class InfluencerDetailSerializer(serializers.ModelSerializer):
    influencer_photo = InfluncerPhotoSerializer(many=True, read_only=True)
    influencer_member = InfluencerMembersSerializer(many=True, read_only=True)
    fields_to_be_removed = ('influencer_photo',
                            'influencer_member',
                            'instagram_statistics',
                            'instagram',
                            'tiktok_statistics',
                            'tiktok',
                            'youtube_statistics',
                            'youtube')

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Influencer')
        exclude = ('id', 'page')

    def to_representation(self, instance):
        rep = super(InfluencerDetailSerializer, self).to_representation(instance)
        for field in self.fields_to_be_removed:
            if not rep[field]:
                rep.pop(field)
        return rep


class InfluencerSerializer(serializers.ModelSerializer):
    fields_to_be_removed = ('instagram_statistics',
                            'instagram',
                            'tiktok_statistics',
                            'tiktok',
                            'youtube_statistics',
                            'youtube')

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Influencer')
        fields = ('id',
                  'name',
                  'instagram_statistics',
                  'instagram',
                  'tiktok_statistics',
                  'tiktok',
                  'youtube_statistics',
                  'youtube')

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
        exclude = ('id', )


class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Voice')
        exclude = ('id', 'studio')


class StudioSerializer(serializers.ModelSerializer):
    voice = VoiceSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Studio')
        exclude = ('id', 'page')


class DubSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='DubSeries')
        exclude = ('id', )


class DubMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='DubMovies')
        exclude = ('id', )


class DubStudioPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    studio = StudioSerializer(many=True, read_only=True)
    series_projects = DubSeriesSerializer(many=True, read_only=True)
    movie_projects = DubMoviesSerializer(many=True, read_only=True)
    fields_to_be_removed = ('series_projects', 'movie_projects',)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='DubStudioPage')
        exclude = ('id', )

    def to_representation(self, instance):
        rep = super(DubStudioPageSerializer, self).to_representation(instance)
        for field in self.fields_to_be_removed:
            if not rep[field]:
                rep.pop(field)
        return rep


class AnimationStudioPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='AnimationStudioPage')
        exclude = ('id', )


class SeriesFilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='SeriesFilms')
        exclude = ('id', )


class SeriesFilmsPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    series_films = SeriesFilmsSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='SeriesFilmsPage')
        exclude = ('id', )


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='Game')
        exclude = ('id', 'page')


class GameDevPageSerializer(BasePageSerializer, serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model(app_label='jks_site', model_name='GameDevPage')
        exclude = ('id', )
