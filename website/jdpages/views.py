import logging

from mezzanine.pages.models import RichTextPage

from fullcalendar.views import OccurrenceView

from website.jdpages.models import HomePage
from website.jdpages.models import SidebarSocial
from website.jdpages.models import PageHeaderImage

logger = logging.getLogger(__name__)


def get_homepage_id():
    homepage = HomePage.objects.values_list('id').first()
    if homepage is not None:
        return homepage[0]
    pages = RichTextPage.objects.filter(slug='/')
    if pages.exists():
        return pages[0].id
    return None


def get_page_header(page):
    """
    :returns: the page header for a given page.
    Uses parent page image when none is defined.
    Top parent is the HomePage.
    None when there is no Hompage or when the HomePage has no header.
    """

    # Get a random page header, or the first one if there is only one
    image = PageHeaderImage.objects.filter(page=page).order_by('?').first()
    if image is not None:
        return image

    # No image found! If we received an integer, then do not search further
    if isinstance(page, int):
        return None

    # Try from parent
    if page.parent:
        return get_page_header(page.parent)

    # Try from first homepage
    homepage = get_homepage_id()
    if homepage is not None:
        # Since we give get_page_header an integer, there is no infinite recursion here...
        return get_page_header(homepage)

    return None


def get_homepage_header():
    """ Returns the page header image of the homepage """
    homepage_id = get_homepage_id()
    if homepage_id is None:
        return None
    return get_page_header(homepage_id)


class OccuranceJDView(OccurrenceView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_for_sidebars'] = HomePage.objects.all().first()
        return context
