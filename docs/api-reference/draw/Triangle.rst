Triangle
========

The ``Triangle`` class provides functionalities for creating, manipulating, and drawing triangles.

.. lua:class:: Triangle

   This class represents a triangle with three vertices and a color.

   .. lua:function:: new(vec2_a, vec2_b, vec2_c, color)

      Creates a new ``Triangle`` instance.

      :param table vec2_a: The first vertex of the triangle.
      :param table vec2_b: The second vertex of the triangle.
      :param table vec2_c: The third vertex of the triangle.
      :param table color: The color of the triangle.
      :return: A new instance of ``Triangle``.

   .. lua:method:: draw()

      Draws the triangle using the specified vertices and color.

   .. lua:method:: get_vec2s()

      Returns the vertices of the triangle.

      :return: A table containing the vertices of the triangle.

   .. lua:method:: get_vec2_a()

      :return: The first vertex of the triangle.

   .. lua:method:: get_vec2_b()

      :return: The second vertex of the triangle.

   .. lua:method:: get_vec2_c()

      :return: The third vertex of the triangle.

   .. lua:method:: Set_vec2s(...)

      Sets the vertices of the triangle.

   .. lua:method:: Set_vec2_a(x, y)

      Sets the first vertex of the triangle.

      :param number x: The x-coordinate.
      :param number y: The y-coordinate.

   .. lua:method:: Set_vec2_b(x, y)

      Sets the second vertex of the triangle.

      :param number x: The x-coordinate.
      :param number y: The y-coordinate.

   .. lua:method:: Set_vec2_c(x, y)

      Sets the third vertex of the triangle.

      :param number x: The x-coordinate.
      :param number y: The y-coordinate.

   .. lua:method:: centroid()

      Calculates the centroid of the triangle.

      :return: The centroid as a ``Vec2`` instance.

   .. lua:method:: area()

      Calculates the area of the triangle.

      :return: The area of the triangle.

   .. lua:method:: perimeter()

      Calculates the perimeter of the triangle.

      :return: The perimeter of the triangle.

   .. lua:method:: type()

      Determines the type of the triangle (equilateral, isosceles, or scalene).

      :return: The type of the triangle as a string.

   .. lua:method:: angle_type()

      Determines the angle type of the triangle (right, obtuse, or acute).

      :return: The angle type of the triangle as a string.

   .. lua:method:: scale(scalar)

      Scales the triangle by a specified scalar.

      :param number scalar: The scaling factor.
      :return: A new scaled ``Triangle`` instance.

   .. lua:method:: Scale(scalar)

      Scales the triangle in place by a specified scalar.

      :param number scalar: The scaling factor.

   .. lua:method:: rotate(angle)

      Rotates the triangle by a specified angle.

      :param number angle: The rotation angle in radians.
      :return: A new rotated ``Triangle`` instance.

   .. lua:method:: Rotate(angle)

      Rotates the triangle in place by a specified angle.

      :param number angle: The rotation angle in radians.

   .. lua:method:: translate(vec2)

      Translates the triangle by a specified vector.

      :param table vec2: The translation vector.
      :return: A new translated ``Triangle`` instance.

   .. lua:method:: Translate(vec2)

      Translates the triangle in place by a specified vector.

      :param table vec2: The translation vector.

   .. lua:method:: bounding_box()

      Calculates the bounding box of the triangle.

      :return: The minimum and maximum ``Vec2`` points defining the bounding box.

   .. lua:method:: incircle()

      Calculates the incircle of the triangle.

      :return: The center and radius of the incircle as a ``Vec2`` instance and a number, respectively.

   .. lua:method:: circumcircle()

      Calculates the circumcircle of the triangle.

      :return: The center and radius of the circumcircle as a ``Vec2`` instance and a number, respectively.
