import uuid
from django.db import models 

# Create your models here.
class User(models.Model):
 user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 first_name = models.charField(max_length=100, null=False)
 last_name = models.charField(max_length=100, null=False)
 email= models.emailField(unique=True,max_length=250, null=False, db_index=True)
 password_hash = models.charField(max_length=250,null=False )
 phone_number = models.charField(max_length=15, null=False, blank=False)
 role = models.charField(max_length=10, choice = [('guest','Guest'), ('host', 'Host'), ('admin','Amin')], null=False)
created_at = models.DateTimeField(auto_now_add=True)   

class Message(models.Model):
 message_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
 sender_id = models.ForeignKey('user', on_delete=models.CASCADE, to_field='user_id', related_name='sent_messages')
 conversations = models.ForeignKey('conversations', on_delete=models.CASCADE, related_name='conversation_messages')
 message_body =models.TextField(null=False)
 sent_at = models.DateTimeField(auto_now_add=True)

 class Conversation(models.Model)
  conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
  participants = models.ManyToManyField('user', related_name='conversation')
  created_at = models.DateTimeField(auto_now_add=True)
                                   