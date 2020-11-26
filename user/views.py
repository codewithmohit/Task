from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.contrib import messages
from . import sms
from django.contrib.auth.models import Group


# Create your views here.

def home(request):
    return render(request, 'user/basic.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        try:
            signin = Student.objects.filter(email=email, password=password)
            if len(signin) > 0:
                print(signin)
                params = {'signin': signin}
                return render(request, "user/profile.html", params)
            else:
                thank = True
                return render(request, 'user/login.html', {'thank': thank})
        except Exception as e:
            return HttpResponse('e')
    return render(request, 'user/login.html')


def forgetPassword(request):
    if request.method == "POST":
        global mobile
        mobile = request.POST.get('phone', '')

        if len(mobile) > 10 or len(mobile) < 10:
            thank1 = True
            return render(request, 'user/forget.html', {'thank1': thank1})
        user = Student.objects.filter(phone=mobile)
        if len(user) < 0:
            thank = True
            return render(request, 'user/forget.html', {'thank': thank})
        global otp
        otp = sms.otp(mobile)
        return render(request, 'user/otpverify.html')
    return render(request, 'user/forget.html')


def otpVerify(request):
    if request.method == "POST":
        otp1 = request.POST.get('otp', '')
        print("Actual otp=", otp)
        if otp == int(otp1):

            return render(request, "user/cnp.html")
        else:
            thank = True
            return render(request, 'user/otpverify.html', {'thank': thank})
    return render(request, "user/otpverify.html")


def resetPassword(request):
    global mobile
    if request.method == "POST":
        pass1 = request.POST.get('pass1', '')
        pass2 = request.POST.get('pass2', '')
        if pass1 == pass2:
            Student.objects.filter(phone=mobile).update(password=pass1)
            thank = True
            return render(request, 'user/cnp.html', {'thank': thank})
        else:
            messages.error(request, 'Your Password is not matched')
            return render(request, "user/cnp.html")
    return render(request, "user/cnp.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zipcode', '')
        phone = request.POST.get('phone', '')
        signup1 = Student(f_name=fname, l_name=lname, email=email, password=password, address=address, city=city,
                          state=state, zip_code=zip_code, phone=phone)
        signup1.save()
        group = Group.objects.get(name='Student')
        signup1.groups.add(group)

        thank = True
        return render(request, "user/signup.html", {'thank': thank})
    return render(request, 'user/signup.html')
