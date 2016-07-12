containerutils
====================
.. automodule:: valhalla.dockerutils


-------------------------

OwtfContainer
~~~~~~~~~~~~~~~~~~~

The OwtfContainer is the main object in this application and has
one single constructor argument, being an Owtf Valhalla Docker image
location.

When a new OwtfContainer class is instantiated, the class constructor
will call *_validate_config_image_and_container()*. This will then
check that everything is OK with all the needed files in place, if the
image has been built, if the container is running and so on.

.. autoclass:: OwtfContainer
    :members:


.. autofunction:: get_valhalla_container


.. autofunction:: get_objectives_and_commands

