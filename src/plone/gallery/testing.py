# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plone.gallery  # NOQA:F401


class PloneGalleryLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plone.gallery)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone.gallery:default")


PLONE_GALLERY_FIXTURE = PloneGalleryLayer()


PLONE_GALLERY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_GALLERY_FIXTURE,),
    name="PloneGalleryLayer:IntegrationTesting",
)


PLONE_GALLERY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_GALLERY_FIXTURE,),
    name="PloneGalleryLayer:FunctionalTesting",
)


PLONE_GALLERY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONE_GALLERY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="PloneGalleryLayer:AcceptanceTesting",
)
