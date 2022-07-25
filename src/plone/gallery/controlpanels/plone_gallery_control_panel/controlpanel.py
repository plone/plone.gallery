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
    myfield_name = schema.TextLine(
        title=_(
            "This is an example field for this control panel",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
    )


class PloneGalleryControlPanel(RegistryEditForm):
    schema = IPloneGalleryControlPanel
    schema_prefix = "plone.gallery.plone_gallery_control_panel"
    label = _("Plone Gallery Control Panel")


PloneGalleryControlPanelView = layout.wrap_form(
    PloneGalleryControlPanel, ControlPanelFormWrapper
)



@adapter(Interface, IPloneGalleryLayer)
class PloneGalleryControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IPloneGalleryControlPanel
    configlet_id = "plone_gallery_control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("Plone Gallery Control Panel")
    group = ""
    schema_prefix = "plone.gallery.plone_gallery_control_panel"
