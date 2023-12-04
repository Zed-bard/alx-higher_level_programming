def add_tuple(tuple_a=(), tuple_b=()):
  """
  Adds two tuples element-wise, assuming missing elements are 0.

  Args:
    tuple_a: The first tuple (default empty).
    tuple_b: The second tuple (default empty).

  Returns:
    A new tuple with the element-wise sums, handling missing elements.
  """

  # Pad the tuples with 0s to ensure they're at least 2 elements long.
  tuple_a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
  tuple_b = tuple_b[:2] + (0,) * (2 - len(tuple_b))

  # Add the corresponding elements and return the result as a tuple.
  return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
