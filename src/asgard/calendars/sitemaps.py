from django.contrib.sitemaps import Sitemap

from asgard.calendars.models import Event

class CalendarEventSitemap(Sitemap):
	changefreq = "never"
	priority = 1.0
	
	def items(self):
		return Event.objects.all()
	
	def lastmod(self, obj):
		return obj.date_modified
