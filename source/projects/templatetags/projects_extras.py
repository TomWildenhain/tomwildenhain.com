from django import template
from django.utils import timezone
from django.template import loader, Template, Variable, TemplateSyntaxError

register = template.Library()

@register.simple_tag(takes_context=True)
def project_images(context, small=False):
    project = context['project']
    context = {'project': project, 'small': small}
    return loader.get_template('projects/image_set.html').render(context)

@register.simple_tag(takes_context=True)
def video(context, url):
    context = {'url': url}
    return loader.get_template('projects/video.html').render(context)

@register.simple_tag(takes_context=True)
def video_pair(context, url1, url2):
    context = {'url1': url1, 'url2': url2}
    return loader.get_template('projects/video_pair.html').render(context)

class RenderAsTemplateNode(template.Node):
    def __init__(self, item_to_be_rendered):
        self.item_to_be_rendered = Variable(item_to_be_rendered)

    def render(self, context):
        try:
            actual_item = self.item_to_be_rendered.resolve(context)
            actual_item = "{% load projects_extras %} " + actual_item
            return Template(actual_item).render(context)
        except template.VariableDoesNotExist:
            return ''

def render_project_description(parser, token):
    bits = token.split_contents()
    if len(bits) !=2:
        raise TemplateSyntaxError("'%s' takes only one argument"
                                  " (a variable representing a template to render)" % bits[0])
    return RenderAsTemplateNode(bits[1])

render_as_template = register.tag(render_project_description)