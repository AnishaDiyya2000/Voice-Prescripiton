from django.shortcuts import render, redirect, resolve_url, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Department, Doctor, Patient, Prescription, admin_doc
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import DocRegistration
# Create your views here.


def home(request):
    return render(request, 'home.html')


def admin_login(request):
    return render(request, 'admin_login.html')


def doctor_login(request):
    departments = Department.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(resolve_url('doc_navbar'))
        return render(request, "doc_login.html", {"error_message": "Invalid username / password", "departments": departments})
    return render(request, "doc_login.html", {"departments": departments})


def doctor_registration(request):
    departments = Department.objects.all()
    if request.method == "POST":
        doc_name = request.POST["name"]
        doc_id = request.POST["username"]
        number = request.POST["mobile"]
        department = request.POST["department"]
        email = request.POST["email"]
        doc_age = request.POST["age"]
        doc_gender = request.POST["gender"]
        passwrd = request.POST["password"]

        try:
            User.objects.get(username=doc_id)
            return render(request, 'doc_login.html', {"error_message": "Username already exists"})
        except User.DoesNotExist:
            user = User(first_name=doc_name, username=doc_id, email=email)
            user.set_password(passwrd)
            user.save()
            doctor = Doctor.objects.create(
                user=user, department=Department.objects.get(pk=department), mobile=number, age=doc_age, gender=doc_gender)
            login(request, user)
            return redirect(resolve_url('doc_navbar'))
    return render(request, 'doc_login.html', {"departments": departments})


def doc_navbar(request):
    return render(request, 'doc_navbar.html')


def m_logout(request):
    logout(request)
    return redirect(resolve_url('home'))


def voice_p(request):
    if request.method == 'POST':
        pat_name = request.POST["name"]
        p_age = request.POST["age"]
        p_gender = request.POST["gender"]
        diagnosis = request.POST["diagnosis"]
        Medicine = request.POST["medicine"]
        Af_Bf = request.POST["timings"]
        Advice = request.POST["advice"]
        new_patient = Patient.objects.create(
            name=pat_name, age=p_age, gender=p_gender)
        Prescription.objects.create(diagnosis=diagnosis, patient=new_patient, medicine=Medicine,
                                    time=Af_Bf, advice=Advice)
        return render(request, 'voice_p.html', {"success_message": "Prescription added successfully"})
    return render(request, 'voice_p.html')


# def admin_base(request):
#     return render(request, 'admin_base.html')


def addAndShow(request):
    if request.method == 'POST':
        fm = DocRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name1']
            mb = fm.cleaned_data['mobile']
            dep = fm.cleaned_data['department_doc']
            age = fm.cleaned_data['age']
            gd = fm.cleaned_data['gender']
            em = fm.cleaned_data['email']
            reg = admin_doc(name1=nm, mobile=mb,
                            department_doc=dep, age=age, gender=gd, email=em)
            reg.save()
            fm = DocRegistration()
    else:
        fm = DocRegistration()
    stud = admin_doc.objects.all()
    return render(request, 'addAndShow.html', {'form': fm, 'stu': stud})


def delete_data(request, id):
    if request.method == 'POST':
        pi = admin_doc.objects.get(pk=id)
        pi.delete()
        return redirect(resolve_url('addAndShow'))


def updateDoc(request, id):
    if request.method == 'POST':
        pi = admin_doc.objects.get(pk=id)
        fm = DocRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = admin_doc.objects.get(pk=id)
        fm = DocRegistration(instance=pi)
    return render(request, 'updateDoc.html', {'form': fm})
