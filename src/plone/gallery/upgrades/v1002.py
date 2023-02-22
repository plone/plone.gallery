# -*- coding: utf-8 -*-

from . import logger
from .base import reload_gs_profile


# from plone import api


def upgrade(setup_tool=None):
    """ """
    logger.info(
        "Running upgrade (Python): Load profile to enable TinyMCE templates and resources"
    )
    reload_gs_profile(setup_tool)
