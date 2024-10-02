from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from blogs.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from django.core.paginator import Paginator


class PublicBlogView(APIView):
    
    def get(self,request):
        print("hiiii")
        try:
            blogs = Blog.objects.all()

            if request.GET.get('search'):
                search = request.GET.get('search')
                blogs=blogs.filter(Q(title__icontains = search) | Q(descriptiom__icontains = search))
            page_number=request.GET.get('page',1)
            paignator=Paginator(blogs,1)

            serializer=BlogSerializer(paignator.page(page_number),many=True)
            return Response({
                'data':serializer.data,
                'message':'blog fetched succesfully'
                })
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
                })


class BlogView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get(self,request):
        try:
            blogs = Blog.objects.filter(user= request.user)


            if request.GET.get('search'):
                search = request.GET.get('search')
                blogs=blogs.filter(Q(title__icontains = search) | Q(descriptiom__icontains = search))

            serializer=BlogSerializer(blogs,many=True)
            return Response({
                'data':serializer.data,
                'message':'blog fetchedsuccesfully',
                })
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
                })



    def post(self,request):
        try:
            data=request.data
            data['user']=request.user.id
            serializer= BlogSerializer(data=data)
            
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message':'something went wrong'
                    })

            serializer.save()
            

            return Response({
                'data':serializer.data,
                'message':'blog is created'
                })

        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
                })



    def patch(self,request):
        try:
            data=request.data
            blog=Blog.objects.filter(uid=data.get("uid"))
            if not  blog.exists():
                return Response({"data":{},"message":"invalid blog uid"})

            if request.user!= blog[0].user:
                return Response({"data":{},"message":"your are not authorised to this"})

            serializer=BlogSerializer(blog[0],data=data,partial=True)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message':'something went wrong'
                    })

            serializer.save()
            

            return Response({
                'data':serializer.data,
                'message':'blog is updated'
                })

            
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
                })


    def delete(self,request):
        try:
            data=request.data
            blog=Blog.objects.filter(uid=data.get("uid"))
            if not  blog.exists():
                return Response({"data":{},"message":"invalid blog uid"})

            if request.user!= blog[0].user:
                return Response({"data":{},"message":"your are not authorised to this"})

            blog[0].delete()
            return Response({"data":{},"message":"Blog Deleted Successfully..!"})

            
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
                })
 

