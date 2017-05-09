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

Started at Alba. 

Tiago Coutinho main contributor.

C++ libtango python binding based on Boost.

Project moves to the ESRF.



2016 - MaxIV joins the game.


2017 - Welcome to Solaris.

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
 
 * develop branch as default branch in github
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
   - PEP8
   - PyFlake



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

Improvements 1/2.
-----


 * Unit tests

 * Git workflow    

 * Continius integration:
    - Official Conda Tango channel
    - Conda package build by travis
    - Windows build

 * Change of binding

 * Server argparse

---

Improvements 2/2.
-----           


 * Clean python module.

 * Refactor tango objects.

 * Documentation:
    - Add documentation about the documentation generation and mock system.
    - Documentation need to be reviewed:
        - Make documentation up to date
        - Promote HL API as the default way of programming in Python.
        - Document and promote new features.


---

name: The MAX-IV approach to tango events.
layout: true

The MAX-IV approach to tango events.
============
---


 * HDB++ Archive events.

 * Change events as default event stream.

 * Facade device approach.

 * Archive events as filtered events.
---


name: The facadedevice library.
layout: true

The facadedevice library.
============
---

[Facadedevice library](http://tango-facadedevice.readthedocs.io/en/latest/): A reactive event-based approach to high-level tango devices

---

name: itango features and jupyter integration
layout: true

itango features and jupyter integration
============

See Nicolas Leclercq [example](http://www.tango-controls.org/community/forum/c/development/python/amazing-jupyter/)

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

---

