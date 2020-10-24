from rest_framework import serializers

from core.models import Article

# ? Serializer??
# ? Convert to JSON
# ? Validate for data passed

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        # fields = [
        #     'id',
        #     'title',
        #     'author',
        #     'email',
        #     'date',
        # ]
        fields = '__all__'