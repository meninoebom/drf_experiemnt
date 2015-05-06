from rest_framework import serializers
from main_app.models import Resume
from main_app.models import Experience
from main_app.models import Qualification

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification