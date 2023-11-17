from django.db import models

# Create your models here.
class register(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    dob=models.DateField()
    password=models.CharField(max_length=20)

class  image_model(models.Model):
    file_name=models.CharField(max_length=50)
    img=models.FileField(upload_to='djangoapp/static')
    description=models.CharField(max_length=200)
class employee(models.Model):
    ename=models.CharField(max_length=50)
    eid=models.EmailField()
    phone=models.IntegerField()
    cname=models.CharField(max_length=100)
    des=models.CharField(max_length=50)

# product details:product name,price,product_company name,quantity,exp date,description
class product(models.Model):
    pname=models.CharField(max_length=100)
    price=models.IntegerField()
    brand=models.CharField(max_length=100)
    quantity=models.IntegerField()
    exp=models.DateField()
    des=models.CharField(max_length=200)
#
# audioname
# audio
# vd name
# video
# pdf name
# pdf
class fileupload(models.Model):
    audionm=models.CharField(max_length=20)
    aud=models.FileField(upload_to='djangoapp/static')
    vdoname=models.CharField(max_length=20)
    vdo=models.FileField(upload_to='djangoapp/static')
    pdfname=models.CharField(max_length=20)
    pdf=models.FileField(upload_to='djangoapp/static')

class checkbox(models.Model):
    fname=models.CharField(max_length=30)
    choice=[
        ('Kerala',"KERALA"),
        ('Karnataka',"KARNATAKA"),
        ('Tamilnadu',"TAMILNADU")

    ]
    state=models.CharField(max_length=30,choices=choice)
    malay=models.BooleanField(default=False)
    eng=models.BooleanField(default=False)
    hindi=models.BooleanField(default=False)