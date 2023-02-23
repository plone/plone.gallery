# -*- coding: utf-8 -*-

# from plone.gallery import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IGalleryList(Interface):
    """Marker Interface for IGalleryList"""


@implementer(IGalleryList)
class GalleryList(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('gallery_list.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
