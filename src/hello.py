def greet(name: str) -> str:
    """
    Return a greeting string for the given name.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return f"Hello, {name}!"
