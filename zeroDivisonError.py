#ZeroDivisionError.py

class Demo:
    def __init__(self, x, y):
        print("Enter __init__")
        self.x = x
        self.y = y
  
    def __enter__(self):
        print("Find the __enter__")
        return self
  
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("\Find the __exit__")
        print("\ntype: ", exc_type)
        print("\nvalue: ", exc_val)
        print("\nTraceback: ", exc_tb)
  
    def exceptionDemo(self):
        # ZeroDivisionError exception
        print(self.x / self.y)
  
  
# with statement not raise exception
with Demo(4, 2) as f:
    f.exceptionDemo()
  
print("\n\n=======================================\n\n")
  
# with statement will raise a ZeroDivisionError
with Demo(1, 0) as f:
    f.exceptionDemo()