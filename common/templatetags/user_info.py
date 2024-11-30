from django import template

register = template.Library()


@register.inclusion_tag('common/base.html')
def user_info(user):
    if user.is_authenticated:
        return {
            'username': user.username,
        }
    return {
        'username': None
    }
