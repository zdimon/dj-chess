from rest_framework import serializers

class ProfileSaveRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    publicname = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    photo_user = serializers.FileField(allow_empty_file=True, required=False)
    photo_car = serializers.FileField(allow_empty_file=True, required=False)
    photo_user_base64 = serializers.CharField(required=False)
    photo_car_base64 = serializers.CharField(required=False)