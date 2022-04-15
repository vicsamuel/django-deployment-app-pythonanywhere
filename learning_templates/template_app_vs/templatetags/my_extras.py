from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    '''
    This cuts out all values of "arg" from the string!
    '''
    return value.replace(arg,'')

# Pass in the name of what you want to call the filter and then pass in the actual filter name
# Can use register or the other way of registering using decorators -- review decorator lesson
register.filter('cut',cut)