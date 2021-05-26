from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from core.models_serializers import TemoignageSerializer
from core.models import Temoignage
from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema



class TemoignageViewset(ListModelMixin, CreateModelMixin, GenericViewSet):
    
    serializer_class = TemoignageSerializer
    queryset = Temoignage.objects.all()
    
    @swagger_auto_schema(operation_description="Creer un temoignage en envoyant "\
            "une requete POST multipart/data avec les champs name, content et image de type File")
    def create(self, request, *args, **kwargs):
        instance = Temoignage()
        instance.name = self.request.data.get('name')
        instance.content = self.request.data.get('content')
        try:
            instance.image = self.request.FILES['image']
        except:
            pass
        instance.save()
        return JsonResponse(TemoignageSerializer(instance).data)
