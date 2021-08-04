from rest_framework.serializers import ModelSerializer
from .models import Category

class CategoryListAPIView(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name' #name bu categoryda yaratgan qatorimiz
        ]