from cvt import get_image_handler as img_cvt
import numpy as np
import requests

def model (obj) : 

    url = "https://api.aiforthai.in.th/lpr-v2"
    payload = {'crop': '1', 'rotate': '1'}
    files = {'image': img_cvt(obj) }
    headers = {'Apikey': "7L7s5NhkHu94NDmfBDkQsIfXiLxO0G9C"}
    
    response = requests.post( url, files=files, headers=headers)
    if response.status_code != 200 :
        return False
    else :
        data = response.json()
        for item in data:
            _object = (item['lpr'])
            xLeftTop = int(item['bbox']['xLeftTop'])
            yLeftTop = int(item['bbox']['yLeftTop'])
            xRightBottom = int(item['bbox']['xRightBottom'])
            yRightBottom = int(item['bbox']['yRightBottom'])

        return _object , xLeftTop,yLeftTop,xRightBottom,yRightBottom

if __name__ == "__main__" :
    import cv2
    img = cv2.imread('licen_2.png')
    x = model(img)
    print(x)
