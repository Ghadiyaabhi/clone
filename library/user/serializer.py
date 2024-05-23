from rest_framework import serializers
from user.models import forgotpassword



class forgotpasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = forgotpassword
        fields = '__all__'   



