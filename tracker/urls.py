from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('Company', views.CompanyModelViewSet, basename='company')
router.register('Application', views.ApplicationModelViewSet, basename='application')
router.register('Interview', views.InterviewModelViewSet, basename = 'interview')
router.register('Contact', views.ContactModelViewSet, basename = 'contact')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.login_api),

]
