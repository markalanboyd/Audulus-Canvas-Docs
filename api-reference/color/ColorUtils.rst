ColorUtils
==========

The ``ColorUtils`` class provides utility functions for handling color codes, including validation and conversion of hexadecimal color codes.

.. lua:class:: ColorUtils

   .. lua:function:: is_valid_hex_code(s)

      Validates whether a given string is a valid hexadecimal color code.

      :param string s: The string to validate.
      :return: Returns ``true`` if the string is a valid hexadecimal color code, otherwise returns ``false``.
        
         .. code-block:: lua
            :caption: Example

            -- #RGB
            print(is_valid_hex_code("#000")) -- true

            -- RGB
            print(is_valid_hex_code("fff")) -- true

            -- #RGBA
            print(is_valid_hex_code("#F1A2")) -- true

            -- #RRGGBB
            print(is_valid_hex_code("#d3a114")) -- true

            -- #RRGGBBAA
            print(is_valid_hex_code("#A3D229CF")) -- true

            print(is_valid_hex_code("#FF")) -- false
            print(is_valid_hex_code("#12345")) -- false
            print(is_valid_hex_code("#GH10")) -- false

   .. lua:function:: hex_code_to_color(s)

      Converts a hexadecimal color code to a color represented as a table with RGBA values.

      This function first validates the hex code. If the code is not valid, it raises an error.

      :param string s: The hexadecimal color code to convert.
      :return: A table representing the color in RGBA format, with each component as a number from 0 to 1.
      :raises: Raises an error if the input string is not a valid hexadecimal color code.
