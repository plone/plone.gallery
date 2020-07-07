.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.org/plone/plone.gallery.svg?branch=master
    :target: https://travis-ci.org/plone/plone.gallery

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

=============
plone.gallery
=============

A photo gallery view for Plone CMS.

Features
--------

- Shows photos of different sizes nicely and responsive
- Allows to zoom and browse thru the photos
- Has a white and blackmode
- Fullscreen and Autoplay mode

It uses the libraries `spotlight <https://github.com/nextapps-de/spotlight>`_ and `flexbin <https://github.com/guoyunhe/flexbin>`_ in combination for that.


.. image:: https://raw.githubusercontent.com/plone/plone.gallery/master/docs/plone-gallery.gif

Works from Phone to Big screen.


.. image:: https://raw.githubusercontent.com/plone/plone.gallery/master/docs/screenshot-gallerie-grid.jpg



Translations
------------

This product has been translated into

- German (MrTango)


Installation
------------

Install plone.gallery by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plone.gallery


and then running ``bin/buildout``

Usage
-----

Please make sure that you have reasonable image sizes set in your portal. Something as follow should be good.

    large 1400:1400
    preview 600:600
    mini 400:400
    thumb 200:200

The large size is used for the zoom and mini for the preview grid view.
Changing the other too just make sense if you change something.

After you have the correct sizes, you can just change the view on every Folder or Collection in Plone to "Photo gallerie".


TODO
----

- add some more tests for the view
- make flexbin-row-height and flexbin-space configureable

Contribute
----------

- Issue Tracker: https://github.com/plone/plone.gallery/issues
- Source Code: https://github.com/plone/plone.gallery


License
-------

The project is licensed under the GPLv2.
