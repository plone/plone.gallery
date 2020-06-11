# -*- coding: utf-8 -*-

from plone.gallery import _
from Products.Five.browser import BrowserView
from plone.app.contenttypes.browser.folder import FolderView
from Products.CMFPlone.resources import add_bundle_on_request


class PhotoGallery(FolderView):

    def __call__(self):
        add_bundle_on_request(self.request, "spotlightjs")
        add_bundle_on_request(self.request, "flexbin")
        return self.index()

    def images_view(self):
        return

    def scale(
            self,
            brain,
            fieldname=None,
            scale=None,
            height=None,
            width=None,
            direction='thumbnail',
            **kwargs):
        obj = brain.getObject()
        images = obj.restrictedTraverse('@@images')
        tag = images.tag(fieldname, **kwargs)
        return tag
