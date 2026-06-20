from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('companyapi', views.CompanyModelViewSet, basename='company')
router.register('applicationapi', views.ApplicationModelViewSet, basename='application')
router.register('interviewapi', views.InterviewModelViewSet, basename = 'interview')
router.register('contactapi', views.ContactModelViewSet, basename = 'contact')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.login_api),

]
