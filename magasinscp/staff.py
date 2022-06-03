from flask import url_for, redirect
from flask_admin import AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class HomePageView(BaseView):
    @expose("/")
    def index(self):
        return redirect(url_for("account"))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.admin == True:
            return current_user.is_authenticated


class UserModelView(ModelView):
    def is_accessible(self):
        if current_user.admin == True:
            return current_user.is_authenticated

    can_create = False
    column_exclude_list = "password"
    form_excluded_columns = ["password", "email_confirmed"]


class ItemModelView(ModelView):
    def is_accessible(self):
        if current_user.admin == True:
            return current_user.is_authenticated


class PurchasedItemsModelView(ModelView):
    def is_accessible(self):
        if current_user.admin == True:
            return current_user.is_authenticated
