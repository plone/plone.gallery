Changelog
=========


1.1.5 (2023-03-22)
------------------

- prevent outputfilter from running when addon is not enabled
  [MrTango]


1.1.4 (2023-03-22)
------------------

- deactivate tinyMCE templates in config, to prevent overriding existing config.
  [MrTango]


1.1.3 (2023-03-20)
------------------

- prevent error when related_photos attribute is None
  [MrTango]


1.1.2 (2023-02-24)
------------------

- Extend related photo list with photos from context, not override them
  [MrTango]


1.1.1 (2023-02-24)
------------------

- Add gallery gallery_shortcode feature to be used in RichText. Photos are coming from the new related photos behavior or are contained if it is a folderish type.
  [MrTango]


1.1.0 (2023-02-22)
------------------

- Add TinyMCE templates with galleries and therefor always enable flexbin and spotlight resources
  [MrTango]

- Fix traceback for missing cmf.ManagePortal permission (#12)
  [laulaz]


1.0.6 (2022-11-23)
------------------

- Just improving the PyPi description
  [MrTango]


1.0.5 (2022-11-22)
------------------

- Declare Plone 6 support and update CI
  [MrTango]


1.0.4 (2022-07-26)
------------------

- Fix gally view for collections
  [MrTango]


1.0.3 (2022-07-26)
------------------

- Fix missing plone.app.contentmenu zcml dependency for plone_displayviews menu
  [laulaz]

- Add gallery control panel to allow setting grid_image_scale and zoom_image_scale
  [MrTango]


1.0.2 (2021-09-29)
------------------

- fix python_requires definition in setup.py
  MrTango

- general cleanup and add an uninstall profile
  MrTango


1.0.1 (2020-07-07)
------------------

- Fix scale size in gallery grid view
  [MrTango]


1.0 (2020-07-07)
----------------

- Cleanup, fixed travis setup and isort version in tox setup
  [MrTango]


1.0a4 (2020-06-12)
------------------

- render img tag manually, to avoid having width and height attributes set
  [MrTango]


1.0a3 (2020-06-12)
------------------

- Fix flexbin image height
  [MrTango]

- Fix title and description in spotlight view
  [MrTango]


1.0a2 (2020-06-11)
------------------

- Fix resources files in released package
  [MrTango]

- Support also Collections not only Folders
  [MrTango]


1.0a1 (2020-06-11)
------------------

- Initial release.
  [MrTango]
