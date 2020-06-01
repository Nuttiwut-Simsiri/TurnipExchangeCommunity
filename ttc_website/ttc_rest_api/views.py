from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from ttc_rest_api.models import TTC_POST_TB
from ttc_rest_api.serializers import PostSerializer

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
def post_info(request, post_id):
    try:
        post_detail = TTC_POST_TB.objects.get(id=post_id)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': f"Post id({post_id}) does not exist."}, safe=False, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        try:
            post_serializer = PostSerializer(post_detail)
            return JsonResponse(post_serializer.data, safe=False ,status=status.HTTP_200_OK)
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
        return JsonResponse({'message': f'Post id({post_id}) was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
