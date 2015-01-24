"""
Mezzanine page processors for jdpages.
Read the mezzanine documentation for more info about page processors.
"""

import logging
logger = logging.getLogger(__name__)

from mezzanine.pages.page_processors import processor_for

from website.jdpages.models import HomePage, ColumnElementWidget
from website.jdpages.models import HorizontalPosition


@processor_for(HomePage)
def add_column_elements(request, page):
    element_widgets_left = ColumnElementWidget.objects.filter(horizontal_position=HorizontalPosition.LEFT).filter(page=page.homepage)
    element_widgets_left = ColumnElementWidget.create_widget_items(element_widgets_left)
    element_widgets_right =  ColumnElementWidget.objects.filter(horizontal_position=HorizontalPosition.RIGHT).filter(page=page.homepage)
    element_widgets_right = ColumnElementWidget.create_widget_items(element_widgets_right)
    return { "column_elements_left": element_widgets_left, "column_elements_right": element_widgets_right }
