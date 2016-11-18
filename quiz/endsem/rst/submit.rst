============================
SDES RST question (Nov-2016)
============================

Please type the following passage about open source including the weblinks and submit an rst file. The rst file will be compiled using rst2pdf and rst2html (with suitable options for math).

For more information about Open Source Philosophy, click here_.

| Below are some benefits. It is hard to be exhaustive.
| **Skills in FOSS are helpful because of following reasons:**

- They do not cost anything. Complete learning happens by source-code exploration.
- The employer need not pay for the employees to be 'productive'.  Hence employees are not 'white elephants'.

It is wrong of government funded educational institutions to teach students proprietary packages for following reasons.

- The private software company should be subsidizing the education if their package should be used for teaching: else the institute has been tricked to purchase the company's package for training the students at govt cost!

Instead of 'cut-throat competition' against each other, FOSS groups help in use of skills across FOSS packages. For example, LaTex skills are useful within rst in the following way. If we need an equation as below, then options like MathJax while compiling the rst file can fetch this equation.

.. math::
    \Gamma = \int_{-\infty}^{\infty} V \cdot \vec{d}l

All one needs to do is:
::

    >>> rst2html --math-output MathJax submit.rst submit.html

Some proprietary packages and their FOSS equivalents
====================================================

.. table::

    +--------------------+--------------------+-----------------+------------------+
    |Proprietary Package | Broad purpose      | FOSS equivalent |   License name   |
    +====================+====================+=================+==================+
    | Matlab             | Electrical, Data   | Octave_         | GPL              |
    |                    |                    +-----------------+------------------+
    |                    | analysis           | Scilab_         | CeCILL (GPL eq.) |
    +--------------------+--------------------+-----------------+------------------+
    | Cadence            | Circuit Simulation | ngspice_        | BSD              |
    |                    |                    +-----------------+------------------+
    | pspice             | Modelling          | eSim_           | Creative Commons |
    +--------------------+--------------------+-----------------+------------------+
    | Ansys-Fluent       | CFD                | OpenFOAM_       | GPL              |
    +--------------------+--------------------+-----------------+------------------+

| *(Contents in the above table perhaps have some details incorrect.)*
| **More about FOSS equivalents can be found at:**

- http://www.aicte-india.org/downloads/Commercial%20Software.pdf

.. _here: https://www.gnu.org/philosophy/philosophy.html
.. _Octave: http://www.gnu.org/s/octave
.. _Scilab: http://www.scilab.org
.. _ngspice: http://ngspice.sourceforge.net
.. _eSim: http://esim.fossee.in
.. _OpenFOAM: http://openfoam.com
