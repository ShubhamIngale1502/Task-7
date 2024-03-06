from rest_framework.views import APIView
from django.views import View
from faker import Faker
from .models import Employee
from .serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse


# Create your views here.
class  CreateFakeView(APIView):
    def post(self, request, *args, **kwargs):
        fake = Faker()
        num_employees = int(request.data.get('num_employees', 100))
        employees = []
        for i in range(num_employees):
            employee = Employee(
                    name=fake.name(),
                    email = fake.email(),
                    salary = fake.random_int(50000,100000),
                    address = fake.address()
                    
                )
            employees.append(employee)
        Employee.objects.bulk_create(employees)
        serializer = EmpSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
class CreateAPI(View):
    
    def get(self, request, format=None):
        template = get_template('employee_list.html')
        employees = Employee.objects.all()
        context = {'employees': employees}
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if pdf.err:
            return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
        return HttpResponse(result.getvalue(), content_type='application/pdf')
        
        


