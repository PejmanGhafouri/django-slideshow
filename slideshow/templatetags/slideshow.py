from django import template
from ..models import SlideShow

register = template.Library()


@register.inclusion_tag("slideshow/partials/slideshow.html")
def slides():
	return {
		"slides": SlideShow.objects.filter(status=True,article__status=True)
	}