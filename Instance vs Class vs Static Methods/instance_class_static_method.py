class MyClass:
    def instance_method(self):
        print("Called instance method")

    @classmethod
    def class_method(cls):
        print("Called class method")

    @staticmethod
    def static_method():
        print("Called static method")

obj = MyClass()
obj.instance_method()   # Called instance method
MyClass.class_method()  # Called class method
MyClass.static_method() # Called static method