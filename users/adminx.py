import xadmin
from .models import Admin,UserProfile,UserCourse,Grade,Course,Teacher
from xadmin import views



class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "北网课程管理后台"
    site_footer = "Powered By chris - 2020"
    menu_style = "accordion"


class AdminAdmin(object):
    list_display =["admin_login","Permission"]
    search_fields = ['admin_login']
    list_filter = ['admin_login']


class UserCourseAdmin(object):
    list_display =["user","course","add_time"]
    search_fields = ["user","course"]
    list_filter = ["user","course"]

class GradeAdmin(object):
    list_display =["grade","user"]
    search_fields = ["grade","user"]
    list_filter = ["grade","user"]

class CourseAdmin(object):
    list_display =["no","name","desc","type","time","teacher"]
    search_fields = ["no","name","desc","type","time","teacher"]
    list_filter = ["no","name","desc","type","time","teacher"]

class TeacherAdmin(object):
    list_display =["name"]
    search_fields = ["name"]
    list_filter = ["name"]

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(Admin,AdminAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Grade,GradeAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
