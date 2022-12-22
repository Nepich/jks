from django.urls import path
from .views import *

urlpatterns = [
    path('main_page/', MainPageView.as_view()),
    path('video_production_page/', VideoProductionPageView.as_view()),
    path('about_us_page/', AboutUsPageView.as_view()),
    path('projects_page/', ProjectsPageView.as_view()),
    path('influencers_page/', InfluencerPageView.as_view()),
    path('influencers_page/<int:pk>/', InfluencerDetailView.as_view()),
    path('dubstudio_page/', DubStudioPageView.as_view()),
    path('animationstudio_page/', AnimationStudioPageView.as_view()),
    path('seriesfilms_page/', SeriesFilmsPageView.as_view()),
    path('gamedev_page/', GameDevPageView.as_view()),
    path('send_form/', FormView.as_view()),
]
