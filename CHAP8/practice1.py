#delete an object

class tree:
    def __init__(self,leaves,branch):
        self.leaves=leaves
        self.branch=branch

t1=tree("palmtreeleaves","brown")
del t1
print(t1.leaves,t1.branch)
