from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from ttc_rest_api.models import TTC_POST_TB, TTC_COMMENT_TB
from ttc_rest_api.serializers import PostSerializer, CommentSerializer

from django.contrib.auth.models import User
from ttc_rest_api.serializers import UserSerializer

from uuid import uuid1


def form_parser(form_post):
    return { k : v[0] for k, v in form_post.items()}

@api_view(['GET','POST'])
def post_all(request):
    if request.method == "GET":
        post_all = TTC_POST_TB.objects.all()
        post_serializer = PostSerializer(post_all, many=True)
        return JsonResponse(post_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == "POST":
        new_post = JSONParser().parse(request)
        post_serializer = PostSerializer(data=new_post)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def post_info(request, uuid):
    try:
        post_detail = TTC_POST_TB.objects.get(uuidPost=uuid)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': f"This post id({uuid}) does not exist."}, safe=False, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        try:
            post = get_object_or_404(TTC_POST_TB, uuidPost=uuid)
            comments = post.comments.all()
            post_serializer = PostSerializer(post_detail)
            comment_serializer = CommentSerializer(comments , many=True)
            return JsonResponse({'Posts': post_serializer.data, 'Comments': comment_serializer.data}, safe=False ,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': e}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    elif request.method == "PUT":
        try:
            post_serializer = PostSerializer(post_detail, data=request.data)
            if post_serializer.is_valid():
                post_serializer.save()
                return JsonResponse(post_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': e}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    elif request.method == "DELETE":
        post_detail.delete()
        return JsonResponse({'message': f'This post id({post_id}) was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def user_all(request):
    if request.method == "GET":
        user_all = User.objects.all()
        user_serializer = UserSerializer(user_all, many=True)
        return JsonResponse(user_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == "POST":
        new_user = JSONParser().parse(request)
        user_serializer = UserSerializer(data=new_user)
        if user_serializer.is_valid():
            try:
                user = User.objects.create_user(new_user['username'], new_user['email'], new_user['password'])
                user.first_name = new_user['first_name']
                user.last_name = new_user['last_name']
                user.save()
                return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def user_info(request, username):
    try:
        user_detail = User.objects.get(username=username)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': f"This username({username}) does not exist."}, safe=False, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        try:
            user_serializer = UserSerializer(user_detail)
            return JsonResponse(user_serializer.data, safe=False ,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': e}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    elif request.method == "PUT":
        try:
            user_serializer = UserSerializer(user_detail, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': e}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)