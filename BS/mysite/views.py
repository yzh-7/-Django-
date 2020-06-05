from django.shortcuts import render,redirect,HttpResponse,reverse
from mysite import models
# Create your views here.
#欢迎
def welcome(request):
    return render(request,'userLogin/welcome.html')
#主页
def home(request):
    username = request.session.get('username','未登录')#登录是否成功标志位
    return render(request,'home.html',locals())

#注册
def register(request):
    # 获取数据库用户表信息
    userList = models.UserInfo.objects.all()
    if request.method =="POST":
        #获取用户名，电话，身份证，密码
        username = request.POST['username']
        telephone = request.POST['telephone']
        sfzid = request.POST['sfzid']
        userpwd = request.POST['userpwd']
        print(username,telephone,sfzid,userpwd)
        try:
            userList.create(username=username,telephone=telephone,sfzid=sfzid,userpwd=userpwd)
            return redirect('/login/')
        except:
           err = "注册失败"
        return render(request,'userLogin/register.html',{"errTip":err})
    else:
        return render(request,'userLogin/register.html')

#登录
def login(request):
    if request.method == "POST":
        # 获取数据库用户表信息
        userList = models.UserInfo.objects.all()
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
        for u in userList:
            if u.username == username and u.userpwd == userpwd:
                request.session['username'] = username
                request.session['userpwd'] = userpwd
                request.session.set_expiry(0)
                return redirect('/home/',locals())

        #错误提示
        err = "用户名或是密码错误"
        return render(request,'userLogin/login.html',{"errTip":err})
    else:
        return render(request,'userLogin/login.html')

#注销登录
def logout(request):
    request.session.flush()
    return redirect(reverse('主页'))
    # return render(request,'userLogin/goodbye.html')

#修改密码
def changepwd(request):
    try:
        username = request.session['username']
        return render(request,'userLogin/changepwd.html')
    except:
        return redirect('/login/')

def cpwd(request):
    username = request.session['username']
    pwd1 = request.POST['password1']
    pwd2 = request.POST['password2']
    if pwd1 == pwd2:
        userList = models.UserInfo.objects.all()
        for u in userList:
            if u.username == username:
                models.UserInfo.objects.filter(username=username).update(userpwd=pwd2)
                return render(request,'home.html', locals())
    else:
        err = "两次密码不相同"
        return render(request,'userLogin/changepwd.html',{"errTip":err})

#我的订单(未完成)
def myorder(request):
    try:
        username = request.session['username']
        moveinList = models.MoveinInfo.objects.filter(username=username)
        return render(request,'userLogin/myorder.html',locals())
    except:
        return redirect('/login/')
#退订
def myordermsg(request):
    m = models.MoveinInfo.objects.all()
    if request.method == "POST":
        id = request.POST.get("order_id")
        # models.MoveinInfo.objects.filter(id=id).update(roomstatus=0,username=None)
        models.MoveinInfo.objects.filter(id=id).delete()
        return redirect('/home/')




#入住
def movein(request):
    try:
        username = request.session['username']
        moveinList = models.MoveinInfo.objects.all()
        return render(request,'userLogin/movein.html',locals())
    except:
        return redirect('/login/')

def moveinmsg(request):
    moveinList = models.MoveinInfo.objects.all()
    if request.method == "POST":
        username = request.session['username']
        id = request.POST.get('room_id')
        predate = request.POST.get('predate')
        #movein_time = request.POST.get('movein_time')#获取当前时间
        print(username,id,predate)
        id = int(id)
        for u in moveinList:
            print(u)
            print(type(u.roomstatus))
            if u.id == id:
                moveinList.filter(id=id).update(username=username,predate=predate,roomstatus=1)
        return redirect('/movein/',locals())
    # else:
    #     #     return redirect('/movein/',locals())



#点餐
def dinner(request):
    try:
        username = request.session['username']
        dishList = models.DishInfo.objects.all()
        return render(request, 'userLogin/dinner.html',locals())
    except:
        return redirect('/login/')

def dinnermsg(request):
    dishList = models.DishInfo.objects.all()
    if request.method == "POST":
        username = request.session['username']
        id = request.POST.get('dish_id')
        dishnumber= request.POST.get('dishnumber')
        id = int(id)
        for d in dishList:
            if d.id == id:
                dishList.filter(id=id).update(username=username,dishnumber=dishnumber)
        return redirect('/dinner/',locals())
    else:
        return redirect('/dinner/',locals())

#选桌
def choosetable(request):
    try:
        username = request.session['username']
        tableList = models.TableInfo.objects.all()
        return render(request,'userLogin/choosetable.html',locals())
    except:
        return redirect('/login/')

def choosetablemsg(request):
    tableList = models.TableInfo.objects.all()
    if request.method =="POST":
        username = request.session['username']
        id = request.POST.get('table_id')
        tablestatus = request.POST.get('table_status')
        id = int(id)
        for t in tableList:
            if t.id == id:
                tableList.filter(id=id).update(username=username,tablestatus =1)
        return redirect('/choosetable/', locals())
    else:
        return redirect('/choosetable/', locals())

#地图
def bdmap(request):
    return render(request,'userLogin/bdmap.html')

#留言
def leacotsPage(request):
    max_leacots = 0
    try:
        username = request.session['username']
        list = models.UserLeacots.objects.all()
        for u in list:
            if u.id > max_leacots:
                max_leacots = u.id
        return render(request, 'userLogin/leacots.html',locals())
    except:
        return render(request,'userLogin/login.html')

def s_leacotsPage(request):
    #或者  username = request.POST.get('username')
    max_leacots = 0
    username = request.session['username']
    leacot = request.POST['desc']
    #测试值是否获取到
    print(username,leacot)
    #把值存到数据库
    try:
        try:
            models.UserLeacots.objects.create(name = username,leacots = leacot)
            print("创建成功")
            list = models.UserLeacots.objects.all()
            for u in list:
                if u.id>max_leacots:
                    max_leacots = u.id
            return render(request, 'userLogin/leacots.html', locals())
        except:
            print("创建失败")
            list = models.UserLeacots.objects.all()
            return render(request,'userLogin/leacots.html',locals())
    except:
        err = "留言失败"
        return render(request,'userLogin/leacots.html',{'errTip':err})
#删除留言
def del_ls(request,del_l):
    try:
        del_u = int(del_l)
        username = request.session['username']
        lists = models.UserLeacots.objects.all()
        for u in lists:
            if u.id==del_u:
                models.UserLeacots.objects.filter(id=u.id).delete()
                list = models.UserLeacots.objects.all()
                print('删除成功')
                return render(request,'userLogin/leacots.html',locals())
    except:
        return HttpResponse("失败")




#公告
def notice(request):
    try:
        username = request.session['username']
        notice_info = models.NoticeInfo.objects.all()
        return render(request,'userLogin/notice.html',locals())
    except:
        return redirect('/login/')



#-----------------------------后台-----------------------------#
#管理员登录
def adminlogin(request):
    if request.method == "POST":
        # 获取数据库用户表信息
        adminList = models.AdminInfo.objects.all()
        name = request.POST.get('adminname')
        pwd = request.POST.get('adminpwd')
        for a in adminList:
            if a.adminname == name and a.adminpwd == pwd:
                return redirect('/usermanage/',locals())
    return render(request,'admin/adminlogin.html')

#用户管理---------------------------------------------------------------------------------------------------------------
def usermanage(request):
    userList = models.UserInfo.objects.all()
    return render(request,'admin/usermanage.html',locals())
#删除用户
def userinfo_delete(request,id):
    request.session.flush()
    models.UserInfo.objects.filter(id=id).delete()
    return redirect('/usermanage/')
#修改用户
def userinfo_change(request,id):
    user_this = models.UserInfo.objects.filter(id=id).first()
    if request.method =="POST":
        username = request.POST['username']
        telephone = request.POST['telephone']
        sfzid = request.POST['sfzid']
        userpwd = request.POST['userpwd']
        models.UserInfo.objects.filter(id=id).update(username=username,telephone=telephone,sfzid=sfzid,userpwd=userpwd)
        return redirect('/usermanage/')
    return render(request,'admin/userinfo_change.html',locals())

#入住管理---------------------------------------------------------------------------------------------------------------
def moveinmanage(request):
    movein_this = models.MoveinInfo.objects.all()
    return render(request,'admin/moveinmanage.html',locals())
#入住信息删除
def moveininfo_delete(request,id):
    models.MoveinInfo.objects.filter(id=id).delete()
    return redirect('/moveinmanage/')
#入住信息修改
def moveininfo_change(request,id):
    moveininfo_this = models.MoveinInfo.objects.filter(id=id).first()
    if request.method =="POST":
        username = request.POST['username']
        predate = request.POST['predate']
        roomstatus = request.POST.get('roomstatus')
        # predate = request.POST['predate']
        models.MoveinInfo.objects.filter(id=id).update(id=id,predate=predate,roomstatus=roomstatus)
        return redirect('/moveinmanage/')
    return render(request, 'admin/moveininfo_change.html', locals())


#客房管理---------------------------------------------------------------------------------------------------------------
def roommanage(request):
    room_this = models.MoveinInfo.objects.all()
    return render(request,'admin/roommanage.html',locals())
#添加客房
def addroom(request):
    if request.method =="POST":
        roomtype = request.POST.get('roomtype')
        roomspace = request.POST.get('roomspace')
        roomprice = request.POST.get('roomprice')
        roomphoto = request.FILES.get('roomphoto')
        models.MoveinInfo.objects.create(roomtype=roomtype,roomspace=roomspace,roomprice=roomprice,roomphoto=roomphoto)
        return redirect('/roommanage/',locals())
    return render(request,'admin/addroom.html',locals())
#客房删除
def roominfo_delete(request,id):
    models.MoveinInfo.objects.filter(id=id).delete()
    return redirect('/roommanage/')
#客房修改
def roominfo_change(request,id):
    roominfo_this = models.MoveinInfo.objects.filter(id=id).first()
    if request.method =="POST":
        roomtype = request.POST.get('roomtype')
        roomspace = request.POST.get('roomspace')
        roomprice = request.POST.get('roomprice')
        # roomphoto = request.FILES.get('roomphoto')
        # roomstatus = request.POST.get('roomstatus')
        models.MoveinInfo.objects.filter(id=id).update(roomtype=roomtype,roomspace=roomspace,roomprice=roomprice)
        return redirect('/roommanage/',locals())
    return render(request,'admin/roominfo_change.html',locals())

#客房类型管理-----------------------------------------------------------------------------------------------------------


#菜品管理---------------------------------------------------------------------------------------------------------------
def dinnermanage(request):
    dinner_this = models.DishInfo.objects.all()
    return render(request,'admin/dinnermanage.html',locals())
#菜品添加
def adddish(request):
    if request.method =="POST":
        dishname = request.POST.get('dishname')
        dishprice = request.POST.get('dishprice')
        dishphoto = request.FILES.get('dishphoto')
        dishflavor = request.POST.get('dishflavor')
        models.DishInfo.objects.create(dishname=dishname,dishprice=dishprice,dishphoto=dishphoto,dishflavor=dishflavor)
        return redirect('/dinnermanage/',locals())
    return render(request,'admin/adddish.html',locals())

#菜品删除
def dinnerinfo_delete(request,id):
    models.DishInfo.objects.filter(id=id).delete()
    return redirect('/dinnermanage/')
#菜品修改
def dinnerinfo_change(request,id):
    dinnerinfo_this = models.DishInfo.objects.filter(id=id).first()
    if request.method == "POST":
        dishname = request.POST['dishname']
        dishprice = request.POST['dishprice']
        dishflavor = request.POST.get('dishflavor')
        # predate = request.POST['predate']
        models.DishInfo.objects.filter(id=id).update(dishname=dishname,dishprice=dishprice,dishflavor=dishflavor)
        return redirect('/dinnermanage/')
    return render(request,'admin/dinnerinfo_change.html',locals())

#餐桌管理---------------------------------------------------------------------------------------------------------------
def tablemanage(request):
    table_this = models.TableInfo.objects.all()
    return render(request,'admin/tablemanage.html',locals())
#添加餐桌
def addtable(request):
    if request.method == "POST":
        tablenumber = request.POST.get('tablenumber')
        tablestatus = request.POST.get('tablestatus')
        models.TableInfo.objects.create(tablenumber=tablenumber,tablestatus=tablestatus)
        return redirect('/tablemanage/', locals())
    return render(request,'admin/addtable.html')
#餐桌删除
def tableinfo_delete(request,id):
    models.TableInfo.objects.filter(id=id).delete()
    return redirect('/tablemanage/')
#餐桌修改
def tableinfo_change(request,id):
    tableinfo_this = models.TableInfo.objects.filter(id=id).first()
    if request.method == "POST":
        username = request.POST.get('username')
        models.TableInfo.objects.filter(id=id).update(username=username)
        return redirect('/tablemanage/')
    return render(request,'admin/tableinfo_change.html',locals())


#消费管理---------------------------------------------------------------------------------------------------------------
def paymanage(request):
    return render(request,'admin/paymanage.html')

#公告管理---------------------------------------------------------------------------------------------------------------
def noticemanage(request):
    notice_this = models.NoticeInfo.objects.all()
    return render(request,'admin/noticemanage.html',locals())
#公告创建
def noticecreate(request):
    if request.method =="POST":
        time = request.POST.get('noticetime')
        content = request.POST.get('noticecontent')
        models.NoticeInfo.objects.create(noticetime=time,noticecontent=content)
        return redirect('/noticemanage/', locals())
    return render(request,'admin/noticecreate.html')
#公告删除
def noticeinfo_delete(request,id):
    models.NoticeInfo.objects.filter(id=id).delete()
    return redirect('/noticemanage/')
#公告修改
def noticeinfo_change(request,id):
    noticeinfo_this = models.NoticeInfo.objects.filter(id=id).first()
    if request.method == "POST":
        time = request.POST.get('noticetime')
        content = request.POST.get('noticecontent')
        models.NoticeInfo.objects.filter(id=id).update(noticetime=time,noticecontent=content)
        return redirect('/noticemanage/')
    return render(request,'admin/noticeinfo_change.html',locals())


#用户留言
def userLeacots(request):
    userLeacots_this = models.UserLeacots.objects.all()
    return render(request,'admin/userLeacots.html',locals())
