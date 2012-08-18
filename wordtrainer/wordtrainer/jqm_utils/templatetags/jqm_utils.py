from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template
from django.template import loader
register = template.Library()


class JQMPage(Tag):
        name = 'jqm_page'
        options = Options(
            Argument('template_name', required=True),
            Argument('page_id', required=True)
        )

        def render_tag(self, context, template_name, page_id):
            context.update(dict(page_id=page_id))
            template = loader.get_template(template_name)
            html = template.render(context)
            return html

register.tag(JQMPage)
