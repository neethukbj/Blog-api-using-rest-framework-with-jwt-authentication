from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model=Blog
		exclude=["create_date","updated_at"]


