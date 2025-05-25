from rest_framework import serializers
from .models import (
    SuspectList,
    MurderStat,
    Detective,
    Trait,
    SuspectTrait,
    Statement,
    Location
)

class SuspectSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField()  # Human-readable location

    class Meta:
        model = SuspectList
        fields = '__all__'

class MurderSerializer(serializers.ModelSerializer):
    suspect = serializers.StringRelatedField()
    location = serializers.StringRelatedField()

    class Meta:
        model = MurderStat
        fields = '__all__'

class DetectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detective
        fields = '__all__'

class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = '__all__'

class SuspectTraitSerializer(serializers.ModelSerializer):
    suspect = serializers.StringRelatedField()
    trait = serializers.StringRelatedField()

    class Meta:
        model = SuspectTrait
        fields = '__all__'

class StatementSerializer(serializers.ModelSerializer):
    detective = serializers.StringRelatedField()
    suspect = serializers.StringRelatedField()

    class Meta:
        model = Statement
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'