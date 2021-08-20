from rest_framework import serializers

from myblog.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many = False, read_only = True)
    class Meta:
        model = Post
        fields = ('id','title','category','body','author')

