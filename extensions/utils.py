from extensions import jalali, ghasedak
from django.utils import timezone

from django.conf import settings

from django.core.mail import send_mail as send
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Email:

	@staticmethod
	def send_mail(subject, to, template, context):
		html_message = render_to_string(template, context)
		message = strip_tags(html_message)
		send(subject, message, None, to, html_message=html_message)


def my_send_sms(message, phone, linenumber=None, checkid=None):
	sms = ghasedak.Ghasedak(settings.SEND_SMS_KEY)
	sms_content = {'message':str(message),'receptor':
	str(phone),'linenumber' : "10008566",}
	if linenumber != None:
		sms_content["linenumber"] = linenumber
	if checkid != None:
		sms_content["checkid"] = checkid
	return sms.send(sms_content)


def persian_numbers_converter(string):
	numbers = {
	"0":"۰",
	"1":"۱",
	"2":"۲",
	"3":"۳",
	"4":"۴",
	"5":"۵",
	"6":"۶",
	"7":"۷",
	"8":"۸",
	"9":"۹",
	}

	for e, p in numbers.items():
		string = string.replace(e, p)

	return string

def jalali_converter(time):
	time = timezone.localtime(time)
	jmonth = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند",]
	time_to_str = f"{time.year},{time.month},{time.day}"
	time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

	output = f"{time_to_tuple[2]} {jmonth[time_to_tuple[1]-1]} {time_to_tuple[0]} ، ساعت  \
	{time.hour}:{time.minute}"
	return persian_numbers_converter(output)
