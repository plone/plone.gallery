# -*- coding: utf-8 -*-
from plone import api
from plone.app.contenttypes.browser.collection import CollectionView
from plone.app.contenttypes.browser.folder import FolderView
from Products.CMFPlone.resources import add_bundle_on_request


# from plone.gallery import _


class PhotoGallery(FolderView):
    def __call__(self):
        self.add_resources()
        return self.index()

    def add_resources(self):
        """override this method if you want to remove or add resources"""
        add_bundle_on_request(self.request, "flexbin")
        add_bundle_on_request(self.request, "spotlightjs")

    def grid_image_scale(self, brain):
        grid_image_scale = api.portal.get_registry_record(
            "plone.gallery.grid_image_scale"
        )
        image = brain.getObject()
        scale_util = api.content.get_view("images", image, self.request)
        return scale_util.scale("image", scale=grid_image_scale)

    def zoom_image_scale(self, brain):
        zoom_image_scale = api.portal.get_registry_record(
            "plone.gallery.zoom_image_scale"
        )
        image = brain.getObject()
        scale_util = api.content.get_view("images", image, self.request)
        return scale_util.scale("image", scale=zoom_image_scale)

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

    def grid_image_scale(self, brain):
        grid_image_scale = api.portal.get_registry_record(
            "plone.gallery.grid_image_scale"
        )
        image = brain.getObject()
        scale_util = api.content.get_view("images", image, self.request)
        return scale_util.scale("image", scale=grid_image_scale)

    def zoom_image_scale(self, brain):
        zoom_image_scale = api.portal.get_registry_record(
            "plone.gallery.zoom_image_scale"
        )
        image = brain.getObject()
        scale_util = api.content.get_view("images", image, self.request)
        return scale_util.scale("image", scale=zoom_image_scale)
