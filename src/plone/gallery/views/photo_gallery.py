# -*- coding: utf-8 -*-

from plone.app.contenttypes.browser.collection import CollectionView
# from plone.gallery import _
from plone.app.contenttypes.browser.folder import FolderView
from Products.CMFPlone.resources import add_bundle_on_request


class PhotoGallery(FolderView):

    def __call__(self):
        add_bundle_on_request(self.request, "spotlightjs")
        add_bundle_on_request(self.request, "flexbin")
        return self.index()

    # We need to get the scale url here, without the tag.
    # right now we use the old way with the scale name in the url for the big picture

    # def images_view(self):
    #     return

    # def scale(
    #         self,
    #         brain,
    #         fieldname=None,
    #         scale=None,
    #         height=None,
    #        # def images_view(self):
    #     return

    # def scale(
    #         self,
    #         brain,
    #         fieldname=None,
    #         scale=None,
    #         height=None,
    #         width=None,
    #         direction='thumbnail',
    #         **kwargs):
    #     obj = brain.getObject()
    #     images = obj.restrictedTraverse('@@images')
    #     tag = images.tag(fieldname, **kwargs)
    #     return tag     **kwargs):
    #     obj = brain.getObject()
    #     images = obj.restrictedTraverse('@@images')
    #     tag = images.tag(fieldname, **kwargs)
    #     return tag


class PhotoGalleryCollection(CollectionView):

    def __call__(self):
        add_bundle_on_request(self.request, "spotlightjs")
        add_bundle_on_request(self.request, "flexbin")
        return self.index()
