import non_existing_module

class MyClass:
    def __init__(self):
        self.attribute1 = "attr1"

    def get_non_existing_attr(self):
        value = non_existing_module.get_non_existing_attr()
        return self.attribute1 + value