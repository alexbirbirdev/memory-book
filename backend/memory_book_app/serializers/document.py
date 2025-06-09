from rest_framework import serializers
from ..models import Document


class DocumentSerializer(serializers.ModelSerializer):
    file_size = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = '__all__'

    def get_file_size(self, obj):
        return obj.file_size