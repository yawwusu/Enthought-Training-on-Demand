
# Great Circle Exercise
# =====================
# 
# The shortest distance between two points on the globe, assuming it is perfectly spherical, is the length of the  _great circle_ path.  If you are given two locations in latitude and longitude, then the [Haversine Formula](http://en.wikipedia.org/wiki/Haversine_formula) gives this shortest distance in a numerically stable way:
# 
# $a = \sin^{2}(\Delta \phi/2) + \cos(\phi_{1})\cos(\phi_{2})\sin^{2}(\Delta \lambda/2)$
# 
# $c = 2 \arcsin(\sqrt{a})$
# 
# $d = rc$
# 
# Where $\phi_{i}$ is latitude and $\lambda_{i}$ is the longitude of point $i$ and $r$ is the radius of the globe.
# 
# Question 1
# ----------
# 
# Write a function that takes as inputs a `radius` and two points specified by tuples of `(latitude, longitude)` and returns the distance between the points along a great circle.


from math import sin, cos, asin, radians    


# Hint: Remember to convert your angles to radians.


# your code goes here



# test your answer: should be roughly 7895 km
r_earth = 6371.0 # km
austin = (30.2500, -97.7500)
cambridge = (52.2050, 0.1190)

print round(haversine_formula(r_earth, austin, cambridge))


# Question 2
# ----------
# 
# Given the list of cities from the "Flight Distances" exercise, and their latitude and longitudes:


cities = {
    'Atlanta': (33.7569444444, -84.3902777778),
    'Austin': (30.3, -97.7333333333),
    'Boston': (42.3577777778, -71.0616666667),
    'Chicago': (41.9, -87.65),
    'Dallas': (32.7825, -96.7975),
    'Denver': (39.7391666667, -104.984722222),
    'Houston': (29.7627777778, -95.3830555556),
    'Los Angeles': (34.05, -118.25),
    'Miami': (25.7833333333, -80.2166666667),
    'New York': (40.67, -73.94),
    'San Francisco': (37.7666666667, -122.433333333),
    'Seattle': (47.6, -122.316666667),
}


# write a function that, given a dictionary of city names and locations, plus the names of two cities, returns the great circle distance between the two cities.  The result should be rounded to the nearest 10 km.
# 
#     def city_distance(cities, city_1, city_2):
#         ...

# Hint: The built-in `round()` function takes an optional second argument for the number of digits of precision.  This argument can be negative.


# your code goes here



print city_distance(cities, "Austin", "San Francisco")


# Question 3
# ----------
# 
# Write a function that, given a set of cities returns a dictionary whose keys are pairs of cities and whose values are the distances between them.  You should use an appropriate data structure for the keys, and round distances to the nearest 10 km.
# 
#     def compute_distances(cities):
#         ...
# 
# Bonus points if you compute the distance for a given pair of cities only once.

# Hint: Have a look at the `flight_distances` exercise in the Frozenset lecture for a possible data structure.


# your code goes here



compute_distances(cities)

