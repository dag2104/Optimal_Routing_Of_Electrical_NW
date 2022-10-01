# Everything to get from frontend
N = 10  # No of users
M = 5  # No of Transformers
S = 1  # No of Substations

P = N + M + S

# JUST FOR TESTING PURPOSE
X = [x for x in range(P)]  # Longitude matrix
Y = [x for x in range(P)]  # Latitude Matrix
R = 9999999999  # Range of LV connections
########################################## AKSHAT #############################

from pyrosm import OSM
from pyrosm import get_data

# Pyrosm comes with a couple of test datasets 
# that can be used straight away without
# downloading anything
fp = get_data("test_pbf")

# Initialize the OSM parser object
osm = OSM(fp)

# Read all drivable roads
# =======================
drive_net = osm.get_network(network_type="driving")
drive_net.plot()
