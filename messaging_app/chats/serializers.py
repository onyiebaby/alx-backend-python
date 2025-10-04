from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model =  User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at', 'full_name']

        def get_full_name(self, obj):
            return f"{obj.first_name} {obj.last_name}"

class ConversationSerializer(serializers.ModelSerializer):
    conversation_label = serializers.CharField(source='conversation_id', read_only=True)
    
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants','created_at', 'conversation_label']

class MessageSerializer(serializers.ModelSerializer):
    sender_email = serializers.SerializerMethodField

    class Meta:
         model = Message
         fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at', 'sender_email']
    def get_sender_email(self, obj):
        return obj.sender.email
    
    def validate_message_body(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Message body cannot be empty.")
        return value