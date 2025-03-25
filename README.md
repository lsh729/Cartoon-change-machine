# Cartoon-change-machine
My Image Cartoon Converter using OpenCV


# 🖼️ Cartoon Image Converter using OpenCV
Python과 OpenCV를 이용하여 일반 이미지를 "만화 스타일"로 변환하는 프로젝트입니다.


## 주요 기능

1. 이미지 크기 조절 | 입력 이미지를 가로 800픽셀 기준으로 리사이징

2.노이즈 제거 | `bilateralFilter`로 윤곽선은 보존하면서 색을 부드럽게 만듬

3.그레이스케일 변환 | 엣지 처리를 위해 컬러 → 흑백 변환

4. 블러 처리 | `medianBlur`로 노이즈 감소 및 경계 부드럽게

5. 윤곽선 추출 | `adaptiveThreshold`로 스케치 느낌의 엣지 생성

6. 합성 처리 | 엣지와 부드러운 색상을 결합해 만화 스타일 완성



a. 표현이 잘 된 이미지
![cartooon1](https://github.com/user-attachments/assets/eb668aeb-d86d-4e87-b450-f9b4fc112a52)

![cartoon4](https://github.com/user-attachments/assets/bb6ffb0a-a054-4914-934a-99a768ba1704)


b. 표현이 잘 표현 되지 않은 이미지

![cartoon3](https://github.com/user-attachments/assets/9645f2e5-b7e5-45ef-9da0-7017abac3a71)


![cartoon2](https://github.com/user-attachments/assets/cc37f3c8-cfcc-4d37-98e9-e8162ea1bca7)


c. 이유와 한계점

밝고 배경이 없어서 경계가 명확하거나 색감이 진한 사진들은 비교적 잘 보이나 어둡거나 배경이 복잡한 사진들은 경계가 무너지고 색감이 지저분해 보이는 경우가 있습니다. 그 이유는 블러 처리와 노이즈를 제거하는 과정에선 Cartoon-change-machine
My Image Cartoon Transducer using OpenCV


# 🖼️ Cartoon Image Converter using OpenCV
Python과 OpenCV를 이용하여 일반 이미지를 "만화 스타일"로 변환하는 프로젝트입니다.


## 주요 기능

1. 이미지 크기 조절 | 입력 이미지를 가로 800픽셀 기준으로 리사이징

2.노이즈 제거 | `bilateralFilter`로 윤곽선은 보존하면서 색을 부드럽게 만듬

3.그레이스케일 변환 | 엣지 처리를 위해 컬러 → 흑백 변환

4. 블러 처리 | `medianBlur`로 노이즈 감소 및 경계 부드럽게

5. 윤곽선 추출 | `adaptiveThreshold`로 스케치 느낌의 엣지 생성

6. 합성 처리 | 엣지와 부드러운 색상을 결합해 만화 스타일 완성



a. 표현이 잘 된 이미지
![cartooon1](https://github.com/user-attachments/assets/eb668aeb-d86d-4e87-b450-f9b4fc112a52)

![cartoon4](https://github.com/user-attachments/assets/bb6ffb0a-a054-4914-934a-99a768ba1704)


b. 표현이 잘 표현 되지 않은 이미지

![cartoon3](https://github.com/user-attachments/assets/9645f2e5-b7e5-45ef-9da0-7017abac3a71)


![cartoon2](https://github.com/user-attachments/assets/cc37f3c8-cfcc-4d37-98e9-e8162ea1bca7)


c. 이유와 한계점

밝고 배경이 없어서 경계가 명확하거나 색감이 진한 사진들은 비교적 잘 보이나 어둡거나 배경이 복잡한 사진들은 경계가 무너지고 색감이 지저분해 보이는 경우가 있습니다. 그 이유는 사진의 입체적인 부분을 지워 평면적으로 만들려고 하다보니 블러 처리와 노이즈를 제거하는 과정에서 이미지가 뭉개지면서 그렇게 보이는 것 같습니다. 더 나은 방법을 찾기 전까진 배경이 없고 경계가 뚜렷한 밝은 사진을 주로 사용해야 될 것 같습니다.
