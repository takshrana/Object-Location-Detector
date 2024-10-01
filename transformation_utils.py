import numpy as np
import math
from geopy.distance import geodesic
from geopy.point import Point

def calculate_real_world_distance(camera_gps_1, camera_gps_2, camera_locations):
    real_world_distance = geodesic(camera_gps_1, camera_gps_2).meters
    delta_x = camera_locations[1][0] - camera_locations[0][0]
    delta_y = camera_locations[1][1] - camera_locations[0][1]
    pixel_distance = math.sqrt(delta_x**2 + delta_y**2)
    scale = real_world_distance / pixel_distance
    return scale

def rotate_and_translate_points(object_locations, camera_locations, angle):
    angle = math.radians(angle)
    for object_location in object_locations:
        x = object_location[0][0]
        y = object_location[0][1]
        x += camera_locations[1][0] - camera_locations[0][0]
        y += camera_locations[1][1] - camera_locations[0][1]
        translated_x = x - camera_locations[1][0]
        translated_y = y - camera_locations[1][1]
        rotated_x = translated_x * math.cos(angle) - translated_y * math.sin(angle)
        rotated_y = translated_x * math.sin(angle) + translated_y * math.cos(angle)
        object_location[0][0] = rotated_x + camera_locations[1][0]
        object_location[0][1] = rotated_y + camera_locations[1][1]
    return object_locations

def calculate_gps_coordinates(object_locations, camera_locations, camera_gps, scale):
    objects_gps = []
    for object_location in object_locations:
        dx = object_location[0][0] - camera_locations[1][0]
        dy = object_location[0][1] - camera_locations[1][1]
        pixel_distance = math.sqrt(dx**2 + dy**2)
        real_world_distance_object = pixel_distance * scale
        bearing = math.degrees(math.atan2(dy, dx))
        object_gps = geodesic(meters=real_world_distance_object).destination(Point(camera_gps[0], camera_gps[1]), bearing)
        objects_gps.append([object_gps.latitude, object_gps.longitude, f"https://www.google.com/maps?q={object_gps.latitude},{object_gps.longitude}"])
    return objects_gps
