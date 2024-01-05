#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name' or not hasattr(self, 'first_name'):
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        else:
            object.__setattr__(self, name, value)

# Example usage
if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"

    try:
        lc.last_name = "Snow"
    except AttributeError as e:
        print(f"[{e.__class__.__name__}] {e}")

