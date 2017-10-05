name: empty layout
layout: true

---
name: title
class: center, middle

PyTango Workshop
================

[Tiago Coutinho](https://github.com/tiagocoutinho) - [Vincent Michel](https://github.com/vxgmichel)

ICALEPCS 2017 - Barcelona

*

GitHub: [vxgmichel/icalepcs-workshop](https://github.com/vxgmichel/icalepcs-workshop)

Slides: [tinyurl.com/icalepcs-rp](http://tinyurl.com/icalepcs-workshop)

---
name: presentation
layout: true

What is PyTango?
================

---

* Python library

* Binding over the C++ tango libray

* ... using boost-python

* relies on numpy

* Multi OS: Linux, Windows, Mac

* Works on python 2.7 .. 3.6

---

... plus some extras:

* Pythonic API

* asyncio and gevent event loop

* ITango (now a separate project)

* alternative TANGO Database server (sqlite, redis backends)

---

name: menu
class: middle
layout: true

What's on the menu?
===================

---

* A fresh python3 tango install using conda

* ITango, a powerful client interface

* Writing tango servers with 15 lines of python

* Testing our servers without a database

* A dive into Jupyter notebooks

---

class: middle
layout: true

Playing with
============

---

.center[![conda](images/conda_logo.svg)]

### Conda is both:

* an open source package management system

* an environment management system

* it runs on Windows, macOS and Linux

---

class: middle
layout: true

Playing with conda
==================

---

### Requirements for this workshop:

* A 64 bits linux machine

* An internet connection

* A Tango database accessible (optional)

* No sudo access is required

---

### Installing miniconda:

``` bash
# Download the latest miniconda
$ wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
[...]

# Extract to a local directory (~/miniconda3)
$ bash Miniconda3-latest-Linux-x86_64.sh -b # No manual intervention
[...]

# Activate the conda environment
$ source ~/miniconda3/bin/activate

# Test python
(root) $ python
Python 3.6.2 |Anaconda, Inc.| (default, Sep 30 2017, 18:42:57)
[...]
```

`(root)` indicates we the main conda environment activated

---

### Creating a tango environment

``` bash
# Conda information
(root) $ conda info
[...]

# Create a python3 + tango envrionment
(root) $ conda create --name tango3 --channel tango-controls itango python=3
[...]

# Activate the tango3 environment
(root) $ source activate tango3

# Test itango
(tango3) $ itango
ITango 9.2.2 -- An interactive Tango client.
Running on top of Python 3.6.2, IPython 6.1 and PyTango 9.2.2
[...]
```

Checkout [anaconda.org/tango-controls](https://anaconda.org/tango-controls)

---



---
name: none
class: middle, center
layout: true

---

# The next slides are from the previous workshop at SOLARIS

---

name: PyTango History
layout: true

PyTango History
=========

---

Started at SOLEIL.

2005 - Moved to ALBA. M. Taurel develops server.

2006 - T. Coutinho main contributor.

2012 - A new API for device servers.

2013 - Project moves with Tiago to the ESRF.

2015 - MaxIV joins the game.

2016 - PyTango 9 is realeased.

2017 - Welcome to Solaris.

---

name: Current Status
layout: true

Current Status
===========
---

- github.com/tango-controls/pytango

- 886 commits

- 11 releases

- 26 contributors

- latest release: v9.2.2


---
name: Contributing to PyTango
layout: true

Contributing to PyTango
======

---

Git workflow
------

 * Github issues

 * Pull request

 * PR merged in develop branch  (reviewed and approved)

 * develop  branch merged into master at each release

 * develop branch as default branch in github

---

Unit-testing
---------

 * Based on Pytest

 * Continious integration:

    - TravisCI is running tests in a conda environment

    - for python2.7, python3.5, python3.6

 * 606 tests:

    - client tests

    - server tests

    - event tests

---

Testing
-------

Useful test context, introduced in 9.2.1:

```python
from tango.test_utils import DeviceTestContext

with DeviceTestContext(SomeDevice) as proxy:
    assert proxy.state() == DevState.ON
```

Or:

```console
$ python -m tango.test_context some_module.SomeDevice --debug=3
Ready to accept request
SomeDevice started on port 8888 with properties {}
Device access: tango://hostname:8888/test/nodb/somemodule#dbase=no
Server access: tango://hostname:8888/dserver/Empty/somemodule#dbase=no
```

---

Documentation
---------

 * Documentation is generated from the sources.

 * The documentation is now hosted on readthedocs. (PyTango version >= 9.)

 * Only works with >= python3.5 (because of the _tango module patch)

---

Coding standards
---------

 * Flake8

   - PEP8

   - PyFlake

 * There are plugins for most IDEs !

---

Progress
--------

 * Got rid of metaclass definition

 * ITango moved to a different project

 * Rename PyTango module to tango

 * Refactoring (asynchronous layer, etc.)

 * Cleaning repo


---

Example
-------

Device servers with pytango >=9.2.1

```python
from tango.server import Device, attribute

class Sensor(Device):

    @attribute(
	    dtype=float)
	def pressure(self):
	    return 1.23

if __ name__ == '__main__':
    Sensor.run_server()
```

---
name: Pending issues and future work.
layout: true

Pending issues and future work
============
---


Pending issues
------


 * Pytango server restart segfault

 * Deprecated NumPy API warnings

 * Compilation warnings related to zero message queue.

---

Tango9 missing features
---------


 * Pipe events (WIP)

 * Pipe write (client & server, WIP)

 * Dynamic commands

 * Forwarded attributes API

 * Device interface change event

 * Fill polling cache from the code ?

---

Improvements 1/2
-----


 * Unit tests (always!)

 * Continius integration:

    - Official Conda Tango channel

    - Conda package build by travis

    - Windows build

 * Change of binding (hard one --')

 * Server argparse (easy one!)

---

Improvements 2/2
-----


 * Clean python module (try tango.+TAB in IPython!)

 * Refactor tango objects

 * Documentation:

    - Add documentation about the documentation generation and mock system

    - Documentation need to be reviewed:

        - Make documentation up to date

        - Promote HL API as the default way of programming in Python

        - Document and promote new features


---

name: The MAX-IV approach to tango events.
layout: true

The MAX-IV approach to tango events
============
---

 * Problem with archiving

 * Change events as default event stream

 * Facade device approach

 * Archive events as filtered events

---


name: The facadedevice library.
layout: true

The facadedevice library.
============
---

[Facadedevice library](http://tango-facadedevice.readthedocs.io/en/latest/): A reactive event-based approach to high-level tango devices

---

name: ITango
layout: true

ITango
============

---

### Features

* IPython (jupyter) console

* Direct access to tango classes

* TANGO class sensitive device name auto-completion

* Event monitor

* Qt console

* Notebook

* User friendly error handling

---

### Hands on

``` bash
(tango3) $ conda install jupyter matplotlib
[...]
(tango3) $ jupyter notebook
```

```ipython
In [2]: tg_test = TangoTest("sys/tg_test/1")
[...]

```

---

### Plan B:

<a href="https://asciinema.org/a/0qfbv42rw496b942ny6lpdxrn">
   <img src="https://asciinema.org/a/0qfbv42rw496b942ny6lpdxrn.png"
   	style="display:block; margin:auto; width: 640px;"/>
</a>

---

name: threading with PyTango
layout: true

Threading with PyTango
============
---

"Adding a thread is adding at least one problem" V.Michel

Monitor lock

Alternative :
 * Tango Polling
 * Polled Update command


---

name:  Green modes
layout: true
Green modes
============
---

```python
tango.GreenMode.Synchronous
tango.GreenMode.Futures
tango.GreenMode.Gevent
tango.GreenMode.Asyncio
```

---

name: Asyncio in PyTango
layout: true
Asyncio in PyTango
============
---

Fill free to test it !
