# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)    
#     def __str__(self):
#         return self.user.name
    


# class Message(models.Model):
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.profile.name

    
    
# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
    
    
    
# class Friend(models.Model):
    # users = models.ManyToManyField(User)
    # current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)
    
    # @classmethod
    # def make_friend(cls, current_user, new_friend):
    #     friend, created = cls.objects.get_or_create(current_user=current_user)
    #     friend.users.add(new_friend)
        
    # @classmethod
    # def lose_friend(cls, current_user, new_friend):
    #     friend, created = cls.objects.get_or_create(current_user=current_user)
    #     friend.users.remove(new_friend)
        
    # def __str__(self):
    #     return self.current_user.username
    
    
    
    
    
    
from django.db import models
from django.contrib.auth.models import User as DjangoUser

class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    online_status = models.BooleanField(default=False)
    # Add other user fields like online status

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"From {self.sender} to {self.recipient}: {self.content}"
    
    
class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')
    chat_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Add more fields as needed

    def __str__(self):
        return self.chat_name