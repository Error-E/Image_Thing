import io
import cv2

def get_image_handler(img_arr):
    ret, img_encode = cv2.imencode('.jpg', img_arr)
    str_encode = img_encode.tobytes()
    img_byteio = io.BytesIO(str_encode)
    img_byteio.name = 'img.jpg'
    reader = io.BufferedReader(img_byteio)
    return reader

if __name__ == "__main__":
    img = cv2.imread("licen_3.jpg")
    #img = get_image_handler(img)
    print(img)
