class Singleton(type):
    """A class where only one instance is ever created

    Args:
        type (_type_): _description_
    """
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        return self.__instance
    
    
class Spam(metaclass=Singleton):
    def __init__(self):
        print("Creating Spam")
        
