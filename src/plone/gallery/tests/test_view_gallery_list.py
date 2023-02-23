# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.gallery.testing import PLONE_GALLERY_FUNCTIONAL_TESTING
from plone.gallery.testing import PLONE_GALLERY_INTEGRATION_TESTING
from plone.gallery.views.gallery_list import IGalleryList
from zope.component import getMultiAdapter

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = PLONE_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "other-folder")
        api.content.create(self.portal, "Document", "front-page")

    def test_gallery_list_is_registered(self):
        view = getMultiAdapter(
            (self.portal["front-page"], self.portal.REQUEST), name="gallery-list"
        )
        self.assertTrue(IGalleryList.providedBy(view))


class ViewsFunctionalTest(unittest.TestCase):

    layer = PLONE_GALLERY_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
