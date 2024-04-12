import os

class Resource:

    def path(self, file):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(curr_dir, file)


resource = Resource()
