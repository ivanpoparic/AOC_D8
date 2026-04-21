# libraries
# -----------------------------------------
import operator

from data import list_of_coords
#from test_data import list_of_coords

# classes
# ---------------------------------------
class JunctionBox:
    def __init__(self, id, x_coord, y_coord, z_coord, circuit):
        self.id = id
        self.x_coords = x_coord
        self.y_coords = y_coord
        self.z_coords = z_coord
        self.circuit = circuit


class Connection:
    def __init__(self, distance, primary_box, secondary_box):
        self.distance = distance
        self.primary_box = primary_box
        self.secondary_box = secondary_box


class Circuit:
    def __init__(self, id, list_of_IDs):
        self.id = id
        self.list_of_IDs = list_of_IDs


# functions
# ---------------------------------------
def calculate_distance_sqr(box_1, box_2):
    return (box_1.x_coords - box_2.x_coords) ** 2 + (box_1.y_coords - box_2.y_coords) ** 2 + (
                box_1.z_coords - box_2.z_coords) ** 2


def switch_circuit_definition(old_id, new_id):
    global junction_box_list
    for box in junction_box_list:
        if box.circuit == old_id:
            box.circuit = new_id

def is_all_same_circuit():
    global junction_box_list
    for i in junction_box_list:
        if i.circuit != 0:
            master_circuit = i.circuit
            break
    for j in junction_box_list:
        if j.circuit != master_circuit:
            return False
    return True


# ******************************************
# BEGIN MAIN
# ******************************************

# initializing variables
# -----------------------------------------
spent_connection = 0  # 10 for test data, 1000 for real data
new_circuit_id = 0  # ID for circuit
final_score = 1

junction_box_list = []
connection_list = []
circuit_list = []
circuit_object_list = []
circuit_lengths = []

last_primary_box = None
last_secondary_box = None

# - create list of junction box objects with properties of x,y,z coordinates and circuit
for i in range(len(list_of_coords)):
    junction_box_list.append(JunctionBox(i, list_of_coords[i][0], list_of_coords[i][1], list_of_coords[i][2], 0))

# - create list of possible connections with properties of distance and IDs of junction boxes
for primary_box in junction_box_list:
    for secondary_box in junction_box_list:
        if primary_box.id < secondary_box.id:
            connection_list.append(
                Connection(calculate_distance_sqr(primary_box, secondary_box), primary_box.id, secondary_box.id))

connection_list.sort(key=operator.attrgetter('distance'))

for connection in connection_list:
    print(connection.distance, connection.primary_box, connection.secondary_box)

    # if both junction boxes are not in a circuit
    if junction_box_list[connection.primary_box].circuit == 0 and junction_box_list[
        connection.secondary_box].circuit == 0:
        new_circuit_id += 1
        circuit_list.append(new_circuit_id)
        print(
            f"Made new connection between box{junction_box_list[connection.primary_box].id} on circuit {junction_box_list[connection.primary_box].circuit} "
            f" and box{junction_box_list[connection.secondary_box].id} on circuit {junction_box_list[connection.secondary_box].circuit}")
        junction_box_list[connection.primary_box].circuit = new_circuit_id
        junction_box_list[connection.secondary_box].circuit = new_circuit_id
        spent_connection += 1
        print(f"Remaining connections: {spent_connection}")
    elif junction_box_list[connection.primary_box].circuit == 0 and junction_box_list[
        connection.secondary_box].circuit != 0:
        print(
            f"Made new connection between box{junction_box_list[connection.primary_box].id} on circuit {junction_box_list[connection.primary_box].circuit} "
            f" and box{junction_box_list[connection.secondary_box].id} on circuit {junction_box_list[connection.secondary_box].circuit}")
        junction_box_list[connection.primary_box].circuit = junction_box_list[connection.secondary_box].circuit
        spent_connection += 1
        print(f"Remaining connections: {spent_connection}")
    elif junction_box_list[connection.primary_box].circuit != 0 and junction_box_list[
        connection.secondary_box].circuit == 0:
        print(
            f"Made new connection between box{junction_box_list[connection.primary_box].id} on circuit {junction_box_list[connection.primary_box].circuit} "
            f" and box{junction_box_list[connection.secondary_box].id} on circuit {junction_box_list[connection.secondary_box].circuit}")
        junction_box_list[connection.secondary_box].circuit = junction_box_list[connection.primary_box].circuit
        spent_connection += 1
        print(f"Remaining connections: {spent_connection}")
    elif junction_box_list[connection.primary_box].circuit == junction_box_list[connection.secondary_box].circuit:
        print(f"Already connected")
        print(
            f"No connection made between box{junction_box_list[connection.primary_box].id} on circuit {junction_box_list[connection.primary_box].circuit} "
            f" and box{junction_box_list[connection.secondary_box].id} on circuit {junction_box_list[connection.secondary_box].circuit}")
        print(f"Remaining connections: {spent_connection}")
        spent_connection += 1
    else:
        old_connection = junction_box_list[connection.secondary_box].circuit
        print(
            f"Switching connection of circuit {junction_box_list[connection.secondary_box].circuit} to circuit {junction_box_list[connection.primary_box].circuit}")
        switch_circuit_definition(junction_box_list[connection.secondary_box].circuit,
                                  junction_box_list[connection.primary_box].circuit)
        spent_connection += 1
        print(f"Remaining connections: {spent_connection}")
        circuit_list.remove(old_connection)


    print(circuit_list)

    if is_all_same_circuit():
        last_primary_box = connection.primary_box
        last_secondary_box = connection.secondary_box
        break

print(last_primary_box)
print(last_secondary_box)

final_score=junction_box_list[last_primary_box].x_coords*junction_box_list[last_secondary_box].x_coords
print(final_score)
"""
# - create list of circuit objects with circuit ID and list of box ID belonging to that circuit
for junction_box in junction_box_list:
    print(junction_box.id, junction_box.circuit)
    list_of_ids = []
    if junction_box.circuit not in circuit_list and junction_box.circuit != 0:
         circuit_object_list.append(Circuit(junction_box.circuit, list_of_ids))

for circuit_object in circuit_object_list:
    for junction_box in junction_box_list:
        if junction_box.circuit == circuit_object.id:
            circuit_object.list_of_IDs.append(junction_box.id)
    print(circuit_object.id, circuit_object.list_of_IDs)
    circuit_lengths.append(len(circuit_object.list_of_IDs))

circuit_lengths.sort(reverse=True)

for i in range(3):
    print(circuit_lengths)
    final_score *= circuit_lengths[i]

print(final_score)
"""







