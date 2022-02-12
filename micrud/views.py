from rest_framework import viewsets

from micrud.models import Crud

from micrud.serializers import CrudModelSerializer

 

class CrudViewSet(viewsets.ModelViewSet):

      queryset = Crud.objects.all()

      serializer_class = CrudModelSerializer