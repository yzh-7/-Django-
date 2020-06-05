from django.urls import path,re_path
from django.conf.urls import url
from . import views
from BS.settings import DEBUG,MEDIA_ROOT      #引入settings里的函数，实现照片显示

urlpatterns = [
    #前台
    path('',views.welcome,name = "欢迎"),
    path('home/',views.home,name="主页"),
    path('register/',views.register,name="注册"),
    path('login/',views.login,name="登录"),
    path('userLogin/',views.logout,name="注销登录"),
    path('myorder/',views.myorder,name="我的订单"),
    url(r'^myordermsg',views.myordermsg),
    path('changepwd/',views.changepwd,name="修改密码"),
    url(r'^newpassword/',views.cpwd),
    path('movein/',views.movein,name="入住"),
    url(r'^moveinmsg',views.moveinmsg),
    path('dinner/',views.dinner,name="点餐"),
    url(r'^dinnermsg',views.dinnermsg),
    path('choosetable/',views.choosetable,name="选桌"),
    url(r'^choosetablemsg/',views.choosetablemsg),
    path('bdmap/',views.bdmap,name="地图"),
    path('leacots/',views.leacotsPage,name="留言"),
    url(r'^leacot/', views.s_leacotsPage),#表单提交数据
    re_path(r'^del_l/(?P<del_l>\d+)/', views.del_ls),#删除留言
    path('notice/',views.notice,name="公告"),

    #后台
    path('adminlogin/',views.adminlogin,name="管理员登录"),
    path('usermanage/',views.usermanage,name="用户管理"),
    re_path(r'usermanage/(\d+)/change',views.userinfo_change),
    re_path(r'usermanage/(\d+)/delete',views.userinfo_delete),

    path('moveinmanage/',views.moveinmanage,name="入住管理"),
    re_path(r'moveinmanage/(\d+)/change', views.moveininfo_change),
    re_path(r'moveinmanage/(\d+)/delete', views.moveininfo_delete),

    path('roommanage/',views.roommanage,name="客房管理"),
    re_path(r'roommanage/(\d+)/change', views.roominfo_change),
    re_path(r'roommanage/(\d+)/delete', views.roominfo_delete),
    path('addroom/',views.addroom,name="添加客房"),
    #客房类型管理

    path('dinnermanage/',views.dinnermanage,name="菜品管理"),
    re_path(r'dinnermanage/(\d+)/change', views.dinnerinfo_change),
    re_path(r'dinnermanage/(\d+)/delete', views.dinnerinfo_delete),
    path('adddish/',views.adddish,name="添加菜品"),

    path('tablemanage/',views.tablemanage,name="餐桌管理"),
    re_path(r'tablemanage/(\d+)/change', views.tableinfo_change),
    re_path(r'tablemanage/(\d+)/delete', views.tableinfo_delete),
    path('addtable/',views.addtable,name="添加餐桌"),

    path('paymanage/',views.paymanage,name="消费管理"),

    path('noticemanage/',views.noticemanage,name="公告管理"),
    path('noticecreate/',views.noticecreate,name="公告创建"),
    re_path(r'noticemanage/(\d+)/change', views.noticeinfo_change),
    re_path(r'noticemanage/(\d+)/delete', views.noticeinfo_delete),

    path('userLeacots/',views.userLeacots,name="用户留言"),

]

#照片显示
from django.views.static import serve
if DEBUG:
    urlpatterns += url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),