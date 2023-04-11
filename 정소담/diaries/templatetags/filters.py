from datetime import datetime, timedelta
from django import template
import calendar

register = template.Library()

@register.filter
def previous_month(value):
    first_day = value.replace(day=1)
    prev_month = (first_day - timedelta(days=1)).replace(day=1)
    return prev_month

@register.filter
def next_month(value):
    days_in_month = calendar.monthrange(value.year, value.month)[1]
    last_day = value.replace(day=days_in_month)
    next_month = (last_day + timedelta(days=1)).replace(day=1)
    return next_month

@register.filter
def format_date(value, format_string='%Y-%m-%d'):
    if isinstance(value, str):
        value = datetime.strptime(value, '%Y-%m-%d')
    return value.strftime(format_string)