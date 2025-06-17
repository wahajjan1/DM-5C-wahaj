def swap_variables(a, b):
    """
    Swaps the values of two variables without using a third variable,
    using the bitwise XOR method.
    """
    print(f"Original values -> a: {a}, b: {b}")

    a = a ^ b  # Step 1: a becomes a ^ b
    b = a ^ b  # Step 2: b becomes original a
    a = a ^ b  # Step 3: a becomes original b

    print(f"Swapped values  -> a: {a}, b: {b}")
    return a, b

# Example usage:
x = 10
y = 5
x, y = swap_variables(x, y)
