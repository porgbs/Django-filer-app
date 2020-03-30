#
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


# class Videolist(APIView):
#
#     def get(self, request):
#         model = Video.objects.all()
#         serializer = VideoSerializer(model, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class VideoDetail(APIView):
#
#     def get(self, request, id):
#         try:
#             model = Video.objects.get(id=id)
#         except Video.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = VideoSerializer(model)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         try:
#             model = Video.objects.get(id=id)
#         except Video.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = VideoSerializer(model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         try:
#             model = Video.objects.get(id=id)
#         except Video.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def patch(self, request, id):
#         try:
#             model = Video.objects.get(id=id)
#         except Video.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = VideoSerializer(model, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Imagelist(APIView):
#
#     def get(self, request):
#         model = Image.objects.all()
#         serializer = ImageSerializer(model, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ImageDetail(APIView):
#
#     def get(self, request, id):
#         try:
#             model = Image.objects.get(id=id)
#         except Image.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = ImageSerializer(model)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         try:
#             model = Image.objects.get(id=id)
#         except Image.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = ImageSerializer(model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         try:
#             model = Image.objects.get(id=id)
#         except Image.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def patch(self, request, id):
#         try:
#             model = Image.objects.get(id=id)
#         except Image.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = ImageSerializer(model, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Folderlist(APIView):
#
#     def get(self, request):
#         model = Folder.objects.all()
#         serializer = FolderSerializer(model, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = FolderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class FolderDetail(APIView):
#
#     def get(self, request, id):
#         try:
#             model = Folder.objects.get(id=id)
#         except Folder.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = FolderSerializer(model)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         try:
#             model = Folder.objects.get(id=id)
#         except Folder.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = FolderSerializer(model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         try:
#             model = Folder.objects.get(id=id)
#         except Folder.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def patch(self, request, id):
#         try:
#             model = Folder.objects.get(id=id)
#         except Folder.DoesNotExist:
#             return Response("No match found for id = " + id, status=status.HTTP_404_NOT_FOUND)
#         serializer = FolderSerializer(model, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Videolist(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                ):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class Imagelist(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                ):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class Folderlist(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 ):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
