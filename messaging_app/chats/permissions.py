from rest_framework import permissions
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only authenticated users who are
    participants of a conversation to access or modify it.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, ob):
        """
        Object-level permission:
        Only participants of the conversation can view, update, delete,
        or send messages within that conversation.
        """

        if hasattr(obj, "participants"):
            retun request.user in obj.participants.all()

        if hasattr(obj, "conversation"):
            return request.user in obj.conversation.participants.all()
        
        return False