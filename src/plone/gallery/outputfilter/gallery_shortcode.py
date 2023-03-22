# -*- coding: utf-8 -*-
# from bs4 import BeautifulSoup
from plone import api
from plone.gallery.interfaces import IPloneGalleryLayer


try:
    from plone.base.utils import safe_text
except ModuleNotFoundError:
    from Products.CMFPlone.utils import safe_text

import logging


# import re


logger = logging.getLogger("plone.outputfilter.spam_filter")


class GalleryShortcode:
    """OUTPUTFILTER: Converts Gallery shortcodes into gallery markup.

    [gallery_shortcode]

    becomes:

    <div class="flexbin flexbin-margin">
        <a class="spotlight" href="http://localhost:8080/Plone/gallery-short/dsc04674.jpg/@@images/cf196084-6a72-48ee-af6a-1329a131bc69.jpeg" title="DSC04674.JPG" data-description="">
            <img loading="lazy" src="http://localhost:8080/Plone/gallery-short/dsc04674.jpg/@@images/68a16f1e-d967-42e8-b4e4-3c7a9f35ff68.jpeg" alt="DSC04674.JPG" title="DSC04674.JPG">
        </a>

        <a class="spotlight" href="http://localhost:8080/Plone/gallery-short/dsc04683.jpg/@@images/3ad1524b-cc31-4d50-a55b-24b796416d07.jpeg" title="DSC04683.JPG" data-description="">
            <img loading="lazy" src="http://localhost:8080/Plone/gallery-short/dsc04683.jpg/@@images/f2073429-acfa-465f-9819-c8e5d13a5a1c.jpeg" alt="DSC04683.JPG" title="DSC04683.JPG">
        </a>

        <a class="spotlight" href="http://localhost:8080/Plone/gallery-short/dsc04737.jpg/@@images/02288d38-6c51-414c-8d18-dbd5bf691627.jpeg" title="DSC04737.JPG" data-description="">
            <img loading="lazy" src="http://localhost:8080/Plone/gallery-short/dsc04737.jpg/@@images/5d597d6e-afd2-4a07-8413-45931f3411dc.jpeg" alt="DSC04737.JPG" title="DSC04737.JPG">
        </a>

        <a class="spotlight" href="http://localhost:8080/Plone/gallery-short/dsc04791.jpg/@@images/59ec67d5-c4f8-4e39-b6c3-be316a196f01.jpeg" title="DSC04791.JPG" data-description="">
            <img loading="lazy" src="http://localhost:8080/Plone/gallery-short/dsc04791.jpg/@@images/9aa3d108-120b-488b-a5c0-251cdddedf6e.jpeg" alt="DSC04791.JPG" title="DSC04791.JPG">
        </a>
    </div>

    """

    order = 1000

    def is_enabled(self):
        return True

    def __init__(self, context=None, request=None):
        self.current_status = None
        self.context = context
        self.request = request

    def __call__(self, data):
        if not IPloneGalleryLayer.providedBy(self.request):
            return data
        data = safe_text(data)
        view = api.content.get_view(
            name="gallery-list", context=self.context, request=self.request
        )
        gallery_markup = view()
        data = data.replace("[gallery_shortcode]", gallery_markup)
        return data
