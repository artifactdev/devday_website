from cms.toolbar_pool import toolbar_pool
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .models import Event
from devday.utils.devday_toolbar import DevDayToolbarBase


@toolbar_pool.register
class CheckinToolbar(DevDayToolbarBase):
    def populate(self):
        super().populate()
        event = Event.objects.current_event()
        if event.sessions_published:  # pragma: no branch
            self.add_admin_link_item_alphabetically(
                _('Check in'),
                reverse_lazy('attendee_checkin', kwargs={'event': event.slug}))
