from django.db import models

# Create your models here.
#用户信息表
class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='用户ID')
    username = models.CharField(unique=True,max_length=50,verbose_name='用户名')
    telephone = models.CharField(max_length=50,verbose_name='手机号')
    sfzid = models.CharField(max_length=50,verbose_name='身份证')
    userpwd = models.CharField(max_length=50,verbose_name='密码')

    def __str__(self):
        return self.username
    # class Meta:
    #     verbose_name = "用户信息表"
    #     verbose_name_plural = "用户信息表"

#用户留言表
class UserLeacots(models.Model):
    # post = models.ForeignKey(primary_key=True, related_name='用户ID')
    id = models.IntegerField(unique=False, primary_key=True, verbose_name='用户ID')
    name = models.CharField(unique=False,max_length=50, verbose_name='用户名')
    leacots = models.CharField(max_length=500, verbose_name='留言')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['-c_time']
    #     verbose_name = '留言'
    #     verbose_name_plural = verbose_name

#入住信息表
class MoveinInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=False,max_length=50)
    roomtype = models.CharField(max_length=50)
    roomspace = models.CharField(max_length=50)
    roomprice = models.CharField(max_length=50)
    predate = models.CharField(max_length=50)
    #照片添加
    roomphoto = models.ImageField(upload_to='imgs')
    roomstatus = models.IntegerField(default=0)
    #roommate = models.CharField(max_length=30)

    movein_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'MoveinInfo:%s'%self.username
    # def __str__(self):
    #     return self.username
    #
    # class Meta:
    #     ordering = ['-predate']
#菜品信息表
class DishInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=False,max_length=50)
    dishname = models.CharField(max_length=50)
    dishflavor = models.CharField(max_length=50)
    dishprice = models.CharField(max_length=50)
    dishnumber = models.CharField(max_length=50)
    dishphoto = models.ImageField(upload_to='imgs')

    def __str__(self):
        return self.username

#餐桌信息表
class TableInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=False,max_length=50)
    tablenumber = models.IntegerField(max_length=30)
    tablestatus = models.IntegerField(max_length=30)

    def __str__(self):
        return self.username

class AdminInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    adminname = models.CharField(max_length=30)
    adminpwd = models.CharField(max_length=30)

    def __str__(self):
        return self.adminname

class NoticeInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    noticetime = models.DateField(auto_now_add=True)
    noticecontent = models.CharField(max_length=100)

    def __str__(self):
        return self.noticecontent