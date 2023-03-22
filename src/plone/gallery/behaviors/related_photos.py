# -*- coding: utf-8 -*-

# from plone import schema
from plone.app.vocabularies.catalog import CatalogSource
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.gallery import _
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from z3c import relationfield
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


# def get_base_path(path):
#     base_obj = api.content.get(path)
#     if not base_obj:
#         return
#     base_path = "/".join(base_obj.getPhysicalPath())
#     return base_path


def get_related_photos_base_path(context):
    return context.absolute_url_path()


class IRelatedPhotosMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IRelatedPhotos(model.Schema):
    """ """

    directives.widget(
        "related_photos",
        pattern_options={
            "basePath": get_related_photos_base_path,
            "selectableTypes": ["Image"],
        },
    )
    related_photos = relationfield.schema.RelationList(
        title=_(
            "Related photos",
        ),
        description=_(
            'Related photos, rendered where you place the gallery_shortcode "[gallery_shortcode]".',
        ),
        value_type=relationfield.schema.RelationChoice(
            title="RelatedPhotos",
            source=CatalogSource(),
        ),
        required=False,
    )


@implementer(IRelatedPhotos)
@adapter(IRelatedPhotosMarker)
class RelatedPhotos(object):
    def __init__(self, context):
        self.context = context

    @property
    def related_photos(self):
        if safe_hasattr(self.context, "related_photos"):
            return self.context.related_photos or []
        return []

    @related_photos.setter
    def related_photos(self, value):
        self.context.related_photos = value
