from rest_framework import serializers
from news.models import News


class NewsSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ("user",)
