# CODECipher

<img align="right" src="https://raw.githubusercontent.com/electux/codecipher/dev/docs/codecipher_logo.png" width="25%">

**codecipher** is package for cipher utilities.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![codecipher python checker](https://github.com/electux/codecipher/actions/workflows/codecipher_python_checker.yml/badge.svg)](https://github.com/electux/codecipher/actions/workflows/codecipher_python_checker.yml) [![codecipher package checker](https://github.com/electux/codecipher/actions/workflows/codecipher_package_checker.yml/badge.svg)](https://github.com/electux/codecipher/actions/workflows/codecipher_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/electux/codecipher.svg)](https://github.com/electux/codecipher/issues) [![GitHub contributors](https://img.shields.io/github/contributors/electux/codecipher.svg)](https://github.com/electux/codecipher/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Package structure](#package-structure)
- [Code coverage](#code-coverage)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/electux/codecipher/dev/docs/debtux.png)

[![codecipher python3 build](https://github.com/electux/codecipher/actions/workflows/codecipher_python3_build.yml/badge.svg)](https://github.com/electux/codecipher/actions/workflows/codecipher_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**codecipher** is located at **[pypi.org](https://pypi.org/project/codecipher/)**.

You can install by using pip

```bash
# python3
pip3 install codecipher
```

##### Install using build

Navigate to **[release page](https://github.com/electux/codecipher/releases)** download and extract release archive.

To install **codecipher**, run

```bash
tar xvzf codecipher-x.y.z.tar.gz
cd codecipher-x.y.z
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install codecipher-x.y.z-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/electux/codecipher/releases)** download and extract release archive.

To install **codecipher**, locate and run setup.py with arguments

```bash
tar xvzf codecipher-x.y.z.tar.gz
cd codecipher-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**codecipher** requires other modules and libraries (Python 3.x)
* None

### Usage

```python
from codecipher.a1z52n62.engine import A1Z52N62
from codecipher.atbs.engine import ATBS
from codecipher.b64.engine import B64
from codecipher.caesar.engine import Caesar
from codecipher.vigenere.engine import Vigenere
from codecipher.vernam.engine import Vernam

print("A1z52N62 cipher")
cipher = A1Z52N62()
data = "More Human Than Human01 Is Our Motto"
# encoding data
encode_data = cipher.encode(data)
# encoded data
print(encode_data)
# decoding data
decode_data = cipher.decode(encode_data)
# decoded data
print(decode_data)
print(50*'=')

print("ATBS cipher")
cipher = ATBS()
data = "More Human Than Human01 Is Our Motto"
# encoding data
encode_data = cipher.encode(data)
# encoded data
print(encode_data)
# decoding data
decode_data = cipher.decode(encode_data)
# decoded data
print(decode_data)
print(50*'=')

print("B64 cipher")
cipher = B64()
data = "More Human Than Human01 Is Our Motto"
# encoding data
encode_data = cipher.encode(data)
# encoded data
print(encode_data)
# decoding data
decode_data = cipher.decode(encode_data)
# decoded data
print(decode_data)
print(50*'=')

print("Caesar cipher")
cipher = Caesar()
data = "More Human Than Human01 Is Our Motto"
# encoding data
encode_data = cipher.encode(data)
# encoded data
print(encode_data)
# decoding data
decode_data = cipher.decode(encode_data)
# decoded data
print(decode_data)
print(50*'=')

print("Vigenere cipher")
cipher = Vigenere()
data = "More Human Than Human01 Is Our Motto"
# encoding data
encode_data = cipher.encode(data)
# encoded data
print(encode_data)
# decoding data
decode_data = cipher.decode(encode_data)
# decoded data
print(decode_data)
print(50*'=')

print("Vernam cipher")
cipher = Vernam()
data = "More Human Than Human01 Is Our Motto"
# encoding data
encode_data = cipher.encode(data)
# encoded data
print(encode_data)
# decoding data
decode_data = cipher.decode(encode_data)
# decoded data
print(decode_data)
print(50*'=')
```

### Package structure

**codecipher** is based on OOP.

Package structure

```bash
    codecipher/
    ├── a1z52n62/
    │   ├── config.py
    │   ├── decode/
    │   │   ├── decode_algorithm.py
    │   │   ├── decoder.py
    │   │   └── __init__.py
    │   ├── encode/
    │   │   ├── encode_algorithm.py
    │   │   ├── encoder.py
    │   │   └── __init__.py
    │   ├── engine.py
    │   └── __init__.py
    ├── abstracts/
    │   ├── ialgorithm.py
    │   ├── icharacter_validator.py
    │   ├── icipher_engine.py
    │   ├── iconfig.py
    │   ├── idata_validator.py
    │   ├── idecoder.py
    │   ├── iencoder.py
    │   ├── __init__.py
    │   └── ivalidation_engine.py
    ├── atbs/
    │   ├── config.py
    │   ├── decode/
    │   │   ├── decode_algorithm.py
    │   │   ├── decoder.py
    │   │   └── __init__.py
    │   ├── encode/
    │   │   ├── encode_algorithm.py
    │   │   ├── encoder.py
    │   │   └── __init__.py
    │   ├── engine.py
    │   └── __init__.py
    ├── b64/
    │   ├── config.py
    │   ├── decode/
    │   │   ├── decode_algorithm.py
    │   │   ├── decoder.py
    │   │   └── __init__.py
    │   ├── encode/
    │   │   ├── encode_algorithm.py
    │   │   ├── encoder.py
    │   │   └── __init__.py
    │   ├── engine.py
    │   └── __init__.py
    ├── caesar/
    │   ├── config.py
    │   ├── decode/
    │   │   ├── decode_algorithm.py
    │   │   ├── decoder.py
    │   │   └── __init__.py
    │   ├── encode/
    │   │   ├── encode_algorithm.py
    │   │   ├── encoder.py
    │   │   └── __init__.py
    │   ├── engine.py
    │   └── __init__.py
    ├── __init__.py
    ├── py.typed
    ├── validation/
    │   ├── character_validator.py
    │   ├── data_validator.py
    │   ├── __init__.py
    │   └── validation_engine.py
    ├── vernam/
    │   ├── config.py
    │   ├── decode/
    │   │   ├── decode_algorithm.py
    │   │   ├── decoder.py
    │   │   └── __init__.py
    │   ├── encode/
    │   │   ├── encode_algorithm.py
    │   │   ├── encoder.py
    │   │   └── __init__.py
    │   ├── engine.py
    │   └── __init__.py
    └── vigenere/
        ├── config.py
        ├── decode/
        │   ├── decode_algorithm.py
        │   ├── decoder.py
        │   └── __init__.py
        ├── encode/
        │   ├── encode_algorithm.py
        │   ├── encoder.py
        │   └── __init__.py
        ├── engine.py
        └── __init__.py

    21 directories, 69 files
```

### Code coverage

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `codecipher/__init__.py` | 9 | 0 | 100%|
| `codecipher/a1z52n62/__init__.py` | 9 | 0 | 100%|
| `codecipher/a1z52n62/config.py` | 26 | 0 | 100%|
| `codecipher/a1z52n62/decode/__init__.py` | 9 | 0 | 100%|
| `codecipher/a1z52n62/decode/decode_algorithm.py` | 41 | 6 | 85%|
| `codecipher/a1z52n62/decode/decoder.py` | 30 | 2 | 93%|
| `codecipher/a1z52n62/encode/__init__.py` | 9 | 0 | 100%|
| `codecipher/a1z52n62/encode/encode_algorithm.py` | 32 | 2 | 94%|
| `codecipher/a1z52n62/encode/encoder.py` | 30 | 2 | 93%|
| `codecipher/a1z52n62/engine.py` | 36 | 0 | 100%|
| `codecipher/abstracts/__init__.py` | 9 | 0 | 100%|
| `codecipher/abstracts/ialgorithm.py` | 16 | 1 | 94%|
| `codecipher/abstracts/icharacter_validator.py` | 14 | 1 | 93%|
| `codecipher/abstracts/icipher_engine.py` | 17 | 2 | 88%|
| `codecipher/abstracts/iconfig.py` | 23 | 0 | 100%|
| `codecipher/abstracts/idata_validator.py` | 14 | 1 | 93%|
| `codecipher/abstracts/idecoder.py` | 10 | 2 | 80%|
| `codecipher/abstracts/iencoder.py` | 10 | 2 | 80%|
| `codecipher/abstracts/ivalidation_engine.py` | 18 | 2 | 89%|
| `codecipher/atbs/__init__.py` | 9 | 0 | 100%|
| `codecipher/atbs/config.py` | 26 | 0 | 100%|
| `codecipher/atbs/decode/__init__.py` | 9 | 0 | 100%|
| `codecipher/atbs/decode/decode_algorithm.py` | 28 | 3 | 89%|
| `codecipher/atbs/decode/decoder.py` | 30 | 2 | 93%|
| `codecipher/atbs/encode/__init__.py` | 9 | 0 | 100%|
| `codecipher/atbs/encode/encode_algorithm.py` | 28 | 3 | 89%|
| `codecipher/atbs/encode/encoder.py` | 30 | 2 | 93%|
| `codecipher/atbs/engine.py` | 36 | 1 | 97%|
| `codecipher/b64/__init__.py` | 9 | 0 | 100%|
| `codecipher/b64/config.py` | 26 | 0 | 100%|
| `codecipher/b64/decode/__init__.py` | 9 | 0 | 100%|
| `codecipher/b64/decode/decode_algorithm.py` | 32 | 7 | 78%|
| `codecipher/b64/decode/decoder.py` | 30 | 2 | 93%|
| `codecipher/b64/encode/__init__.py` | 9 | 0 | 100%|
| `codecipher/b64/encode/encode_algorithm.py` | 27 | 3 | 89%|
| `codecipher/b64/encode/encoder.py` | 30 | 2 | 93%|
| `codecipher/b64/engine.py` | 36 | 2 | 94%|
| `codecipher/caesar/__init__.py` | 9 | 0 | 100%|
| `codecipher/caesar/config.py` | 26 | 0 | 100%|
| `codecipher/caesar/decode/__init__.py` | 9 | 0 | 100%|
| `codecipher/caesar/decode/decode_algorithm.py` | 41 | 2 | 95%|
| `codecipher/caesar/decode/decoder.py` | 30 | 2 | 93%|
| `codecipher/caesar/encode/__init__.py` | 9 | 0 | 100%|
| `codecipher/caesar/encode/encode_algorithm.py` | 41 | 2 | 95%|
| `codecipher/caesar/encode/encoder.py` | 30 | 2 | 93%|
| `codecipher/caesar/engine.py` | 36 | 2 | 94%|
| `codecipher/validation/__init__.py` | 9 | 0 | 100%|
| `codecipher/validation/character_validator.py` | 17 | 1 | 94%|
| `codecipher/validation/data_validator.py` | 19 | 1 | 95%|
| `codecipher/validation/validation_engine.py` | 24 | 4 | 83%|
| `codecipher/vernam/__init__.py` | 9 | 0 | 100%|
| `codecipher/vernam/config.py` | 26 | 0 | 100%|
| `codecipher/vernam/decode/__init__.py` | 9 | 0 | 100%|
| `codecipher/vernam/decode/decode_algorithm.py` | 44 | 5 | 89%|
| `codecipher/vernam/decode/decoder.py` | 30 | 2 | 93%|
| `codecipher/vernam/encode/__init__.py` | 9 | 0 | 100%|
| `codecipher/vernam/encode/encode_algorithm.py` | 44 | 5 | 89%|
| `codecipher/vernam/encode/encoder.py` | 30 | 2 | 93%|
| `codecipher/vernam/engine.py` | 36 | 0 | 100%|
| `codecipher/vigenere/__init__.py` | 9 | 0 | 100%|
| `codecipher/vigenere/config.py` | 26 | 0 | 100%|
| `codecipher/vigenere/decode/__init__.py` | 9 | 0 | 100%|
| `codecipher/vigenere/decode/decode_algorithm.py` | 40 | 3 | 92%|
| `codecipher/vigenere/decode/decoder.py` | 30 | 2 | 93%|
| `codecipher/vigenere/encode/__init__.py` | 9 | 0 | 100%|
| `codecipher/vigenere/encode/encode_algorithm.py` | 40 | 3 | 92%|
| `codecipher/vigenere/encode/encoder.py` | 30 | 2 | 93%|
| `codecipher/vigenere/engine.py` | 36 | 0 | 100%|
| **Total** | 1541 | 90 | 94% |

### Docs

[![documentation status](https://readthedocs.org/projects/codecipher/badge/?version=latest)](https://codecipher.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [codecipher.readthedocs.io](https://codecipher.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to codecipher](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2021 - 2026 by [electux.github.io/codecipher](https://electux.github.io/codecipher/)

**codecipher** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/electux/codecipher/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
