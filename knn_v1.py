import csvreader

class mydataframe():
    def __init__(self):
        self.X_train = []
        self.Y_train = []
        self.X_scale = []
        self.Y_scale = []
        self.k = 3
    
    def readfile(self, filename):
        pass

    def scale(self):
        min_X = min(self.X_train)
        X_mined = []
        for i in self.X_train:
            X_mined.append(i-min_X)
        max_X = max(X_mined)
        for j in X_mined:
            self.X_scale.append(j/max_X)

        min_Y = min(self.Y_train)
        Y_mined = []
        for i in self.Y_train:
            Y_mined.append(i-min_Y)
        max_Y = max(Y_mined)
        for j in Y_mined:
            self.Y_scale.append(j/max_Y)

    def checkdist(self, p):
        # from p to all others
        pass

    def is_punctual(self,p):
        # is p in time?
        pass

