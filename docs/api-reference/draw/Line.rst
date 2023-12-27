Line
====

The ``Line`` class provides functionalities for creating and drawing lines.

.. lua:class:: Line

   This class represents a line with start and end points, color, and width.

   .. lua:function:: new(vec2_a, vec2_b, color, width)

      Creates a new ``Line`` instance.

      :param table vec2_a: The start point of the line.
      :param table vec2_b: The end point of the line.
      :param table color: The color of the line. Defaults to theme's text color.
      :param number width: The width of the line. Defaults to ``1``.
      :return: A new instance of ``Line``.

        .. code-block:: lua
            :caption: Example

            vec_a = Vec2.new(0, 0)
            vec_b = Vec2.new(0, 10)
            vec_c = Vec2.new(10, 10)

            line = Line.new(vec_a, vec_b, vec_c, theme.azureHighlight, 3)

   .. lua:function:: draw_between_all(...)

      Draws lines between all pairs of provided points.

      :param ...: A variable number of points represented as tables.

        .. code-block:: lua
            :caption: Example

            vec_a = Vec2.new(0, 0)
            vec_b = Vec2.new(0, 10)
            vec_c = Vec2.new(10, 10)

            p1 = Point.new(vec_a)
            p2 = Point.new(vec_b)
            p3 = Point.new(vec_c)

            Line.draw_between_all(p1, p2, p3)

   .. lua:function:: dash_between_all(...)

      Draws dashed lines between all pairs of provided points.

      :param ...: A variable number of points represented as tables.

   .. lua:function:: draw_from_to_all(vec2, ...)

      Draws lines from a given point to all other provided points.

      :param table vec2: The starting point for all lines.
      :param ...: A variable number of points represented as tables.

   .. lua:function:: dash_from_to_all(vec2, ...)

      Draws dashed lines from a given point to all other provided points.

      :param table vec2: The starting point for all dashed lines.
      :param ...: A variable number of points represented as tables.

   .. lua:method:: draw()

      Draws the line using the specified start and end points, color, and width.

   .. lua:method:: dashed(dash_length, space_length)

      Draws the line as a dashed line.

      :param number dash_length: The length of each dash. Defaults to ``5``.
      :param number space_length: The space between dashes. Defaults to the same as dash_length.
