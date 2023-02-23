# -*- coding: utf-8 -*-
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from plone.gallery.behaviors.related_photos import IRelatedPhotosMarker
from plone.gallery.testing import PLONE_GALLERY_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class RelatedPhotosIntegrationTest(unittest.TestCase):

    layer = PLONE_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_behavior_related_photos(self):
        behavior = getUtility(IBehavior, "plone.gallery.related_photos")
        self.assertEqual(
            behavior.marker,
            IRelatedPhotosMarker,
        )
