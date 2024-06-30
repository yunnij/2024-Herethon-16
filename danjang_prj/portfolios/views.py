from .models import Portfolio, Career, Video, Photo
from .serializers import PortfolioSerializer, CareerSerializer, VideoSerializer, PhotoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, generics

class PortfolioViewSet(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    
    # 테스트할 때는 주석
    # def perform_create(self, serializer):
    #     serializer.save(name = self.request.user)


class PortfolioListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def portfolio(self, request, *args, **kwargs):
        return self.create(request)

class PortfolioDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    # def delete(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)


class CareerViewSet(ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    def get_queryset(self, **kwargs):
        id = self.kwargs['portfolio_id']
        return self.queryset.filter(portfolio=id)

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self, **kwargs):
        id = self.kwargs['portfolio_id']
        return self.queryset.filter(portfolio=id)

class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self, **kwargs):
        id = self.kwargs['portfolio_id']
        return self.queryset.filter(portfolio=id)