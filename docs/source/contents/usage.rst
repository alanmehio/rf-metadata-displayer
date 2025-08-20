
Installation
------------

| **rfmetadata** is available on PyPI hence you can use `pip` to install it.

It is recommended to perform the installation in an isolated `python virtual environment` (env).
You can create and activate an `env` using any tool of your preference (ie `virtualenv`, `venv`, `pyenv`).

Assuming you have 'activated' a `python virtual environment`:

.. code-block:: shell

  python -m pip install rfmetadata


---------------
Simple Use Case 
---------------

This application needs the **rfserver** to be live. The rfserver application creates the database for the user,
queries it and sends the response through the flask api.

First install the rfserver.

.. code-block:: shell

  python -m pip install rfserver

Then start the rfserver to allow the client to query the database.

.. code-block:: shell

  rfserver  

.. image:: _static/rfserver.png
   :alt: running the server.
   :width: 400px
   :align: center

Now you can run the rfmetadata and query the data.

.. code-block:: shell

  rfmetadata

.. image:: _static/rfmetadata.png
   :alt: running the server.
   :width: 400px
   :align: center

See the server when the displayer queries it:

.. image:: _static/rfserverQuery.png
   :alt: running the server.
   :width: 400px
   :align: center

If you don't run the server and you try to search in the displayer, you will get errors:

.. image:: _static/rfmetadataErrors.png
   :alt: running the server.
   :width: 400px
   :align: center

--------------
Running PyTest 
--------------
| PyTest can be run from command line.

.. code-block:: shell
  
  python -m pip install -e . rfmetadata[test]
  pytest



