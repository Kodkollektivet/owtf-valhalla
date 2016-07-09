.. valhalla documentation master file, created by
   sphinx-quickstart on Sat Jul  9 10:17:47 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to valhalla's documentation!
====================================

This project aims at providing a simple and easy way to
do penetration testing with the `OWASP pentester guide <https://www.owasp.org/index.php/OWASP_Testing_Guide_v4_Table_of_Contents>`_.


The execution idea
------------------

The idea is simple.
In the penetration testing world there are alot of tools.
We assemble all the tools into different Docker containers
to keep them separated from your local system.
Providing a good and simple way to execute the different
via a nice looking GUI.

Internally the process is simple.
We have a Docker container with the tool that we need.
Around the container is a small Rest API.
We can execute commands and get the results in the following way::

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



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

