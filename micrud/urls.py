from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views as micrud_views

 

router = DefaultRouter()

router.register(r'micrud', micrud_views.CrudViewSet, basename='micrud')

urlpatterns = [

    path('', include(router.urls))

]