from rest_framework import serializers
from natica.models import FilePrefix

class FilePrefixSerializer(serializers.ModelSerializer):
    telescope = serializers.StringRelatedField(many=False)
    instrument = serializers.StringRelatedField(many=False)
    class Meta:
        model = FilePrefix
        fields = ('telescope', 'instrument')
