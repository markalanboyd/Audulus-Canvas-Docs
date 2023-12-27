Origin
======

The ``Origin`` class provides functionalities for handling origin points with various visual representations.

.. lua:class:: Origin

   This class represents an origin point with configurable visual representation and position.

   .. lua:function:: new(direction, options)

      Creates a new ``Origin`` instance.

      :param string direction: The direction where the origin will be placed. Valid values are ``n``, ``ne``, ``e``, ``se``, ``s``, ``sw``, ``w``, ``nw``, and ``c`` for center. Defaults to ``sw``.
      :param table options: A table of options to configure the origin's appearance. Includes keys for 'show', 'type', 'width', and 'color'.
      :return: A new instance of ``Origin``.

         .. code-block:: lua
            :caption: Example

            o = Origin.new("c", {show=true, type='+'})

   .. lua:function:: calculate_offset(direction)

      Calculates the offset of the origin based on the specified direction.

      :param string direction: The direction for calculating the offset.
      :return: A table representing the calculated offset.

   .. lua:method:: reset()

      Resets the origin to its initial state.

      Resets the translation of the origin back to its initial state, undoing any translations applied during the creation of the origin instance.
