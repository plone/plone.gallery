# -*- coding: utf-8 -*-

# from plone.gallery import _
from plone import api
from .photo_gallery import BasePhotoGalleryMixin
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface
from plone.app.contenttypes.interfaces import IImage

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IGalleryList(Interface):
    """Marker Interface for IGalleryList"""


@implementer(IGalleryList)
class GalleryList(BrowserView, BasePhotoGalleryMixin):

    def __call__(self):
        return self.index()

    def album_images(self):
        images = []
        for item in self.context.relatedItems:
            rel_obj = item.to_object
            if not IImage.providedBy(rel_obj):
                continue
            images.append(rel_obj)
        return images
