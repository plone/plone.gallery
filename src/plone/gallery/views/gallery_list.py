# -*- coding: utf-8 -*-

# from plone.gallery import _
from .photo_gallery import BasePhotoGalleryMixin
from plone import api
from plone.app.contenttypes.interfaces import IImage
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IGalleryList(Interface):
    """Marker Interface for IGalleryList"""


@implementer(IGalleryList)
class GalleryList(BrowserView, BasePhotoGalleryMixin):
    def __call__(self):
        return self.index()

    def album_images(self):
        images = []
        # if not hasattr(self.context, "related_photos"):
        #     return images
        related_photos = getattr(self.context, "related_photos", []) or []
        for item in related_photos:
            rel_obj = item.to_object
            if not IImage.providedBy(rel_obj):
                continue
            images.append(rel_obj)
        images.extend(
            api.content.find(
                context=self.context,
                portal_type="Image",
                sort_on="getObjPositionInParent",
            )
        )
        return images
