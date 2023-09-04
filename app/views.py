from django.shortcuts import render



# Create your views here.
from app.models import *

def insert_school(request):

    if request.method=='POST':
        scn=request.POST['scn']
        sp=request.POST['sp']
        sl=request.POST['sl']
        so=school.objects.get_or_create(SCName=scn,SCPrincipal=sp,SCLocation=sl)[0]
        so.save()
        QLSO=school.objects.all()
        d={'QLSO':QLSO}
        return render(request,'dispaly_school.html',d)
    return render(request,'insert_school.html')

def insert_student(request):
  

 if request.method=='POST':
    sc=request.POST['sc']
    sn=request.POST['sn']
    si=request.POST['si']

    so=school.objects.get(SCName=sc)

    STO=Student.objects.get_or_create(Scname=SO,Sname=sn,Sid=si)[0]
    STO.save()



def insert_student(request):
    if request.method == 'POST':
        sc = request.POST['sc']  
        sn = request.POST['sn']  # Student name
        si = request.POST['si']  # Student ID

        STO = school.objects.get(SCName=sc)

        STO = student.objects.get_or_create(SCName=STO, Sname=sn, Sid=si)[0]
        STO.save()

        return render(request, 'display_student.html', {'student': STO})

    return render(request, 'insert_student.html')

