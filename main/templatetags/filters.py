from django import template

register = template.Library()

@register.filter
def colorize(number, arg):
    return (120-(120/number)*arg)

