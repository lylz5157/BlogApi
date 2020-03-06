from rest_framework import serializers

from .models import db_classify


class db_classifyserializers(serializers.ModelSerializer):
    class Meta:
        model = db_classify

        fields = '__all__'
