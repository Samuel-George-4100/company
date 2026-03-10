from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.views import View

class Add_Employee(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'add_employee.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_employee')
        return render(request, 'add_employee.html', {'form': form})


class View_Employee(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'view_employee.html', {'employees': employees})