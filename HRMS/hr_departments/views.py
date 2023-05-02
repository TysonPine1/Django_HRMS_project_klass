from django.shortcuts import render, redirect
from .models import DepartmentModel
from .forms import DepartmentForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.db.models import Q

# Create your views here.
class SearchBy(View):

    def get(self, request):
        search = request.GET.get('search')
        if search:    
            departments = DepartmentModel.objects.filter(
                Q(name__icontains=search) | 
                Q(sequence__icontains=search) |
                Q(meeting_date__icontains=search) |
                Q(total_employees__icontains=search) |
                Q(note__icontains=search) |
                Q(status__icontains=search) |
                Q(create_date__icontains=search)
            )
        else:      
            departments = DepartmentModel.objects.all()
        return render(request, 'department_list.html', {'all_departments': departments})

class OrderBy(View):

    def get(self, request):
        order = request.GET.get('order')
        departments = DepartmentModel.objects.all().order_by("-"+ order)
        order_selected = {str(order): 'btn-primary text-white'}
        return render(request, 'department_list.html', {'all_departments': departments, 'order_selected': order_selected})
        
class Department(PermissionRequiredMixin, View):
    permission_required = 'hr_departments.view_departmentmodel'
    login_url = 'login'

    def get(self, request, department_id):
        department = DepartmentModel.objects.get(id=department_id)  
        return render(request,'department_detail.html', {'department': department})

class AllDepartments(LoginRequiredMixin, View):
    paginate_by = 1
    login_url = 'login'
    
    def get(self, request):
        all_departments = DepartmentModel.objects.all()
        return render(request,'department_list.html', {'all_departments': all_departments})

class AddDepartment(PermissionRequiredMixin, View):
    permission_required = 'hr_departments.add_departmentmodel'
    login_url = 'login'

    def get(self, request):
        print('AddDepartment get call +++++++++++++++')
        form = DepartmentForm()
        return render(request,'department_create.html',{'form':form}) 
    def post(self, request):
        print('AddDepartment post call ++++++++++++', request.POST)
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            return redirect('/hr_departments/show_department/') 

class UpdateDepartment(PermissionRequiredMixin, View):
    permission_required = 'hr_departments.change_departmentmodel'
    login_url = 'login'

    def get(self, request, department_id):
        department = DepartmentModel.objects.get(id=department_id)  
        form = DepartmentForm(instance=department)
        return render(request, 'department_update.html', {'form': form, 'uploaded_image': department.attachment})
    def post(self, request, department_id):
        department = DepartmentModel.objects.get(id=department_id)  
        form = DepartmentForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            form.save()
            return redirect('/hr_departments/detail/' + str(department_id) + '/')

class DeleteDepartment(PermissionRequiredMixin, View):
    permission_required = 'hr_departments.delete_departmentmodel'
    login_url = 'login'

    def get(self, request, department_id):
    #     department = DepartmentModel.objects.get(id=department_id)  
    #     return render(request, 'department_delete.html', {'department': department})        
    # def post(self, request, department_id):
        department = DepartmentModel.objects.filter(id=department_id)
        department.delete()
        return redirect('/hr_departments/show_department/')