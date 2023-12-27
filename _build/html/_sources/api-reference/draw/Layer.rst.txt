Layer
=====

The ``Layer`` class provides functionalities for managing drawing layers, which includes adding objects to layers and drawing all layers in order of their z-index.

.. lua:class:: Layer

   This class represents a drawing layer with a z-index and objects.

   .. lua:function:: new(z_index)

      Creates a new ``Layer`` instance.

      :param number z_index: The z-index of the layer, determining its drawing order. Defaults to ``0``.
      :return: A new instance of ``Layer``.

   .. lua:function:: draw_all()

      Draws all layers in order of their z-index.

   .. lua:method:: add(object, draw_function_name)

      Adds an object to the layer.

      :param table object: The object to be added to the layer.
      :param string draw_function_name: The name of the draw function to be used for the object. Defaults to ``"draw"``.

   .. lua:method:: draw()

      Draws all objects in the layer using their specified draw function.
