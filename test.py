class One:
    def __init__(self):
        print("One!!!!")


class Two(One):
    def __init__(self):
        super().__init__()
        print("Two!!!!")

Two()