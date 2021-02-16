from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

    def validate_roll(self,value):
        if value>=200:
            raise  serializers.ValidationError('Seats full')
        return value
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'raj' and ct.lower() !='kanpur':
            raise serializers.ValidationError('sorry babu')
        return data

