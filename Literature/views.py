from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status

from Literature.models import Literature, Novel, Ancient_Poetry, Modern_Poetry
from Literature import serializers
from Literature.user_auth import IsOwnerReadOnly
from Users.models import UserInfo


# class LiteratureViewSet(viewsets.ModelViewSet):
#     queryset = Literature.objects.all()
#     serializer_class = LiteratureSerializers

# class NovelChapterViewSet(viewsets.ModelViewSet):
#     queryset = NovelChapter.objects.all()
#     serializer_class = NovelChapterSerializers

@csrf_exempt
@api_view(["POST", "GET"])
def literature_list(request):
    print(request.user)
    if request.method == "GET":
        queryset = Literature.objects.all()
        serializer = serializers.LiteratureSerializers(instance=queryset, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        if request.user.is_superuser:
            serializer = serializers.LiteratureSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response('没有操作权限！')


@csrf_exempt
@api_view(["GET"])
def literature_detail(request, pk):
    if request.method == "GET":
        print(request.user)
        if Token.objects.filter(key=pk).exists():
            user = UserInfo.objects.get(pk=Token.objects.filter(key=pk).first().user_id)
            novel_length = Novel.objects.filter(author_id=user).__len__()
            ancient_poetry_length = Ancient_Poetry.objects.filter(author_id=user).__len__()
            modern_poetry_length = Modern_Poetry.objects.filter(author_id=user).__len__()
            return Response(data={"Novel_length": novel_length, "Ancient_Poetry_length": ancient_poetry_length,
                                  "Modern_Poetry_length": modern_poetry_length}, status=status.HTTP_200_OK)


class LiteratureModern(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]

    def get(self, request):
        queryset = Modern_Poetry.objects.filter(author_id=request.user)
        serializer = serializers.LiteratureModernSerializers(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.LiteratureModernSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiteratureModernDetail(APIView):
    permission_classes = (IsAuthenticated, IsOwnerReadOnly)

    @staticmethod
    def get_object(pk):
        try:
            return Modern_Poetry.objects.get(pk=pk)
        except Modern_Poetry.DoesNotExist:
            return

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = serializers.LiteratureModernSerializers(instance=obj, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if obj:
            serializer = serializers.LiteratureModernSerializers(instance=obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=status.HTTP_404_NOT_FOUND)


class LiteratureAncient(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]

    def get(self, request):
        print(request.user)
        queryset = Ancient_Poetry.objects.filter(author_id=request.user)
        serializer = serializers.LiteratureAncientSerializers(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.user)
        serializer = serializers.LiteratureAncientSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiteratureAncientDetail(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated, IsOwnerReadOnly)

    @staticmethod
    def get_object(pk):
        try:
            return Ancient_Poetry.objects.get(pk=pk)
        except Ancient_Poetry.DoesNotExist:
            return

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = serializers.LiteratureAncientSerializers(instance=obj, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        print(request.user)
        obj = self.get_object(pk)
        print(obj.author)
        if obj:
            serializer = serializers.LiteratureAncientSerializers(instance=obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=status.HTTP_404_NOT_FOUND)


class LiteratureNovel(APIView):

    def get(self, request):
        queryset = Novel.objects.filter(author_id=request.user)
        serializer = serializers.NovelSerializers(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(self.request.user)
        serializer = serializers.NovelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiteratureNovelDetail(APIView):
    pass
