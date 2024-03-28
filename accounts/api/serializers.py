from rest_framework import serializers
from  ..models import Account

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        if Account.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use")
        return value

    def validate_username(self, value):
        if Account.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already in use")
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get("password")
        password2 = value
        if password != password2:
            raise serializers.ValidationError("Passwords must match")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        account = Account.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            is_active=True  # You might want to send an email confirmation before setting it to True
        )
        return account