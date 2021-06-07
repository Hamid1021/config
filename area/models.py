from django.db import models

# Create your models here.


class Ostan(models.Model):
    title = models.CharField(verbose_name="نام استان",
                             max_length=200, null=True, blank=True)
    position = models.IntegerField(
        auto_created=True, verbose_name="موقعیت", unique=True)
    active = models.BooleanField(default=True, verbose_name="وضعیت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "استان "
        verbose_name_plural = "استان ها"
        db_table = 'ostan_item'
        ordering = ['position', ]


class Shahrestan(models.Model):
    title = models.CharField(verbose_name="نام استان",
                             max_length=200, null=True, blank=True)
    position = models.IntegerField(
        auto_created=True, verbose_name="موقعیت", unique=True)
    active = models.BooleanField(default=True, verbose_name="وضعیت")
    ostan = models.ForeignKey(
        Ostan, on_delete=models.SET_NULL, verbose_name="استان", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "شهرستان"
        verbose_name_plural = "شهرستان ها"
        db_table = 'shahrestan_item'
        ordering = ['position', ]


class Bakhsh(models.Model):
    title = models.CharField(verbose_name="نام استان",
                             max_length=200, null=True, blank=True)
    position = models.IntegerField(
        auto_created=True, verbose_name="موقعیت", unique=True)
    active = models.BooleanField(default=True, verbose_name="وضعیت")
    shahrestan = models.ForeignKey(
        Shahrestan, on_delete=models.SET_NULL, verbose_name="شهرستان", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بخش"
        verbose_name_plural = "بخش ها"
        db_table = 'bakhsh_item'
        ordering = ['position', ]


class Dehestan(models.Model):
    title = models.CharField(verbose_name="نام استان",
                             max_length=200, null=True, blank=True)
    position = models.IntegerField(
        auto_created=True, verbose_name="موقعیت", unique=True)
    active = models.BooleanField(default=True, verbose_name="وضعیت")
    bakhsh = models.ForeignKey(
        Bakhsh, on_delete=models.SET_NULL, verbose_name="بخش", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دهستان"
        verbose_name_plural = "دهستان ها"
        db_table = 'dehestan_item'
        ordering = ['position', ]
