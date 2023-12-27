ColorTables
===========

The ``ColorTables`` class provides predefined color tables, including a comprehensive list of HTML color names and their corresponding RGBA values.

.. lua:class:: ColorTables

   .. lua:attribute:: htmlColors

      A table containing key-value pairs where each key is an HTML color name and its value is a table representing the color in RGBA format. Each RGBA value is a number from 0 to 255 for R, G, B and from 0 to 1 for A (alpha).

      Example: ``lightskyblue`` is represented as ``{ 135, 206, 250, 1 }``.
