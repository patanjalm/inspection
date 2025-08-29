# inspection/urls.py
from django.urls import path
from .views import RegisterUser, LoginUser,ProjectList,UserApprovalList
from .views import *

urlpatterns = [
    path("registerUser/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("projectList/", ProjectList.as_view(), name="projectList"),
    path("addProject/", AddProject.as_view(), name="addProject"),
    path("userApprovalList/", UserApprovalList.as_view(), name="userApprovalList"),
    path("activateUser/", ActivateUser.as_view(), name="activateUser"),
    path("assignProjectToAdmin/", AssignProjectToAdmin.as_view(), name="assignProjectToAdmin"),
    path("adminProjectfilter/", AdminProjectfilter.as_view(), name="adminProjectfilter"),
    path("uploadTaskImage/", UploadTaskImage.as_view(), name="uploadTaskImage"),
    path("getTaskDetails/", GetTaskDetails.as_view(), name="getTaskDetails"),
    path("getHomeTask/", GetHomeTask.as_view(), name="getHomeTask"),
    path("deleteTask/", DeleteTask.as_view(), name="deleteTask"),
    path("getUserHomeTask/", GetUserHomeTask.as_view(), name="getUserHomeTask"),
    path("addTag/", AddTag.as_view(), name="addTag"),
    path("deleteTag/", DeleteTag.as_view(), name="deleteTag"),
]
