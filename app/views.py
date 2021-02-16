from django.shortcuts import render,HttpResponse
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class MyView(View):
    def post(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializers = StudentSerializer(data=pythondata)
        if  serializers.is_valid():
            serializers.save()
            res = {'msg':'Data inserted successfully'}
            json_data =JSONRenderer().render(res)
            return HttpResponse(json_data,content_type ='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data,content_type = 'application/json')
    def get(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata =JSONParser().parse(stream)
        id  = pythondata.get('id',None)
        if id is None:
            stu = Student.objects.all()
            serializers = StudentSerializer(stu,many=True)
            json_data = JSONRenderer().render(serializers.data)
            return HttpResponse(json_data,content_type='applocation/json')
        else :
            stu = Student.objects.get(id=id)
            serializers = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializers.data)
            return HttpResponse(json_data,content_type ='application/json')
    def put(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializers = StudentSerializer(stu,data=pythondata)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'data updated successfully'}
            json_data = JSONParser().parse(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONParser().parse(serializers.errors)
        return HttpResponse(json_data,content_type='application/json')
    def put(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata =JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializers = StudentSerializer(stu,data=pythondata,partial=True)
        if serializers.is_valid():
            serializers.save()
            res ={'msg':'data updated'}
            json_data =JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data =JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data,content_type='application/json')
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')

        


