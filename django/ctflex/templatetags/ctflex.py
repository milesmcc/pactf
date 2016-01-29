from django.core.urlresolvers import reverse
from django import template

from ctflex.models import Window
from ctflex import queries


register = template.Library()


@register.filter(is_safe=True, name="str")
def str_(element):
    return str(element)

@register.simple_tag(takes_context=True)
def teamscore(context):
    return context['team'].score(context['window'])

@register.simple_tag()
def current_window():
    return Window.current()

@register.simple_tag()
def switch_window(window, resolver_match):
    kwargs = resolver_match.kwargs
    if 'window_id' in kwargs:
        kwargs['window_id'] = window.id
    return reverse(resolver_match.view_name, args=resolver_match.args, kwargs=kwargs)

@register.simple_tag(takes_context=True)
def other_windows(context):
    # TODO(Yatharth): Extract to queries, or consider changing all of this altogether
    return Window.objects.exclude(pk=context['window'].id)

@register.simple_tag()
def format_problem(problem, team):
    data = problem.__dict__
    # XXX(Yatharth): Is the first condition necessary?
    if 'dynamic' in data and not problem.dynamic:
        return problem

    class Dummy:
        pass

    result = Dummy()
    data['description_html'] = problem.generate_desc(team)
    result.__dict__ = data
    return result
#
@register.simple_tag()
def solved(problem, team):
    return queries.solved(problem, team)
