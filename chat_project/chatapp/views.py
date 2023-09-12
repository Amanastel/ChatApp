from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    context = {}
    return render(request, 'chat.html', context)


def chat(request):
    context = {}
    return render(request, 'chat.html', context)

def Login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    return redirect("index")
        return render(request,'login.html',{})

def Signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password1 = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username,email=email,password=password1)
            if user:
                return redirect("login")
        return render(request,'signup.html',{})

def Logout(request):
    logout(request)
    return redirect("index")




# from django.shortcuts import render
# from django.http import JsonResponse
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import User, Message, Chat
# from .serializers import UserSerializer, MessageSerializer, ChatSerializer
# from rest_framework import status
# from rest_framework.authtoken.models import Token

# # User Registration View
# @csrf_exempt
# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = User.objects.create_user(
#                 username=serializer.validated_data['username'],
#                 password=serializer.validated_data['password']
#             )
#             # Additional user registration logic here (e.g., sending a verification email)
#             return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # User Login View
# @csrf_exempt
# @api_view(['POST'])
# def login_user(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key, "user_id": user.id}, status=status.HTTP_200_OK)
#         return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# # Get Online Users View
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_online_users(request):
#     if request.method == 'GET':
#         online_users = User.objects.filter(is_online=True)
#         serializer = UserSerializer(online_users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# # Start a Chat View
# @csrf_exempt
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def start_chat(request):
#     if request.method == 'POST':
#         recipient_id = request.data.get('recipient_id')
#         sender = request.user  # Assuming the sender is the authenticated user
        
#         # Check if the recipient exists and is online
#         try:
#             recipient = User.objects.get(id=recipient_id, online_status=True)
#         except User.DoesNotExist:
#             return Response({"message": "Recipient is offline or not found"}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Check if a chat between the sender and recipient already exists
#         existing_chat = Chat.objects.filter(participants__in=[sender, recipient])
        
#         if existing_chat.exists():
#             chat = existing_chat.first()
#         else:
#             # If no existing chat, create a new chat
#             chat = Chat.objects.create()
#             chat.participants.add(sender, recipient)
        
#         # Optionally, you can return the chat details or any other relevant data
#         serializer = ChatSerializer(chat)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# # Send a Message View (WebSocket)
# @login_required
# def chat_room(request, room_name):
#     # Implement WebSocket chat functionality here
#     # This view handles WebSocket communication for sending and receiving messages
#     pass

# # Friends Recommendation View
# @api_view(['GET'])
# def suggested_friends(request, user_id):
#     if request.method == 'GET':
#         # Implement the recommendation algorithm here
#         # Return a JSON containing the top 5 recommended friends for the given user_id
#         pass

# # Other views and logic related to chat functionality can be added here

