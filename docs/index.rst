.. valhalla documentation master file, created by
   sphinx-quickstart on Sat Jul  9 10:17:47 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Valhalla's documentation!
====================================

This project aims to provide a simple and easy way to
do penetration testing with the `OWASP pentester guide <https://www.owasp.org/index.php/OWASP_Testing_Guide_v4_Table_of_Contents>`_.


The execution idea
------------------

In the penetration testing world there are alot of tools, which
Valhalla assembles into different Docker containers. This keeps them
separated from your local system, providing a good and simple way to
version and execute them via a nice looking web GUI.

Internally the process is simple. A Docker container holds each tool
that we need, and around the container is a small Rest API. This lets
the user execute commands and get the results in the following way::

    >>> from valhalla.dockerutils import OwtfContainer
    >>> from valhalla.middleman.handler import send_for_execution
    >>> oc = OwtfContainer('valhalla/containers/testcontainer')  # Point to the container
    >>> oc.build_image()  # Build Docker image
    >>> oc.build_container()  # Build continer from image
    >>> oc.is_valid  # Check if valid
    True
    >>> oc.start()  # Start the container
    >>> send_for_execution(oc, {'command': 'ping -c 1 scanme.nmap.org'})  # Execute command


Contents:

.. toctree::
   :maxdepth: 2

   dockerutils
   middleman



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

