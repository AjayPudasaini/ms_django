from rest_framework import serializers
from user.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'phone_number']

    def save(self):
        user = User(
            email = self.validated_data['email'],
            phone_number = self.validated_data['phone_number'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'password must match.'})
        
        user.set_password(password)
        user.save()

        return user



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    

class TokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD



class Codeing(serializers.Serializer):
    system_url = serializers.URLField()
    code = serializers.ChoiceField(choices=[])
    display = serializers.CharField()

class Codeable(serializers.Serializer):
    code = Codeing()
    text = serializers.CharField()


class MySerializer(serializers.Serializer):
    a = Codeable() # system_url = google.com, code = (1, 1), (2, 3), (3, 3)
    b = Codeable() # system_url = gmail.com, code = ('a','a'), ('b','b'), ('c','c')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['a'].system_url = "google.com"
        self.fields['a'].code = self.get_dynamic_choices_a()

        self.fields['b'].system_url = "gmail.com"
        self.fields['b'].code = self.get_dynamic_choices_b()


    def get_dynamic_choices_a(self):
        return [
            ('choice1', 'Choice 1'),
            ('choice2', 'Choice 2'),
            ('choice3', 'Choice 3'),
        ]
    
    def get_dynamic_choices_b(self):
        return [
            (1, 1),
            (2, 2),
            (3, 3),
        ]

   
