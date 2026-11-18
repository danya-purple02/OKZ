def load_image(image_path):
    import cv2 as cv
    image = cv.imread(image_path)
    return image
    
def display_image(image):
    import cv2 as cv
    cv.imshow('Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()