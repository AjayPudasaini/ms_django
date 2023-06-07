from rest_framework.decorators import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from posts.models import Posts
from posts.serializers import PostSerializer


class PostCreateApiView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            posts = serializer.save()
            data['email'] = posts.title
            return JsonResponse({
                'message': f"Post created with title : ({ posts.title }) success",
                'success': True,
                'status' : status.HTTP_201_CREATED,
                'result' : data
            })
        else:
            data = serializer.errors

        return Response(data)


class PostListApiView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse({'posts': serializer.data, "success": True})


class PostDetailAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        post = Posts.objects.get(id=pk)
        serializer = PostSerializer(post)
        return JsonResponse({'post': serializer.data, "success":True})
    


class PostDeleteAPIView(APIView):
    permission_classes = (AllowAny, )
    def delete(self, request, pk):
        post = Posts.objects.get(id=pk)
        post.delete()
        return JsonResponse({'post': post.title, 'message':"post deleted success", "success": True})

