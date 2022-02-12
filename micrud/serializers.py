from rest_framework import serializers

from micrud.models import Crud

 

class CrudModelSerializer(serializers.ModelSerializer):

    class Meta:

      model = Crud

      fields = '__all__'