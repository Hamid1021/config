from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import date
import uuid
from django.apps import apps
from django.contrib.auth.hashers import make_password

from random import randint
from django.utils import timezone
from image_optimizer.fields import OptimizedImageField

from area.models import Ostan, Shahrestan, Bakhsh, Dehestan

from extensions.utils import jalali_converter
class CustomUserManager(UserManager):

    def get_moaref(self, kode_moarefy):
        """get user with kode_moarefy"""
        try:
            user = self.get(kode_moarefy=kode_moarefy)
            return user
        except:
            pass

    @classmethod
    def check_full_int(self, phone_number):
        phone = phone_number
        try:
            phone = int(phone)
            return False
        except:
            return True

    @classmethod
    def checking_phone_number(cls, phone_number):
        """
        checking phone number the phone_number checking contains 0 and 9 in the start.
        """
        phone_number = phone_number or ''

        if phone_number[0] != "0":
            return 0
        elif phone_number[1] != "9":
            return 1
        elif len(phone_number) > 11:
            return 2
        elif cls.check_full_int(phone_number):
            return 3
        else:
            return phone_number

    def _create_user(self, phone_number, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not phone_number:
            raise ValueError('The given username must be set')

        phone_number = self.checking_phone_number(phone_number)

        if phone_number == 0:
            raise ValueError('The given phone_number must start with 0')
        elif phone_number == 1:
            raise ValueError(
                'The given phone_number index 1 must start with 9')
        elif phone_number == 2:
            raise ValueError('The given phone_number character must be 11')
        elif phone_number == 3:
            raise ValueError('The given phone_number character must be integer')
            
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(
            username=username, phone_number=phone_number, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


        
    def generate_ranint(self):
        return randint(100000,999999)



    def create_user(self,phone_number, username, email=None, password=None, kode_moarefy=None, ** extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # str(uuid.uuid4())[-1:8:-1] is a 24 random character
        extra_fields.setdefault('custom_user_id', str(uuid.uuid4())[:11:-1])
        extra_fields.setdefault('kode_moarefy', str(uuid.uuid4())[:8])
        extra_fields.setdefault('gender', "m")
        extra_fields.setdefault('ozv_faal', False)
        extra_fields.setdefault('moshaver', False)
        extra_fields.setdefault('naeb_moodir', False)
        extra_fields.setdefault('dabir', False)
        extra_fields.setdefault('modir', False)
        extra_fields.setdefault('pass_per_save', password or "")
        extra_fields.setdefault('code_send', self.generate_ranint())
        extra_fields.setdefault('email_sended', False)
        if kode_moarefy != None:
            extra_fields.setdefault('moaref', self.get_moaref(kode_moarefy))
        return self._create_user(phone_number, username, email, password, **extra_fields)


    def _create_super_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_super_user(username, email, password, **extra_fields)

class User(AbstractUser):
    ostan = models.ForeignKey(
        Ostan, on_delete=models.SET_NULL, verbose_name="استان", null=True, blank=True)
    shahrestan = models.ForeignKey(
        Shahrestan, on_delete=models.SET_NULL, verbose_name="شهرستان", null=True, blank=True)
    bakhsh = models.ForeignKey(
        Bakhsh, on_delete=models.SET_NULL, verbose_name="بخش", null=True, blank=True)
    dehestan = models.ForeignKey(
        Dehestan, on_delete=models.SET_NULL, verbose_name="دهستان", null=True, blank=True)

    image = OptimizedImageField(
        upload_to='images',
        optimized_image_output_size=(540,540),
        optimized_image_resize_method='thumbnail'  # 'thumbnail', 'cover' or None
    ,null=True, blank=True, verbose_name="تصویر پروفایل", default="None.jpg")
    kode_moarefy = models.CharField(
        verbose_name="کد معرفی", max_length=8, null=True, blank=True)
    moaref = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name="معرف", null=True, blank=True)
    modir = models.BooleanField(
        default=False, verbose_name="رئیس کل", blank=True, null=True)
    dabir = models.BooleanField(
        default=False, verbose_name="دبیر", blank=True, null=True)
    naeb_moodir = models.BooleanField(
        default=False, verbose_name="نائب رئیس", blank=True, null=True)
    moshaver = models.BooleanField(
        default=False, verbose_name="مشاور", blank=True, null=True)
    ozv_faal = models.BooleanField(
        default=False, verbose_name="عضو فعال", blank=True, null=True)
    birthday = models.DateField(
        verbose_name="تاریخ تولد", default=date.today, null=True, blank=True)
    pass_per_save = models.CharField(
        verbose_name="گذر واژه هش نشده", max_length=128, blank=True)

    GENDER_CHOICES = (
        ("m", "مرد"),
        ("w", "زن"),
        ("b", "ترجیح می دهم نگویم"),
    )
    gender = models.CharField(
        verbose_name="جنسیت", max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    phone_number = models.CharField(
        verbose_name="شماره همراه", max_length=11, null=True, blank=True, unique=True)
    meli_code = models.CharField(
        verbose_name="شماره ملی", max_length=10, null=True, blank=True, unique=True)
    shenasname_code = models.CharField(
        verbose_name="شماره شناسنامه", max_length=10, null=True, blank=True, unique=True)
    custom_user_id = models.CharField(
        verbose_name="کد اختصاصی کاربر", max_length=24, null=True, blank=True, unique=True)
    code_send = models.IntegerField(
        verbose_name="کد ارسال شده", null=True, blank=True)
    email_sended = models.BooleanField(
        default=False, verbose_name="ایمیل ارسال شده است")
    resend_time = models.DateTimeField(
        verbose_name="زمان ارسال", default=timezone.now, null=True, blank=True)

    objects = CustomUserManager()

    def jbirthday(self):
        return jalali_converter(self.created)
    jbirthday.short_description = "تاریخ تولذ"
