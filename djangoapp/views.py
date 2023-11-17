import json

from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from  .forms import *
from django.contrib.auth.models import User
# Create your views here.

# first
def first(request):
    return HttpResponse("my first django page")

# second
def second(request):
    return HttpResponse("my second django page")

# render

def third(request):
    return render(request,"third.html")
def fourth(request):
    return  render(request,"djangointro.html")
def registration(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpswd')

        if password==cpassword:
            a=register(fname=fname,lname=lname,username=username,email=email,phone=phone,gender=gender,address=address,dob=dob,password=password)
            a.save()
            return HttpResponse("registration success")
        else:
            return HttpResponse("Password doesn't match!!!")
    return render(request,"reg.html")
# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('eid')
#         password=request.POST.get('password')
#         c=register.objects.all()#model_name.object.all() orm query that is used to fetch a table in our model field
#         for i in c:
#             if(i.email==email and i.password==password):
#                 return HttpResponse("login successfull")
#         else:
#             return HttpResponse("login failed")
#
#     return render(request,"login.html")
def indexpg(request):
    return render(request,"index.html")

def image_uploadd(request):
    if  request.method=='POST':
        flnm=request.POST.get('flname')
        image=request.FILES.get('imgg')
        desc=request.POST.get('des')
        bb=image_model(file_name=flnm,img=image,description=desc)
        bb.save()
        return HttpResponse("file upload success")


    return render(request,"image_upload.html")

def emp_reg(request):
    if request.method=='POST':
        ename=request.POST.get('ename')
        eid=request.POST.get('eid')
        phone=request.POST.get('phone')
        cname=request.POST.get('cname')
        des=request.POST.get('des')



        b = employee(ename=ename, eid=eid, phone=phone, cname=cname, des=des)
        b.save()
        return HttpResponse("registered successfully")


    return render(request,'employee_reg.html')


# employee search
def emp_search(request):
    if request.method=='POST':

        ename=request.POST.get('ename')
        phone=request.POST.get('phone')

        d=employee.objects.all()
        for i in d:
            if(i.ename==ename and int(i.phone)==int(phone)):
                return HttpResponse("Employee found")
        else:
            return HttpResponse("Employee not found")
    return render(request,"search_employee.html")

# product details:product name,price,product_company name,quantity,exp date,description
def product_details(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        price=request.POST.get('price')
        brand=request.POST.get('brand')
        qty=request.POST.get('quantity')
        exp=request.POST.get('exp')
        des=request.POST.get('des')

        e=product(pname=pname,price=price,brand=brand,quantity=qty,exp=exp,des=des)
        e.save()
        return HttpResponse("product added successfully")


    return render(request,"product_details.html")

def product_check(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        brand = request.POST.get('brand')
        f=product.objects.all()
        for i in f:
            if(i.pname==pname and i.brand==brand ):
                return HttpResponse("product found")
        else:
            return HttpResponse("not found")
    return render(request,'product_searches.html')


def fileup_load(request):
    if request.method=='POST':
        adonm=request.POST.get('adonm')
        audio_file=request.FILES.get('ado')
        vdonm=request.POST.get('vdo')
        vdofile=request.FILES.get('vdofile')
        pdfnm=request.POST.get('pdfnm')
        pdf=request.FILES.get('pdf')

        dd=fileupload(audionm=adonm,aud=audio_file,vdoname=vdonm,vdo=vdofile,pdfname=pdfnm,pdf=pdf)
        dd.save()
        return HttpResponse('UPLOAD SUCCESS')
    return render(request,'files_upload.html')

def select_check(request):
    if request.method=='POST':
        fullnm=request.POST.get('fullname')
        state=request.POST.get('state')
        mala=request.POST.get('mala')
        if mala=='on':
            mala=True
        else:
            mala=False
        english=request.POST.get('eng')
        if english=='on':
            english=True
        else:
            english=False
        hindi=request.POST.get('hin')
        if hindi=='on':
            hindi=True
        else:
            hindi=False
        gg=checkbox(fname=fullnm,state=state,malay=mala,eng=english,hindi=hindi)
        gg.save()
        return HttpResponse("Data saved successfully")

    return render(request,"check_select.html")


def display_fun(request):
    a=employee.objects.all()#[(1,arjun,ghj),(2,akhil,ghhj)]
    return render(request,'display.html',{'data':a})



def display_reg(request):
    vv=register.objects.all()
    return render(request,'reg_display.html',{'d':vv})

def image_diaplay(request):
    id=[]
    image=[]
    filename=[]
    description=[]
    l=image_model.objects.all()
    for i in l:
        id1=i.id
        id.append(id1)
        fname=i.file_name
        filename.append(fname)
        im=str(i.img).split('/')[-1]
        image.append(im)
        desc=i.description
        description.append(desc)

    mylist=zip(id,filename,image,description)#[(1,imageee,image.jpeg,blackpink in your area),(2,abc,image2.jpeg,this is my image)]
    return render(request,"image_display.html",{'dd':mylist})

def display_files(request):
    id2=[]
    audio=[]
    audio1=[]
    video=[]
    video1=[]
    pdf=[]
    pdf1=[]
    x=fileupload.objects.all()
    for i in x:
        id3=i.id
        id2.append(id3)
        audii=i.audionm
        audio.append(audii)
        audios=str(i.aud).split('/')[-1]
        audio1.append(audios)
        videoo=i.vdoname
        video.append(videoo)
        vd=str(i.vdo).split('/')[-1]
        video1.append(vd)
        pdff=i.pdfname
        pdf.append(pdff)
        pd=str(i.pdf).split('/')[-1]
        pdf1.append(pd)

    myfile=zip(id2,audio,audio1,video,video1,pdf,pdf1)
    return render(request,"display_file.html",{"data":myfile})


def update_data(request,id):
    a = register.objects.get(id=id)
    if request.method=='POST':

        a.fname=request.POST.get('firstname')
        a.lname=request.POST.get('lastname')
        a.username=request.POST.get('username')
        a.email=request.POST.get('eid')
        a.phone=request.POST.get('phone')
        if str(request.POST.get('gen'))=='female' or str(request.POST.get('gen'))=='male':
            a.gender = request.POST.get('gen')
        else:
            a.save()

        a.address=request.POST.get('address')
        if len(str(request.POST.get('dob')))>0:
            a.dob=request.POST.get('dob')
        else:
            a.save()
        a.save()
        return redirect(display_reg)
    return render(request,"update_profile.html",{'data':a})


def update_emp(request,id):
    bb=employee.objects.get(id=id)
    if request.method=='POST':
        bb.ename=request.POST.get('empname')
        bb.eid=request.POST.get('email')
        bb.phone=request.POST.get('phn')
        bb.cname=request.POST.get('cmp')
        bb.des=request.POST.get('desig')
        bb.save()
        return redirect(display_fun)
    return render(request,'update_employee.html',{'data':bb})


def update_files(request,id):
    z=fileupload.objects.get(id=id)
    audio1=str(z.aud).split('/')[-1]
    video1=str(z.vdo).split('/')[-1]
    pdf2=str(z.pdf).split('/')[-1]

    if request.method=='POST':
        z.audionm=request.POST.get('aname')
        if request.FILES.get('audioo')==None:
            z.save()
        else:
            z.aud=request.FILES.get('audioo')
            z.save()

        z.vdoname=request.POST.get('vname')
        if request.FILES.get('videoo')==None:
            z.save()
        else:
            z.vdo=request.FILES.get('videoo')
            z.save()
        z.pdfname=request.POST.get('pname')
        if request.FILES.get('pdf1')==None:
            z.save()
        else:
            z.pdf = request.FILES.get('pdf1')
            z.save()


        z.save()
        return redirect(display_files)
    return render(request,"update_file.html",{'data':z,'adio':audio1,'vdeo':video1,'pdfa':pdf2})


def image_edit(request,id):
    w=image_model.objects.get(id=id)
    image=str(w.img).split('/')[-1]
    if request.method=='POST':
        w.file_name=request.POST.get('fname')
        if request.FILES.get('imagee')==None:
            w.save()
        else:
            w.img = request.FILES['imagee']
            w.save()

        w.description=request.POST.get('desc')
        w.save()
        return redirect(image_diaplay)
    return render(request,"update_image.html",{'data':w,'img':image})

def delete_reg(request,id):
    a=register.objects.get(id=id)
    a.delete()
    return redirect(display_reg)
def delete_img(request,id):
    j=image_model.objects.get(id=id)
    j.delete()
    return redirect(image_diaplay)
def delete_file(request,id):
    u=fileupload.objects.get(id=id)
    u.delete()
    return redirect(display_files)


def userregistration(request):
    if request.method=='POST':#{'username:anshya, first_name:'anshya'}
        a = userreg(request.POST)
        if a.is_valid():
            uname=request.POST.get('username')#anshya
            fname=request.POST.get('first_name')
            lname=request.POST.get('last_name')
            em=request.POST.get('email')#@anshya@gmail.com
            passw=request.POST.get('password')
            b=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=em,password=passw)
            b.save()
            return HttpResponse('authenticated user')
        else:
            return HttpResponse('user not added')
    else:


           form=userreg()
           print(form)
           return render(request,"user_register.html",{'forms':form})


def userresgis(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']

            if password == confirm:
                # Create a new User instance and set the password using set_password
                user = User(username=username, first_name=first_name, last_name=last_name, email=email)
                user.set_password(password)
                user.save()
                return HttpResponse('Registered successfully')
            else:
                return HttpResponse('Password does not match')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = userform()
        return render(request, 'userregist.html', {'form': form})


def userr_login(request):
    if request.method=='POST':
        form=userlogin(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("login success")
            else:
                return HttpResponse("invalid username or password")
        else:
            return HttpResponse('invalid username or password')
    else:
        return render(request,'log_in.html')


from rest_framework.views import APIView

def  read_response():
    with open(r"C:\Users\User\PycharmProjects\DjangoProject\DjangoProject\djangoapp\movie.json","r",encoding="utf8") as f:
        data=json.load(f)
    return  data

class MyTodos(APIView):
    def get(self,request):
        data=read_response()
        return render(request,'indexing.html',{'data':data})

def read_hotel():
    with open(r"C:\Users\User\PycharmProjects\DjangoProject\DjangoProject\djangoapp\hotel.json","r",encoding="utf8") as h:
        data=json.load(h)
    return data
class HotelViews(APIView):
    def get(self,request):
        data=read_hotel()
        return render(request,"hoteldata.html",{'data':data})

