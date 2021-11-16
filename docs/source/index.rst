CODECipher
----------

**codecipher** is package for cipher utilities.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/electux/codecipher/workflows/Python%20package/badge.svg
   :target: https://github.com/electux/codecipher/workflows/Python%20package/badge.svg?branch=main

.. |GitHub issues| image:: https://img.shields.io/github/issues/electux/codecipher.svg
   :target: https://github.com/electux/codecipher/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/electux/codecipher.svg
   :target: https://github.com/electux/codecipher/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/codecipher/badge/?version=latest
   :target: https://codecipher.readthedocs.io/projects/codecipher/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/electux/codecipher/releases

To install **codecipher** type the following

.. code-block:: bash

    tar xvzf codecipher-x.y.z.tar.gz
    cd codecipher-x.y.z/
    # pyton3
    pip3 install -r requirements.txt
    python3 -m build
    pip3 install codecipher-x.y.z-py3-none-any.whl

or old fashioned way

.. code-block:: bash

    tar xvzf codecipher-x.y.z.tar.gz
    cd codecipher-x.y.z/
    # pyton3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install ats-utilities

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/electux/codecipher/workflows/codecipher%20docker%20checker/badge.svg
   :target: https://github.com/electux/codecipher/actions?query=workflow%3A%22codecipher+docker+checker%22

Dependencies
-------------

**codecipher** requires next modules and libraries

* None

Package structure
--------------------

**codecipher** is based on OOP.

Package structure

.. code-block:: bash

    codecipher/
    ├── a1z52n62/
    │   ├── decode.py
    │   ├── encode.py
    │   └── __init__.py
    ├── atbs/
    │   ├── decode.py
    │   ├── encode.py
    │   ├── __init__.py
    │   └── lookup_table.py
    ├── b64/
    │   ├── decode.py
    │   ├── encode.py
    │   └── __init__.py
    ├── caesar/
    │   ├── decode.py
    │   ├── encode.py
    │   └── __init__.py
    ├── __init__.py
    ├── vernam/
    │   ├── decode.py
    │   ├── encode.py
    │   └── __init__.py
    └── vigenere/
        ├── decode.py
        ├── encode.py
        ├── __init__.py
        ├── key_generator.py
        └── lookup_table.py

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2021 by `electux.github.io/codecipher <https://electux.github.io/codecipher>`_

**codecipher** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/electux/codecipher/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
