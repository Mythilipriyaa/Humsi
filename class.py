class Cat():
    def __init__(self,fur="",eye="",paws=2):
        self.fur=fur
        self.eye=eye
        self.paws=paws
    
    def scratch(self):
        print("Hurr hurrr rrrrrrrruhhhhhh..........nnnnmeawwwwwwwwww.........!! MEAaaaaaaooooooww !!!")
orange_cat=Cat("orange","pink",2)
orange_cat.scratch()
black_cat=Cat("black","pink",4)
x=black_cat.paws
print(x)