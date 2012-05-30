=======
rest.py
=======

**An easy way to build RESTful services. Nothing more. Nothing less.**

Purpose
=======

The rest.py package is intended to replace the typical use of web.py. Web.py
is an incredible tool for building lightweight web services, but suffers from
two primary problems:

#.  It makes use of a global `web.ctx` property to supply request/response
    specific information.

#.  It has grown to include unnecessary features such as database abstraction,
    session handling, and templating.

This project will be a simple tool for building RESTful web services. It will
not include any tools other than those required to make accepting a request and
outputting a response fast, simple, and reliable.

Standards
=========

Commits
-------

All commit messages should follow the guide
`here <http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_
that describes the general structure of a good commit message. Adding to the
standards listed in the guide, the following standards should also be followed:

1. All messages begin with a verb in the imperative sense.

2. Limit verbs to `Add`, `Fix`, `Change`, `Remove`.

3. Place a colon (`:`) after the verb. `Add:`, `Fix:`, etc.

4. Make sure every commit is signed using `--signoff`.

If struggling for a good commit message just ask what the patch would do if
installed. Would it *Add: Feature X* or *Fix: Issue #00000*?

PEP8
----

All code in this repository will be compliant with PEP8 styles wherever
possible.

License
=======

rest.py
-------

The MIT License (MIT)

Copyright (c) 2012 Kevin Conway

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Werkzeug
--------

This project relies on, but does not include for distribution, the
`Werkzeug <https://github.com/mitsuhiko/werkzeug>`_ library for WSGI
abstraction. Werkzeug is available and distributed by its creators under the
`BSD <https://github.com/mitsuhiko/werkzeug/blob/master/LICENSE>`_ license.


Contributing
============

Contributions to this project are protected under a modified Oracle Contributor
Agreement detailed in the file `CONTRIBUTING`. While it is encouraged that all
contributors read the document the basic message is this:

    "You give me permission to modify and distribute your code and I promise to
    maintain an open source release of anything you contribute."
