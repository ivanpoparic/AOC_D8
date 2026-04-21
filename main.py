#libraries
#-----------------------------------------

#from data import list_of_coords
from test_data import list_of_coords

# classes
#---------------------------------------
class JunctionBox:
    def __init__(self, x_coord, y_coord, z_coord, circuit):
        self.x_coords = x_coord
        self.y_coords = y_coord
        self.z_coords = z_coord
        self.circuit = circuit

# functions
#---------------------------------------
def calculate_distance(box_1, box_2):
    pass


#******************************************
# BEGIN MAIN
#******************************************

# initializing variables
#-----------------------------------------
junction_box=[]
# - create list of junction box objects with properties of x,y,z coordinates and circuit
for i in range(len(list_of_coords)):
    junction_box.append(JunctionBox(list_of_coords[i][0],list_of_coords[i][1],list_of_coords[i][2],0))





