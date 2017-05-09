name: empty layout
layout: true

---
name: title
class: center, middle

SOLARIS PyTango Workshop.
========================

Lukasz Zytniak - Vincent Michel - Antoine Dupré 

May 10th 2017


---

name: PyTango History
layout: true

PyTango History
=========

---

Started at Alba 
Tiago Coutinho main contributor
C++ libtango python binding based on Boost


Project moves to the ESRF



2016-April - MaxIV joins the game.


2017-May - Welcome to Solaris.

---

name: Current Status
layout: true

Current Status.
===========
---



Project on Github

Last release: v9.2.1
Release v9.2.2 upcomming





---
name: Contributing to PyTango
layout: true

Contributing to PyTango.
======

---

Git workflow.
------

 * Github issues.

 * Pull request.

 * PR merged in develop branch  (reviewed and approved).

 * develop  branch merged into master at each release.


> Make develop branch as default branch in github
---

Unit-testing.
---------

 * Based on Pytest.

 * Continious integration:
    - TravisCI is running tests in a conda environment.

 * 574 tests:
    - client tests.
    - server tests.
    - event tests.

> Useful test context:
```python 
from tango.test_utils import DeviceTestContext
```

---

Documentation.
---------

 * Documentation is generated from the sources.

 * The documentation is now hosted on readthedocs. (PyTango version >= 9.)


> Only works with >= python3.5

---

Coding standards.
---------

 * Flake8

---
name: Pending issues and future work.
layout: true

Pending issues and future work.
============
---


Pending issues
------


 * Pytango server restart segfault.

 * Deprecated NumPy API.

 * Compilation warnings related to zero message queue.

---

Tango9 missing features:
---------


 * Pipe events.

 * Pipe write (client & server).

 * Dynamic commands.

 * Forwarded attributes API.

 * Device interface change event.

 * Fill polling cache from the code ?

---

Improvements.
-----


 * Unit tests
 * Git workflow    
 * Continius integration:
    - Official Conda Tango channel
    - Conda package build by travis
    - Windows build
 * Change of binding
 * Documentation:
    - Documentation about documentation generation and mock system.
    - Documentation need to be reviewed:
        - Make documentation up to date
        - Promote HL API as the default way of programming in Python.
        - Document and promote new features.
 * Server argparse
 * Simplify DeviceImpl
 * Clean directory tree
 * Refactor tango objects

---

name: The MAX-IV approach to tango events.
layout: true

The MAX-IV approach to tango events.
============
---


 * HDB++ Archive events
 * Change events as default event stream 
 * Facade device approach
 * Archive events as filtered events
---


name: The facadedevice library: a reactive event-based approach to high-level tango devices
layout: true

The facadedevice library: a reactive event-based approach to high-level tango devices
============
---

---

name: itango features and jupyter integration
layout: true

itango features and jupyter integration
============


---

name: threading with PyTango
layout: true

threading with PyTango
============
---


---

name:  green modes
layout: true
green modes
============
---



---

name: asyncio in PyTango
layout: true
asyncio in PyTango
============
---

---

