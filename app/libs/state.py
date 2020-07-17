from libs.files import FileManager

class State:
    _defaults = {
        'status': 400
    }

    def __init__(self, **kwargs):
        """
        :param event:
        :type even: dict
        """
        self.files: FileManager = FileManager(**kwargs)