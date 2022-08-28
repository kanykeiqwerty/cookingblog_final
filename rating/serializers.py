from rest_framework import serializers
from . models import Review



class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.email')
    recipe=serializers.ReadOnlyField(source='recipe.title')
    class Meta:
        model=Review
        fields='__all__'

    def create(self, validated_data):
        request=self.context.get('request')
        user=request.user
        recipe=self.context.get('recipe')
        validated_data['user']=user
        validated_data['recipe']=recipe
        return super().create(validated_data)