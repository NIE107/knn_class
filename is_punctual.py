import csvreader

class mydataframe():
    def __init__(self):
        self.X_train = []
        self.Y_train = []
        self.X_scale = []
        self.Y_scale = []
        self.k = 3
        self.punctual = []
    
    def readfile(self, filename):
        pass

    def scale(self):
        pass

    def checkdist(self, p):
        # from p to all others
        pass

    def is_punctual(self, indexes):
        punctuality = 0
        punctuality_list = []
        for index in indexes:
            punctuality_list.append(self.punctual[indexes])
        for point in punctuality_list:
            if punctuality_list:
                punctuality += 1
            else:
                punctuality -= 1
        if punctuality > 0:
            return True
        else:
            return False

def check_distance(point_one, point_two):
    return 0.1

def check_all_distances(check_point, points):
    all_points = []
    for point in points:
        check_distance(check_point, point)
