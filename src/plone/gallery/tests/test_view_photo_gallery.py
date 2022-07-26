# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.gallery.testing import PLONE_GALLERY_FUNCTIONAL_TESTING
from plone.gallery.testing import PLONE_GALLERY_INTEGRATION_TESTING
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = PLONE_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "other-folder")
        api.content.create(self.portal, "Document", "front-page")

    def test_photo_gallery_is_registered(self):
        view = getMultiAdapter(
            (self.portal["other-folder"], self.portal.REQUEST), name="photo-gallery"
        )
        self.assertTrue(view.__name__ == "photo-gallery")
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in photo-gallery'
        # )

    def test_photo_gallery_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal["front-page"], self.portal.REQUEST), name="photo-gallery"
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = PLONE_GALLERY_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
