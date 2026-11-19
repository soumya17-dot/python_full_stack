from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import Student_table
from .forms import Student_form_data
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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

def Student_form_dj(request):
    if request.method=="POST":
        form=Student_form_data(request.POST)
        if form.is_valid():
            reg_no1=form.cleaned_data['reg_no1']
            name1=form.cleaned_data['name1']
            email1=form.cleaned_data['email1']
            return HttpResponse("Saved Successfully!")
        else:
            return HttpResponse("Invalid Data")
    else:
        form=Student_form_data()
        return render(request,'Student_form_data.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid Username or Password!")
    return render(request,'login.html')
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')
def user_logout(request):
    if request.method == 'POST':
        logout(request)

        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Logout Successful</title>

            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: 'Segoe UI', Arial, sans-serif;
                }

                body {
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: linear-gradient(135deg, #e8edf3, #cbd5e1);
                }

                .container {
                    width: 400px;
                    padding: 45px 35px;
                    background: #ffffff;
                    border-radius: 12px;
                    text-align: center;
                    box-shadow: 0 10px 35px rgba(15, 23, 42, 0.12);
                    border: 1px solid #e2e8f0;
                }

                .icon {
                    width: 65px;
                    height: 65px;
                    line-height: 65px;
                    margin: 0 auto 20px;
                    border-radius: 50%;
                    background: #dcfce7;
                    color: #16a34a;
                    font-size: 35px;
                }

                h1 {
                    color: #0f172a;
                    font-size: 25px;
                    margin-bottom: 15px;
                }

                p {
                    color: #64748b;
                    font-size: 15px;
                    line-height: 1.6;
                    margin-bottom: 30px;
                }

                a {
                    display: block;
                    padding: 13px;
                    background: #1e3a8a;
                    color: white;
                    text-decoration: none;
                    border-radius: 7px;
                    font-weight: 600;
                    transition: 0.3s;
                }

                a:hover {
                    background: #2563eb;
                    transform: translateY(-2px);
                }

                @media (max-width: 450px) {
                    .container {
                        width: 90%;
                        padding: 35px 25px;
                    }
                }
            </style>
        </head>

        <body>

            <div class="container">

                <div class="icon">&#10004;</div>

                <h1>Logged Out Successfully!</h1>

                <p>You have successfully logged out of your account.
                Thank you for visiting!</p>

                <a href="/login/">Login Again</a>

            </div>

        </body>
        </html>
        """

        return HttpResponse(html)

    return HttpResponse("Invalid request!")