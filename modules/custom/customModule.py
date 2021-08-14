class CustomModule:
    def __init__(self):
        self.a=None

    def apply(self,param):
        print(param)
        return 'something'+param