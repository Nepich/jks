from django.apps import apps
from django.utils import translation
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Manager
from .serializers import MainPageSerializer, VideoProductionPageSerializer, AboutUsPageSerializer, \
    ProjectsPageSerializer, InfluencersPageSerializer, InfluencerDetailSerializer, DubStudioPageSerializer, \
    AnimationStudioPageSerializer, SeriesFilmsPageSerializer, GameDevPageSerializer, FormSerializer
from .services import send_notifications
from .tasks import send_mail, send_telegram


class BasePageView(RetrieveAPIView):
    """View to get landing context"""
    queryset = None
    serializer_class = None
    pk = None

    def get(self, request, *args, **kwargs):
        try:
            language = request.GET.get('language')
            with translation.override(language):
                queryset = self.get_queryset().objects.select_related('header', 'footer').get(pk=self.pk)
                serializer = self.get_serializer(queryset, context={"lang": language, 'request': request})
                return Response(serializer.data)
        except Exception as e:
            print(e)


class MainPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='MainPage')
    serializer_class = MainPageSerializer
    pk = 1


class VideoProductionPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='VideoProductionPage')
    serializer_class = VideoProductionPageSerializer
    pk = 1


class AboutUsPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='AboutUsPage')
    serializer_class = AboutUsPageSerializer
    pk = 1


class ProjectsPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='ProjectsPage')
    serializer_class = ProjectsPageSerializer
    pk = 1


class InfluencerPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='InfluencersPage')
    serializer_class = InfluencersPageSerializer
    pk = 1


class InfluencerDetailView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='Influencer')
    serializer_class = InfluencerDetailSerializer

    def get(self, request, *args, **kwargs):
        try:
            language = request.GET.get('language')
            with translation.override(language):
                queryset = self.get_queryset().objects.get(pk=self.kwargs['pk'])
                serializer = self.get_serializer(queryset, context={"lang": language, 'request': request})
                return Response(serializer.data)
        except Exception as e:
            print(e)


class DubStudioPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='DubStudioPage')
    serializer_class = DubStudioPageSerializer
    pk = 1

    def get(self, request, *args, **kwargs):
        try:
            language = request.GET.get('language')
            with translation.override(language):
                queryset = self.get_queryset().objects.select_related('header', 'footer')\
                    .prefetch_related('studio__voice').get(pk=self.pk)
                serializer = self.get_serializer(queryset, context={"lang": language, 'request': request})
                return Response(serializer.data)
        except Exception as e:
            print(e)


class AnimationStudioPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='AnimationStudioPage')
    serializer_class = AnimationStudioPageSerializer
    pk = 1


class SeriesFilmsPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='SeriesFilmsPage')
    serializer_class = SeriesFilmsPageSerializer
    pk = 1


class GameDevPageView(BasePageView):
    queryset = apps.get_model(app_label='jks_site', model_name='GameDevPage')
    serializer_class = GameDevPageSerializer
    pk = 1


class FormView(CreateAPIView):
    """View to send a form"""
    queryset = apps.get_model(app_label='jks_site', model_name='Form')
    serializer_class = FormSerializer

    def perform_create(self, serializer):
        try:
            mail_to = [recepient['email'] for recepient in Manager.objects.all().values('email')]
            data = self.request.data
            interest = apps.get_model(app_label='jks_site', model_name='Choices').objects.get(pk=data["type"]).type
            send_mail(self.request.data, interest, mail_to)
            send_telegram(self.request.data, interest)
            serializer.save()
        except Exception as e:
            print(e)
