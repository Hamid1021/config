from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class DateInpup(forms.DateInput):
    input_type = 'date'


class SingUpForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        label="",
        widget=forms.TextInput(
            attrs={"type":"text","class":"input--style-4","placeholder":"نام کاربری را وارد کنید","id":"username"}
        ))

    first_name = forms.CharField(
        max_length=200,
        label="",
        widget=forms.TextInput(
            attrs={"type":"text","class":"input--style-4","placeholder":"نام","id":"first_name"}
        ))

    meli_code = forms.CharField(
        max_length=10,
        label="",
        widget=forms.TextInput(
            attrs={"type":"number","class":"input--style-4","placeholder":"کد ملی","id":"meli_code","pattern":r"[0-9]{10}"}
        ))

    # shenasname_code = forms.CharField(
    #     max_length=10,
    #     label="",
    #     widget=forms.TextInput(
    #         attrs={"type":"text","class":"input--style-4","placeholder":"شماره شناسنامه","id":"shenasname_code"}
    #     ))


    last_name = forms.CharField(
        max_length=200,
        label="",
        widget=forms.TextInput(
            attrs={"type":"text","class":"input--style-4","placeholder":"نام خانوادگی","id":"last_name"}
        ))

    email = forms.CharField(
        max_length=300,
        label="",
        widget=forms.TextInput(
            attrs={"type":"email", "name" : "email", "class":"input--style-4","placeholder":"آدرس ایمیل","id":"email"}
            ))

    GENDER_CHOICES = (
        ("m", "مرد"),
        ("w", "زن"),
        # ("b", "ترجیح می دهم نگویم"),
    )
    gender = forms.CharField(
        label="",
        widget=forms.RadioSelect(
            choices=GENDER_CHOICES,
            attrs={"type":"radio", "id":"gender", "name":"gender"}
        ))

    birthday = forms.DateField(
        label="",
        widget=DateInpup(
            attrs={"type":"date","class":"input--style-4", "id":"birthday"}
            ))

    # password = forms.CharField(
    #     max_length=100,
    #     label="",
    #     widget=forms.TextInput(
    #         attrs={"type":"password","class":"input--style-4","placeholder":"رمز عبور", "id":"password", "name":"password"}
    #     ))
    # password_confirm = forms.CharField(
    #     max_length=100,
    #     label="",
    #     widget=forms.TextInput(
    #         attrs={"type":"password","class":"input--style-4","placeholder":"تایید رمز عبور","id":"password1","name":"C_Password"}
    #     ))

    kode_moarefy = forms.CharField(
        max_length=8,
        label="",
        required = False,
        widget=forms.TextInput(
            attrs={"type":"text","class":"input--style-4", "placeholder":"کد معرف","id":"kode_moarefy"}
        ))

    phone = forms.CharField(
        max_length=11,
        label="",
        widget=forms.TextInput(attrs=(
            {"type":"tel","pattern":r"[0]{1}[9]{1}[0-9]{9}", "class":"input--style-4","placeholder":"شماره همراه","id":"phone"})
        ))

    def clean_kode_moarefy(self):
        kode_moarefy = self.cleaned_data.get("kode_moarefy")
        if not kode_moarefy:
            return kode_moarefy
        userCheck = User.objects.filter(kode_moarefy=kode_moarefy)
        if not userCheck:
            raise forms.ValidationError(
                "کد معرف یافت نشد خالی رها کرده یا اصلاح نمایید")
        return kode_moarefy

    def clean_phone(self):
        phone_number = self.cleaned_data.get("phone")
        userCheck = User.objects.filter(Q(phone_number=phone_number))
        if userCheck:
            raise forms.ValidationError(
                "این شماره همراه قبلا ثبت نام کرده است")
        return phone_number


    def clean_meli_code(self):
        meli_code = self.cleaned_data.get("meli_code")
        userCheck = User.objects.filter(Q(meli_code=meli_code))
        if userCheck:
            raise forms.ValidationError(
                "فردی با این کد ملی ثبت نام کرده است")
        return meli_code


    def clean_email(self):
        email = self.cleaned_data.get("email")
        userCheck = User.objects.filter(Q(email=email))
        if userCheck:
            raise forms.ValidationError(
                "فردی با این ایمیل ثبت نام کرده است")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        userCheck = User.objects.filter(Q(username=username))
        if userCheck:
            raise forms.ValidationError(
                "نام کاربری انتخابی از قبل موجود است دوباره امتحان کنید")
        return username

    # def clean_password_confirm(self):
    #     password = self.cleaned_data.get("password")
    #     password_confirm = self.cleaned_data.get("password_confirm")
    #     if password_confirm != password:
    #         raise forms.ValidationError(
    #             "تکرار رمز عبور صحیح نمی باشد لطفا بررسی نمایید")
    #     else:
    #         return password


class ConfrimSingUpForm(forms.Form):

    code = forms.CharField(
        max_length=6,
        label="",
        widget=forms.TextInput(
            attrs={"type":"number","class":"input--style-4","placeholder":"کد ارسال شده را وارد کنید","id":"code", "name":"code", "max":"999999", "min":"100000",}
        ))




class LoginForm(forms.Form):
    phone_number = forms.CharField(
        max_length=11,
        label="",
        required = False,
        widget=forms.TextInput(attrs=(
            {"type":"tel","pattern":r"[0]{1}[9]{1}[0-9]{9}", "class":"input--style-4","placeholder":"شماره همراه","id":"phone"})
        ))

    email = forms.CharField(
        max_length=300,
        label="",
        required = False,
        widget=forms.TextInput(
            attrs={"type":"email", 'style':"text-transform: lowercase;", "name" : "email", "class":"input--style-4","placeholder":"آدرس ایمیل","id":"email"}
            ))