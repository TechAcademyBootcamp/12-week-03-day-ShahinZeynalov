from django.template import Library,Template
from datetime import datetime
register = Library()


print(dir(register))
# @register.filter
# def find_date(value):
#     now = datetime.now().strftime('%Y/%d')
#     return value.split('-')[1]
