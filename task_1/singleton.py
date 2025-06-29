class Singleton(type):
    
    _instances = {}
    
    def __call__(self, *args, **kwds):
        if self not in self._instances:
            self._instances[self] = super().__call__(*args, **kwds)
        return self._instances[self]


class Logger(metaclass=Singleton):
    def __init__(self):
        self._logs = []
    
    def log(self, message):
        self._logs.append(message)

    def get_logs(self):
        return self._logs


logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]
