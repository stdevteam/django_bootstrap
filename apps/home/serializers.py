from rest_framework import serializers

from .models import Checkmarks


class CheckmarksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkmarks
        fields = '__all__'
