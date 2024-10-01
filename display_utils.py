import matplotlib.pyplot as plt
import cv2

def display_images(im_src, object_locations_array, im_dst, object_locations_new, camera_locations):
    plt.figure(figsize=(35, 10))
    plt.subplot(2, 1, 1)
    plt.imshow(cv2.cvtColor(im_src, cv2.COLOR_BGR2RGB))
    plt.scatter(object_locations_array[:, 0, 0], object_locations_array[:, 0, 1], c='red', s=20, marker='o', label='Object Locations')
    plt.title('Source Image (Street View)')
    plt.subplot(2, 1, 2)
    plt.imshow(cv2.cvtColor(im_dst, cv2.COLOR_BGR2RGB))
    plt.scatter(object_locations_new[:, 0, 0], object_locations_new[:, 0, 1], c='yellow', s=10, marker='o', label='Object Locations')
    plt.scatter(camera_locations[:, 0], camera_locations[:, 1], c='green', s=15, marker='o', label='Camera Location')
    plt.title('Destination Image (Bird Eye View) with objects')
    plt.legend()
    plt.show()
