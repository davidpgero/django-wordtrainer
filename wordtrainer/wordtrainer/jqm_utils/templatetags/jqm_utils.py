from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template
from django.template import loader
register = template.Library()


class JQMPage(Tag):
        name = 'jqm_page'
        options = Options(
            Argument('template_name', required=True)
        )

        def render_tag(self, context, template_name):
            template = loader.get_template(template_name)
            html = template.render(context)
            return html

register.tag(JQMPage)
