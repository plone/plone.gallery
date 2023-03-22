# -*- coding: utf-8 -*-
from plone import api
from plone.app.contenttypes.browser.collection import CollectionView
from plone.app.contenttypes.browser.folder import FolderView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer
from zope.interface import Interface


# from plone.gallery import _


class IPhotoGallery(Interface):
    """Marker Interface IPhotoGallery"""


class IPhotoGalleryCollection(Interface):
    """Marker Interface IPhotoGallery"""


class BasePhotoGalleryMixin:
    gallery_list_template = ViewPageTemplateFile("gallery_list.pt")

    def grid_image_scale(self, brain):
        grid_image_scale = api.portal.get_registry_record(
            "plone.gallery.grid_image_scale"
        )
        if hasattr(brain, "getObject"):
            image = brain.getObject()
        else:
            # already the object it self
            image = brain
        scale_util = api.content.get_view("images", image, self.request)
        return scale_util.scale("image", scale=grid_image_scale)

    def zoom_image_scale(self, brain):
        zoom_image_scale = api.portal.get_registry_record(
            "plone.gallery.zoom_image_scale"
        )
        if hasattr(brain, "getObject"):
            image = brain.getObject()
        else:
            # already the object it self
            image = brain
        scale_util = api.content.get_view("images", image, self.request)
        return scale_util.scale("image", scale=zoom_image_scale)


@implementer(IPhotoGallery)
class PhotoGallery(FolderView, BasePhotoGalleryMixin):
    def __call__(self):
        return self.index()


@implementer(IPhotoGalleryCollection)
class PhotoGalleryCollection(CollectionView, BasePhotoGalleryMixin):
    def __call__(self):
        return self.index()
