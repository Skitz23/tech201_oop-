from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.venom = None
        self.two_lungs = True

    def digest_large_prey(self):
        print("Ok, let me get the stretchy pants")

    def climb(self):
        print("up we go")

    def shed_skin(self):
        print("im growing out this now")

peter = Python()
peter.breathe()
peter.use_tongue_to_smell()
peter.hunt()
peter.shed_skin()