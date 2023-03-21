=============
plone.gallery
=============

.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/plone/plone.gallery/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/plone/plone.gallery/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/plone/plone.gallery/badge.svg?branch=master
    :target: https://coveralls.io/github/plone/plone.gallery?branch=master
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/v/plone.gallery.svg
    :target: https://pypi.python.org/pypi/plone.gallery/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/plone.gallery.svg
    :target: https://pypi.python.org/pypi/plone.gallery
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/plone.gallery.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/plone.gallery.svg
    :target: https://pypi.python.org/pypi/plone.gallery/
    :alt: License

A photo gallery view for Plone CMS.

Features
========

- Shows photos of different sizes nicely and responsive
- Allows to zoom and browse thru the photos
- Has a white and blackmode
- Fullscreen and Autoplay mode
- Flexible setting of grid image scale and zoom image scale in gallery control panel
- works for folders and collections
- comes with TinyMCE templates for adding static galleries in Document,News items aso.
- come with a gallery_shortcode to use in richtext like in TinyMCE editor.

It uses the libraries `spotlight <https://github.com/nextapps-de/spotlight>`_ and `flexbin <https://github.com/guoyunhe/flexbin>`_ in combination for that.


.. image:: https://raw.githubusercontent.com/plone/plone.gallery/master/docs/plone-gallery.gif


Works from Phone to Big screen
------------------------------

.. image:: https://raw.githubusercontent.com/plone/plone.gallery/master/docs/screenshot-gallerie-grid.jpg


TinyMCE templates
-----------------

Also usable in TinyMCE with templates.

.. image:: https://raw.githubusercontent.com/plone/plone.gallery/master/docs/screenshot-gallerie-grid-richtext.jpg

To enable the templates, add these lines to the templates field in TinyMCE control panel.

.. code-block:: json

    [
      {"title": "3 pictures as gallery", "description": "Photo gallery: 4 photos", "url": "++plone++plone.gallery/tinymce-templates/gallery-grid-3.html"},
      {"title": "4 pictures as gallery", "description": "Photo gallery: 4 photos", "url": "++plone++plone.gallery/tinymce-templates/gallery-grid-4.html"},
      {"title": "6 pictures as gallery", "description": "Photo gallery: 6 photos", "url": "++plone++plone.gallery/tinymce-templates/gallery-grid-6.html"},
      {"title": "8 pictures as gallery", "description": "Photo gallery: 8 photos", "url": "++plone++plone.gallery/tinymce-templates/gallery-grid-8.html"}
    ]


Gallery shortcode
-----------------

You can use the `gallery_shortcode` as follows in TinyMCE.

Somewhere in the text place this placeholder: [gallery_shortcode]

.. code-block:: html

    <p>Tempor eu labore sint occaecat et esse. Irure nisi incididunt commodo exercitation aliqua. Ullamco quis quis sunt velit duis consectetur dolor aute cupidatat deserunt amet. Velit sunt eiusmod nulla proident consequat eu. Irure eiusmod aute reprehenderit occaecat laboris fugiat exercitation consectetur laboris nisi. Non ullamco commodo enim aute ex mollit est amet nostrud eu dolor. Mollit quis esse commodo irure duis veniam velit adipisicing.</p>

    [gallery_shortcode]

    <p>Tempor eu labore sint occaecat et esse. Irure nisi incididunt commodo exercitation aliqua. Ullamco quis quis sunt velit duis consectetur dolor aute cupidatat deserunt amet. Velit sunt eiusmod nulla proident consequat eu. Irure eiusmod aute reprehenderit occaecat laboris fugiat exercitation consectetur laboris nisi. Non ullamco commodo enim aute ex mollit est amet nostrud eu dolor. Mollit quis esse commodo irure duis veniam velit adipisicing.</p>

The outputfilter will now render all photos in referenced under related photos or contained in the context as a gallery.

You can either reference photos with the related photos field or place them into the current page if you have a folderish page.



Translations
============

This product has been translated into

- German (MrTango)


Installation
============

Install plone.gallery by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plone.gallery


and then running ``bin/buildout``

Usage
=====

Please make sure that you have reasonable image sizes set in your portal. Something as follow should be good.

    large 1400:1400
    preview 600:600
    mini 400:400
    thumb 200:200

The large size is used for the zoom and mini for the preview grid view.
Changing the other too just make sense if you change something.

After you have the correct sizes, you can just change the view on every Folder or Collection in Plone to "Photo gallery".


TODO
====

- make flexbin-row-height and flexbin-space configureable

Contribute
==========

- Issue Tracker: https://github.com/plone/plone.gallery/issues
- Source Code: https://github.com/plone/plone.gallery


License
=======

The project is licensed under the GPLv2.
