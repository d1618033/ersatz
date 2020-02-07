class InvalidCall(BaseException):
    def __init__(self, function, args, kwargs):
        self.args = args
        self.function = function
        self.kwargs = kwargs

    def __repr__(self):
        return f"Invalid call to mock function {self.function.__name__} with {self.args}, {self.kwargs}"
