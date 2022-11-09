from django.shortcuts import render,redirect
from django.contrib import messages
from app7.forms import Table1Form,LoginForm,UpdateForm
from.models import Table1

# Create your views here.
def index(request):
    return render(request,'index.html')

def show_form(request):
    if request.method=='POST':
        form=Table1Form(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            photo=form.cleaned_data['Photo']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['Confirmpassword']
             
            user=Table1.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'email already exits')
                return redirect('/show_form')
            elif password!=cpassword:
                messages.warning(request,'wrong password')
                return redirect('/show_form')
            else:
                tab=Table1(Name=name,Age=age,Place=place,Email=email,Photo=photo,Password=password)
            tab.save()
            messages.success(request,'data saved')
            return redirect('/')
    else:
        form=Table1Form()
    return render(request,'showform.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            
            user=Table1.objects.get(Email=email)
        if not user:
            messages.warning(request,'Email Does not Exits')
            return redirect('/login')
        elif password!=user.Password:
            messages.warning(request,'Password incorrect')
            return redirect('/login')
        else:
            messages.success(request,'login success')
            return redirect('/home/%s' % user.id)
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})

def home(request,id):
    user=Table1.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def gallery(request):
    igs=Table1.objects.all()
    return render(request,'gallery.html',{'igs':igs})


def detail(request,id):
    data=Table1.objects.get(id=id)
    return render(request,'details.html',{'data':data})

def update(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'data updated')
            return redirect('/home/%s'% user.id,)
    else:
        form=UpdateForm(instance=user)
        return render(request,'update.html',{'form':form,'user':user,'data':data})

