from rest_framework import generics, mixins
from .models import Article
from .serializers import ArticleSerializer


class ArticleListCreateView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
