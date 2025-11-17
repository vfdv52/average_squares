Average Squares Documentation
=============================

Module Overview
---------------

The ``squares`` module provides functions for computing weighted averages of squares
and converting string data to numeric formats.

API Reference
-------------

.. automodule:: squares
   :members:
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

Usage Examples
--------------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from squares import average_of_squares, convert_numbers
   
   # Calculate average of squares with equal weights
   result = average_of_squares([1, 2, 4])
   print(result)  # Output: 7.0

Weighted Average
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Calculate weighted average of squares
   result = average_of_squares([2, 4], [1, 0.5])
   print(result)  # Output: 6.0

String Conversion
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Convert strings to numbers
   numbers = convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
   print(numbers)  # Output: [4, 8, 15, 16]

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   # Weights and numbers must have same length
   try:
       result = average_of_squares([1, 2, 4], [1, 0.5])
   except AssertionError as e:
       print(e)  # Output: weights and numbers must have same length