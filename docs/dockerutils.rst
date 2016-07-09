valhalla.dockerutils
====================
.. automodule:: valhalla.dockerutils


-------------------------

OwtfContainer
~~~~~~~~~~~~~~~~~~~

The OwtfContainer is the main object in this application.
It only have one constructor argument and thats a location for
a Owtf Valhalla Docker image.
When a new OwtfContainer class in instantiated the class
constructor will call *_validate_config_image_and_container()*.
*_validate_config_image_and_container()* will then check that
everything is OK with all the needed files in place.
If the image have been built to a container, if the
container is running and so on.

.. autoclass:: OwtfContainer
    :members:


