# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.gallery import _
from plone.gallery.interfaces import IPloneGalleryLayer
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IPloneGalleryControlPanel(Interface):
    grid_image_scale = schema.Choice(
        title=_(
            "Grid Image Scale",
        ),
        description=_(
            "Image scale to use in the grid view.",
        ),
        vocabulary="plone.app.vocabularies.ImagesScales",
        default="preview",
        required=True,
    )
    zoom_image_scale = schema.Choice(
        title=_(
            "Zoom Image Scale",
        ),
        description=_(
            "Image scale to use when zoomed.",
        ),
        vocabulary="plone.app.vocabularies.ImagesScales",
        default="large",
        required=True,
    )


class PloneGalleryControlPanel(RegistryEditForm):
    schema = IPloneGalleryControlPanel
    schema_prefix = "plone.gallery"
    label = _("Plone Gallery Control Panel")


PloneGalleryControlPanelView = layout.wrap_form(
    PloneGalleryControlPanel, ControlPanelFormWrapper
)


@adapter(Interface, IPloneGalleryLayer)
class PloneGalleryControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IPloneGalleryControlPanel
    configlet_id = "plone-gallery-controlpanel"
    configlet_category_id = "Products"
    title = _("Plone Gallery Control Panel")
    group = ""
    schema_prefix = "plone.gallery"
