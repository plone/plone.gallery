# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.gallery.testing import PLONE_GALLERY_FUNCTIONAL_TESTING
from plone.gallery.testing import PLONE_GALLERY_INTEGRATION_TESTING
from plone.gallery.views.photo_gallery import IPhotoGallery
from plone.gallery.views.photo_gallery import IPhotoGalleryCollection
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):
    layer = PLONE_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "other-folder")
        api.content.create(self.portal, "Collection", "other-collection")
        api.content.create(self.portal, "Document", "front-page")

    def test_photo_gallery_is_registered(self):
        view = getMultiAdapter(
            (self.portal["other-folder"], self.portal.REQUEST), name="photo-gallery"
        )
        self.assertTrue(IPhotoGallery.providedBy(view))

    def test_photo_gallery_collection_is_registered(self):
        view = getMultiAdapter(
            (self.portal["other-collection"], self.portal.REQUEST), name="photo-gallery"
        )
        self.assertTrue(IPhotoGalleryCollection.providedBy(view))

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
