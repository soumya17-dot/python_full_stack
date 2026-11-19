from django.shortcuts import render
from  django.http import HttpResponse
from .models import Student_table
# Create your views here.
def home(request):
    data={
        'name':"Soumm",
        'age':17,
        'department':"BCA"
    }
    marks=[100,40,50]
    return render(request,'home.html',{'data':data,'marks':marks})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def forms(request):
    if request.method=="POST":
        reg_no=request.POST.get('req_no')
        name=request.POST.get('name')
        email=request.POST.get('email')
        marks=request.POST.get('marks')
        dob=request.POST.get('dob')
        Student_table.objects.create(reg_no=reg_no,name=name,email=email,marks=marks,dob=dob)
        return HttpResponse("saved successfully")
    return render(request,'Student_form.html')