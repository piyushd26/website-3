import logging
logger = logging.getLogger(__name__)

from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from mezzanine.blog.models import BlogCategory

from website.jdpages.models import ColumnElement, BlogCategoryElement


@receiver(post_save)
def post_save_callback(sender, instance, created, **kwargs):
    """
    Called after a model instance is saved.
    Created related database objects for some 
    
    Arguments:
    sender -- the model class
    instance -- the actual instance being saved
    created -- a boolean; True if a new record was created
    """
    
    if not created:
        return
    if sender == BlogCategory:
        if ColumnElement.objects.filter(object_id=instance.id, content_type=ContentType.objects.get_for_model(sender)):
            return
        blog_category = instance
        blog_category_element = BlogCategoryElement()
        blog_category_element.blog_category = blog_category
        blog_category_element.title = blog_category.title
        blog_category_element.content_type = ContentType.objects.get_for_model(BlogCategory)
        blog_category_element.object_id = blog_category.id
        blog_category_element.save()
        blog_category_element.site_id = instance.site_id
        blog_category_element.save(update_site=False)
        logger.info('Created BlogCategoryElement: ', blog_category_element)
    return
