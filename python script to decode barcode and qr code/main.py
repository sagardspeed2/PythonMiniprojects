import cv2
import numpy as np
from pyzbar.pyzbar import decode

inputImage = input("\n Selec the barcode or QR code image : ")

codeImage = cv2.imread(inputImage)

decodeCode = decode(codeImage)

for CodeImg in decodeCode:
    print("\nCode Type : ", CodeImg.type)
    print("\nCode Data : ", CodeImg.data)

    points = CodeImg.polygon

    if len(points) > 4:
        conHull = cv2.convexHull(np.array([pts for pts in points], dtype=np.float32))

        conHull = list(map(tuple, np.squeeze(conHull)))

    else:
        conHull = points

    n = len(points)

    for j in range(0, n):
        cv2.line(codeImage, conHull[j], conHull[(j + 1) % n], (0, 0, 255), 2)

cv2.imshow("Decode Code : ", codeImage)
cv2.waitKey(0)