import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic

#カスケードファイルを指定して分類機を作成
cascade_file = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

#画像の読み込んでグレイスケールに変換
img = cv2.imread("emma.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#顔検出を実行
face_list = cascade.detectMultiScale(img_gray, minSize=(150, 150))
if len(face_list) == 0:
    quit()

#認識した部分の画像にモザイクをかける
for (x,y,w,h) in face_list:
    img = mosaic(img, (x,y, x+w, y+h), 10)

#画像出力
cv2.imwrite("out-mosaic.jpg", img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()