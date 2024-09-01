from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAdminUser

from apps.article.models import Category
from .serializers import CategoryRUDSerializer


class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRUDSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Category.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
    