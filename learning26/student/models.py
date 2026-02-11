from django.db import models

# Create your models here.
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    #meta class
    class Meta:
        db_table = "student" #table name
    def __str__(self):
        return self.studentName

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    class meta:
        db_table = "product"

class cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "cart"
    def __str__(self):
        return self.product.productName

class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentName    

class category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName
class service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    cateoryid = models.ForeignKey(category,on_delete=models.CASCADE)
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName
    
class userprofile(models.Model):
        userName = models.CharField(max_length=100)
        userEmail = models.EmailField()
        userPassword = models.CharField(max_length=100)
        userPhone = models.CharField(max_length=10)
        userAddress = models.CharField(max_length=100)
        class Meta:
            db_table = "userprofile"
        def __str__(self):
            return self.userName
        
class college(models.Model):
        collegeName = models.CharField(max_length=100)
        collegeCity = models.CharField(max_length=100)
        collegeState = models.CharField(max_length=100)
        collegeCountry = models.CharField(max_length=100)
        class Meta:
            db_table = "college"
        def __str__(self):
            return self.collegeName
        
class department(models.Model):
        departmentName = models.CharField(max_length=100)
        collegeId = models.ForeignKey(college,on_delete=models.CASCADE)
        class Meta:
            db_table = "department"
        def __str__(self):
            return self.departmentName
class subject(models.Model):
        subjectName = models.CharField(max_length=100)
        departmentId = models.ForeignKey(department,on_delete=models.CASCADE)
        class Meta:
            db_table = "subject"
            
        def __str__(self):
            return self.subjectName
        
