import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread("image.jpg") 

# 이미지 크기 조절
height, width = img.shape[:2]
new_width = 800
scale = new_width / width
new_height = int(height * scale)
img = cv2.resize(img, (new_width, new_height))


# 노이즈 제거 
color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)


# 그레이스케일
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 블러
blur = cv2.medianBlur(gray, 7)

# 엣지
edges = cv2.adaptiveThreshold(blur, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY,
                              blockSize=9,
  C=2)


# 컬러, 엣지 결합
cartoon = cv2.bitwise_and(color, color, mask=edges)

# 결과 출력
cv2.imshow("Original", img)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
