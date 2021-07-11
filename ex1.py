#ex1.py

class Demo:
    def __enter__(self):
        print(" calling to __enter__ method")
        return "True"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(" calling to __exit__ method")


def calling_demo():
    return Demo()


with calling_demo() as f:
    print("demo:", f)
