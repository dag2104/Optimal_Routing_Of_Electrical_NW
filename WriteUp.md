# Problem Statement
The unpredictable increase in electricity demand has challenged the design and planning of
any electrical system in transmission or distribution level. The population growth, migration
and city planning had reduced the performance of the Electric Distribution Systems (EDS) in
large cities, especially in third world countries.
This Project tackles this increase in demand by automating the process of Implementing EDS
systems with formal considerations of planning and/or project demand in view of
georeferenced data.

# Overview
This project aims to implement a system to find the optimal routing of an electrical distribution
system. This Project employs the PRIM algorithm as a graph search heuristic. The system routes
an electrical distribution network in a georeferenced area, taking into account the
characteristics of the terrain, such as streets or intersections, and scenarios without squared
streets.

# Objectives
1) To ensure efficient and complete connectivity between substation and end users.
2) To find the most cost efficient way of implementing EDS.

# Solution Methodology
### Step 1: Acquisition of georeferenced data
We require data of user locations, possible transformer locations (Along the highway/streets) and
the connection between streets. We are extracting both data from OSM (OpenStreetMap). We
will be storing location data of user and possible transformer locations in a latitude-longitude
array and data of connection between streets is stored in an adjacency matrix (Matrix
representation of a graph).
### Step 2: Layer 1 implementation:
We begin by declaring the required variables which are received from the georeferenced data.
From all the possible transformer locations, we utilize K-Medoids algorithm to find the optimal
transformer locations (Exact methodology under research).We utilize PRIM’s algorithm to
determine the optimal connection between the transformers.
### Step 3: Layer 2 implementation:
Layer 2 determines the connections between transformer and end users. This is implemented by
first finding the distances between users and transformers and then applying dijkstra to find the
nearest transformer from a user and then making connections between the users and connecting
users to the nearest transformer using PRIM’s algorithm.
### Step 4: Layer 3 implementation:
This layer allows us to determine the allocation of the rooftop photo-voltaic panels in the houses.
First we collect all the coordinates in one array. After that, each house’s rooftop photovoltaic
contribution is determined and stored in one array. And all the photovoltaic contribution is added
to the network
