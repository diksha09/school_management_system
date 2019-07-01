from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from management.models import  SchoolUser, Klass, Subject, Div, Student, StudentFee, Teacher, Department, StudAtt, TeachAtt, AssiTeacher
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json 
import string
import traceback
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission
from .serializers import SchoolUserSerializer

# Create your views here.
errorMessage = "Something went wrong, Please try after sometime."
addSuccessMessage = "Successfully Added"
updateSuccessMessage = "Successfully Updated"
removeSuccessMessage = "Deleted Successfully"


@api_view(['POST'])
def AddAdminUser(request):
    try:
        with transaction.atomic():
            # serializer.save()
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            firstname = request.data['firstname']
            lastname = request.data['lastname']
            address = request.data['address']
            gender = request.data['gender']
            phone_no = request.data['phone_no']
            
            user = User.objects.create(username=username,
                                 email=email,
                                 first_name=firstname,
                                 last_name=lastname,
                                 password=make_password(password),
                                 is_superuser=0,
                                 is_staff=0,
                                 is_active=1,
                                date_joined=timezone.now())
            if user is not None:
                g = Group.objects.get(name='Principal')
                g.user_set.add(user)
                SchoolUser1 = SchoolUser.objects.create(address=address,
                                                        firstname=firstname,
                                                        lastname=lastname,
                                 gender=gender,
                                 phone_no=phone_no,
                                 user_auth_id=user.id,
                                 role=1
                                 );
                if SchoolUser1 is not None:
                    return Response({"message" : "Done", "status" : "1", "object" : {"id" : SchoolUser1.id, "firstname" : user.first_name, "lastname":user.last_name, "username" : user.username, "email" : user.email, "address" : SchoolUser1.address}}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message" : "Sorry Something Went Wrong", "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"message" : "Sorry Something Went Wrong", "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    except Exception as e:
        print(e)
        return Response({"message" : "Sorry Something Went Wrong", "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@csrf_exempt
def appAdminLogin(request):
    try:
        with transaction.atomic():
            received_json_data = json.loads(request.body, strict=False)
            username = received_json_data['username']
            password = received_json_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                checkGroup1 = user.groups.filter(name='Principal').exists()
                checkGroup2 = user.groups.filter(name='Teacher').exists()
                checkGroup3 = user.groups.filter(name='Student').exists()
                if checkGroup1 or checkGroup2 or checkGroup3:
                    existedUser = SchoolUser.objects.get(user_auth_id=user.id)
                    if user.is_active == 1 and existedUser.status == 1:
                        token = ''
                        try:
                            user_with_token = Token.objects.get(user=user)
                        except:
                            user_with_token = None
                            
                        if user_with_token is None:
                            token1 = Token.objects.create(user=user)
                            token = token1.key
                        else:
                            Token.objects.get(user=user).delete()
                            token1 = Token.objects.create(user=user)
                            token = token1.key                
                        return Response({"status" : "1", "token" : token, "role" : existedUser.role}, status=status.HTTP_200_OK)
                    else:
                        return Response({"message" : "Your account has been blocked", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({"message" : "Email or Password incorrect", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"message" : "Email or Password incorrect", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
            # else:
            #    return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception:
        print(traceback.format_exc())
        return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def addUser(request):
    try:
        with transaction.atomic():
            API_key = request.META.get('HTTP_AUTHORIZATION')
            if API_key is not None:
                try:
                    token1 = Token.objects.get(key=API_key)
                    user = token1.user
                    checkGroup = user.groups.filter(name='Principal').exists()
                    checkGroup1 = user.groups.filter(name='Teacher').exists()
                    checkGroup2 = user.groups.filter(name='Student').exists()
                except:
                    return Response({"message" : "Session Expired!! Please Login Again", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
                if checkGroup or checkGroup1 or checkGroup2:
                    permissions = Permission.objects.filter(user=user)
                    print(permissions)
                    if user.has_perm('api.add_schooluser'):
                        username = request.data["username"]
                        email = request.data["email"]
                        password = request.data["password"]
                        firstname = request.data["firstname"]
                        lastname = request.data["lastname"]
                        gender = request.data["gender"]
                        phone_no = request.data["phone_no"]
                        des = request.data["des"]
                        role = -1
                        if des == "Principal":
                            role = 1
                        elif des == "Teacher":
                            role = 2
                        elif des == "Student":
                            role = 3
                        
                        user = User.objects.create(username=username,
                                    email=email,
                                    first_name=firstname,
                                    last_name=lastname,
                                    password=make_password(password),
                                    is_superuser=0,
                                    is_staff=0,
                                    is_active=1,
                                    date_joined=timezone.now())
                                             
                        if user is not None:
                            
                            g = Group.objects.get(name=des)
                            g.user_set.add(user)
                            
                            kuser = SchoolUser.objects.create(address=address,
                                                                    
                                                                      user_auth_id=user.id,
                                                                      status=1,
                                                                      role=role,
                                                                      gender=gender
                                             );
                            if kuser is not None:
                                return Response({"message" : addSuccessMessage, "status" : "1", "object" : {"id" : OtherUserDetails.id}}, status=status.HTTP_201_CREATED)
                            else:
                                return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    
                        # else:
                            # return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
                    else:
                        return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print(traceback.format_exc())
        return Response({"message" : str(e), "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@csrf_exempt
def logoutAdmin(request):
    try:
        with transaction.atomic():
                        
            received_json_data = json.loads(request.body, strict=False)
            token = received_json_data['token']
            try:
                token1 = Token.objects.get(key=token)
            except:
                return Response({"message" : "Session Expired!! Please Login Again", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)                  
            if token1 is not None: 
                user = token1.user 
                if user is not None: 
                    user.auth_token.delete()
                
                return Response({"message" : "Successfully Logged Out", "status" : "1"}, status=status.HTTP_200_OK)
            else:
                return Response({"message" : "User Does Not Exist!!", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception:
        print(traceback.format_exc())
        return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

