# Methods

class MethodExamples:

#    this_can_be_accessed_easily = "Hi i am easily found!"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi i am easily found!"

x = MethodExamples()

print(x._this_can_be_accessed_easily)
x.set_this_can_be_accessed_easily = ("I have been changed!")
print(x._this_can_be_accessed_easily)



