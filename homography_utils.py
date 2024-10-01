import numpy as np
import cv2

def compute_homography(pts_src, pts_dst):
    pts_src = np.array(pts_src)
    pts_dst = np.array(pts_dst)
    h, status = cv2.findHomography(pts_src, pts_dst, cv2.RANSAC)
    return h

def transform_points(h, points):
    points_array = np.array(points, dtype=np.float32).reshape(-1, 1, 2)
    transformed_points = cv2.perspectiveTransform(points_array, h)
    return transformed_points
