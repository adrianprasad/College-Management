from django.shortcuts import redirect, render
from clgapp.models import student_details,teacher_details,coursename
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginpage(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, f'Welcome {username}')
            return redirect('addcourse')
        else:
            messages.info(request,'Invalid Username or Password.Try Again.')
            return redirect('login')
    else:
        return redirect('login')

def signup(request):
    return render(request,'signup.html')

def createuser(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This usernae already exists!!!')
                print("Username already taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username= username,
                    password= password,
                    email= email)
                user.save()
                print("successed")
                return redirect('login')
        else:
            messages.info(request,'Password doesnt match!!!!')
            print("password is not matching...")
            return redirect('signup')
    
    else:
        return render(request,'signup.html')

def about(request):
    if request.user.is_authenticated:
        return render(request,'about.html')
    return redirect('login')

def addcourse(request):
    if request.user.is_authenticated:
        v=student_details.objects.all()
        context= {'ve':v}
        return render(request,'addcourse.html',context)
    return redirect('login')

def addcour(request):
    if request.method == 'POST':
        course=request.POST['course']
        fee=request.POST['fee']
        stu=coursename(Course=course,
                        fee=fee)
        stu.save()
        print('success')
        return redirect('addteacher')

def addteacher(request):
    if request.user.is_authenticated:
        v=coursename.objects.all()
        context= {'ve':v}
        return render(request,'addteacher.html',context)
    return redirect('login')

def addtea(request):
    if request.method == 'POST':
        Tea_name=request.POST['teaname']
        stu=teacher_details(Teacher_name=Tea_name,)
        stu.save()
        print('success')
        return redirect('addstudent')

def addstudent(request):
    if request.user.is_authenticated:
        v=coursename.objects.all()
        e=teacher_details.objects.all()
        context= {'ve':v,'we':e}
        return render(request,'addstud.html',context)
    return redirect('login')

def addstud(request):
    if request.method == 'POST':
        name=request.POST['sname']
        Place=request.POST['place']
        stud_age=request.POST['age']
        tnam=request.POST['Tname']
        teaname=teacher_details.objects.get(id=tnam)
        sel=request.POST['course']
        course=coursename.objects.get(id=sel)
        stu=student_details(Stud_name=name,
            Course=course,
            TName=teaname,
            Place=Place,
            stud_age=stud_age)
        stu.save()
        print('success')
        return redirect('show')
    ve=coursename.objects.all()
    return render(request,'addstud.html',{'ve':ve} )

def show(request):
    v=student_details.objects.all()
    return render(request, 'show.html',{'ve':v})

def profile(request,pk):
        stud=student_details.objects.get(id=pk)
        
        return render(request,'profile.html',{'stud':stud})

def edit (request,pk): 
    stud=teacher_details.objects.get(id=pk)
    std=coursename.objects.get(id=pk)
    return render(request, 'edit.html', {'stud': stud,'std':std})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')

def edit_stud(request,pk):
    if request.method=='POST':
        stud=student_details.objects.get(id=pk)
        stud.Stud_name = request.POST.get('sname')
        stud.Course = request.POST.get('course')
        stud.TName = request.POST.get('Tname')
        stud.Place = request.POST.get('place')
        stud.stud_age=request.POST.get('age')
        stud.save() 
        print("successfully updated")
        return redirect('profile')
    return render(request,'edit.html',)

def delete_stud(request,pk):
     employee=student_details.objects.get(id=pk)
     employee.delete()  
     print("successfully deleted")
     return redirect('show')