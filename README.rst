=============================================================
Collectors Extension for DISSM Satellite Imagery Repositories
=============================================================

About
=====

DISSM-Collectors is a Flask extension following `Brazil Data Cube Collectors <https://github.com/brazil-data-cube/bdc-collectors>`_ interfaces to retrieve satellite imagery from DISSM repositories.

We define our custom collectors using Python entry point in ``setup.py``.

Note: It is an experimental implementation under development.

Installation
============

Development installation
------------------------

Pre-Requirements
++++++++++++++++

The ``DISSM Collectors`` (``DISSM-Collectors``) depends essentially on:

- `Brazil Data Cube Collectors <https://github.com/brazil-data-cube/bdc-collectors>`_

Clone the software repository
+++++++++++++++++++++++++++++

Use ``git`` to clone the software repository::

    git clone https://github.com/dissm-inpe/dissm-collectors.git

Install DISSM-Collectors in Development Mode
++++++++++++++++++++++++++++++++++++++++++

Go to the source code folder::

    cd dissm-collectors

Install in development mode::

    pip3 install -e .

.. note::

    If you want to create a new *Python Virtual Environment*, please, follow this instruction:

    *1.* Create a new virtual environment linked to Python 3.11::

        python3.11 -m venv venv

    **2.** Activate the new environment::

        source venv/bin/activate

    **3.** Update pip and setuptools::

        pip3 install --upgrade pip

        pip3 install --upgrade setuptools

Usage
=====

In order to verify if extension is enabled, use the ``bdc-collector show-providers`` command::

    bdc-collector show-providers

Output::

    BDC-Collectors  Copyright (C) 2023  INPE
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    Supported providers:
        CREODIAS
        Dataspace
        DGI
        Google
        MODIS
        ONDA
        SciHub
        USGS
        GOES <===

Examples
========

See ``examples`` folder.

GOES-16 Data
------------

.. code-block:: python

    from flask import Flask
    from bdc_collectors import CollectorExtension
    
    app = Flask(__name__)
    ext = CollectorExtension(app)
    
    # Get specific GOES collector
    provider = ext.get_provider('GOES')()
    
    # Search scenes from 2024/02/01 until 2024/02/02, GOES-16/Band 13
    scenes = provider.search(
        query='GOES-16', band='13',
        start_date='20240201', end_date='20240202'
    )

    # Download first scene
    provider.download(scenes[0].scene_id, output_dir='./')

GOES-13 Data
------------

.. code-block:: python

    from flask import Flask
    from bdc_collectors import CollectorExtension

    app = Flask(__name__)
    ext = CollectorExtension(app)

    # Get specific GOES collector
    provider = ext.get_provider('GOES')()

    # Search scenes from 2016/04/08 until 2016/04/09, GOES-13/Band 04
    scenes = provider.search(
        query='GOES-13', band='04',
        start_date='20160408', end_date='20160409'
    )

    # Download first scene
    provider.download(scenes[0].scene_id, output_dir='./')

License
=======

.. admonition::
    Copyright (C) INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
