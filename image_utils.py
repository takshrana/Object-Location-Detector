import cv2

def load_and_resize_image(file_path, size=(1024, 768)):
    return cv2.resize(cv2.imread(file_path), size)

def select_points(image, window_name):
    points = []
    def select_point(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))
            cv2.circle(image, (x, y), 5, (255, 0, 0), -1)
            cv2.imshow(window_name, image)
    cv2.imshow(window_name, image)
    cv2.setMouseCallback(window_name, select_point)
    while True:
        key = cv2.waitKey(0)
        if key == 27:  # 'Esc' key
            break
    cv2.destroyAllWindows()
    return points
