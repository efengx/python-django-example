from .models import Vehicles, Trailer
from .serializers import VehiclesSerializer, TrailerSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import logging

logger = logging.getLogger('view.py')


# 获取全部的trailer 名称列表
@permission_classes((permissions.AllowAny,))
class TrailerList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@permission_classes((permissions.AllowAny,))
class TrailerDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# 过滤查询数据
@permission_classes((permissions.AllowAny,))
class VehiclesDetail(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@permission_classes((permissions.AllowAny,))
class VehicleList(generics.ListAPIView):

    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

    def post(self, request, *args, **kwargs):
        return self.list(request, * args, **kwargs)

    def get_queryset(self):
        data = self.request.data
        d = Vehicles.objects.filter(pickup__contains=data['pick_up_state'], delivery__contains=data['delivery'])
        if 'pick_up_city' in data.keys():
            d = d.filter(pickup__icontains=data['pick_up_city'])
        return d
