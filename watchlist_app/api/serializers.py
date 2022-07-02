from dataclasses import fields
from rest_framework import serializers
from watchlist_app.models import Movie
from watchlist_app.models import Watchlist, StreamPlatform
from watchlist_app.models import Review

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
    
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different")
        else:
            return data

class MovieSerializerGonchu(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = "__all__"
    
    def get_len_name(self,object):
        return len(object.name)

    def validate_name(self,value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different")
        else:
            return data

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Watchlist
        fields = "__all__"
    
    def get_len_name(self,object):
        return len(object.title)
    

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    #watchlist = WatchListSerializer(many=True,read_only=True)
    watchlist = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
       model =   StreamPlatform
       fields = "__all__"

