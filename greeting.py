def greet(name: str) -> str:
    """The greeting the app shows a visitor."""
    return f"Hey, {name}!"


if __name__ == "__main__":
    print(greet("world"))
