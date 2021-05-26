from core.models import Temoignage
from rest_framework.serializers import ModelSerializer


class TemoignageSerializer(ModelSerializer):
    
    class Meta:
        model = Temoignage
        fields = ('id', 'name', 'content', 'image')
