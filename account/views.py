from django.shortcuts import render, redirect, reverse
from account.forms import SingUpForm, ConfrimSingUpForm, LoginForm
from django.contrib.auth import get_user_model, login
from extensions.utils import my_send_sms
from django.views.generic.edit import FormView


from django.db.models import Q
from extensions.utils import Email


from random import randint

User = get_user_model()


def random_number():
    return randint(100000,999999)


class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = 'account:Confrim_User'


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get("phone_number")
            email = form.cleaned_data.get("email")
            error = ("",)
            try:
                user = User.objects.get(Q(phone_number=phone_number)|Q(email=email))

                if user is not None:
                    user.code_send = random_number()
                    user.save()
                    if user.is_active:
                        message = f"سلام کاربر گرامی کد تایید شما برای ادامه فرایند {user.code_send} می باشد با تشکر"
                        if phone_number != "":
                            my_send_sms(message=message, phone="09107647361")
                        if email != "":
                            try:
                                Email.send_mail("کد تایید برای ادامه", [email,], "Emails/send_mail.html", {"d":message})
                                user.email_sended = True
                                user.save()
                            except:
                                print("was't sent")
                                error = ("ایمیل ارسال نشد ... از شماره همراه امتحان نمایید")
                        status = 1
                        return redirect(reverse(self.success_url, kwargs={"custom_user_id": user.custom_user_id, "status":status}))
                    else:
                        error = ("کاربر فعال نیست","از صفحه فعال سازی اقدام نمایید")
                        status = 2

                else:
                    error = ("کاربر وجود ندارد باید ثبت نام کنید",)
            except:
                error = ("کاربر وجود ندارد باید ثبت نام کنید",)

        return render(request, self.template_name, {"form":form,"error":error, 'status':status, "user":user})




class SignUpView(FormView):
    template_name = "registration/sign_up.html"
    form_class = SingUpForm
    success_url = 'account:Confrim_User'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        error = ("",)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            username = form.cleaned_data.get("username")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            gender = form.cleaned_data.get("gender")
            birthday = form.cleaned_data.get("birthday")
            # password = form.cleaned_data.get("password")
            kode_moarefy = form.cleaned_data.get("kode_moarefy")
            meli_code = form.cleaned_data.get("meli_code")
            # shenasname_code = form.cleaned_data.get("shenasname_code")
            phone = form.cleaned_data.get("phone")
            user = User.objects.create_user(phone_number=phone, username=username, first_name=first_name, last_name=last_name, email=email, birthday=birthday, gender=gender, kode_moarefy=kode_moarefy, meli_code=meli_code)
            message = f"سلام کاربر گرامی کد تایید شما برای ادامه فرایند {user.code_send} می باشد با تشکر"

            if my_send_sms(message=message, phone="09107647361", checkid=user.code_send):
                user.email_sended = True
                user.save()
            if email != "":
                try:
                    Email.send_mail("کد تایید برای ادامه", [email,], "Emails/send_mail.html", {"d":message})
                    user.email_sended = True
                    user.save()
                except:
                    print("was't sent")
                    
                status = 1
                return redirect(reverse(self.success_url, kwargs={"custom_user_id": user.custom_user_id,"status":status}))
            else:
                error = ("متاسفانه پیام ارسال نشد دوباره امتحان کنید",)
        return render(request, self.template_name, {'form': form, "error":error})



class ConfrimSingUpView(FormView):
    template_name = "registration/confirm_user_code.html"
    form_class = ConfrimSingUpForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        error = ("پیامی برای شما ارسال نشده است",)
        form = self.form_class(request.POST)

        global custom_user_id
        global status

        custom_user_id = kwargs["custom_user_id"]
        status = kwargs["status"]

        user = User.objects.get(custom_user_id=custom_user_id)

        if status != 2:
            if form.is_valid():
                code = form.cleaned_data.get("code")
                if user.email_sended:
                    if int(code) == user.code_send:
                        user.is_active = True
                        user.save()
                        login(request, user)
                        return redirect(self.success_url)
                    else:
                        error = ("کد ارسالی صحیح نیست لطفا مجددا بررسی نمایید", )

        elif status == 2:
            user = User.objects.get(custom_user_id=custom_user_id)
            message = f"سلام کاربر گرامی کد تایید شما برای ادامه فرایند {user.code_send} می باشد با تشکر"
            email = user.email
            error = ("اطلاعات ورود و فعال سازی به شما ارسال گردید به وسیله فیلد بالا اقدام نمایید",)

            if my_send_sms(message=message, phone=user.phone_number, checkid=user.code_send):
                user.email_sended = True
                user.save()
                status = 1

            if email != "":
                try:
                    Email.send_mail("کد تایید برای ادامه", [email,], "Emails/send_mail.html", {"d":message})
                    user.email_sended = True
                    user.save()
                    status = 1
                except:
                    print("was't sent")
            else:
                error = ("متاسفانه پیام ارسال نشد دوباره امتحان کنید",)
            if form.is_valid():
                code = form.cleaned_data.get("code")
                if user.email_sended:
                    if int(code) == user.code_send:
                        user.is_active = True
                        user.save()
                        login(request, user)
                        return redirect(self.success_url)
                    else:
                        error = ("کد ارسالی صحیح نیست لطفا مجددا بررسی نمایید", )

        context = {'form': form, "error": error, "status":status}
        return render(request, self.template_name, context)


# class ResentCode(FormView):
#     template_name = "registration/confirm_user_code.html"
#     success_url = 'account:Confrim_User'


#     def get(self, request, *args, **kwargs):
#     	user = User.objects.get(custom_user_id=kwargs["custom_user_id"])
#     	form = self.form_class(request.POST)
#     	time_resent = user.resend_time + timedelta(minutes = 2)
#     	if time_resent > datetime.now():
#     		access = False

#     		return redirect(reverse(self.success_url, kwargs={"custom_user_id": user.custom_user_id}))
#     	else:
#     		access = True

#     		return redirect(reverse(self.success_url, kwargs={"custom_user_id": user.custom_user_id}))


#     	return render(request, self.template_name, {'form': form, "access": access})
