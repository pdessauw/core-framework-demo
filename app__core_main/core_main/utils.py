from django.shortcuts import render as django_render


def render(request, template_name, context):
    """ Rendering function

    :param request:
    :param template_name:
    :param context:

    :return:
    """
    context["template"] = template_name

    return django_render(request, "core_main/app_wrapper.html", context)
