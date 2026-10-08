import cv2
from PIL import Image

img_path = "cat.jpg"
cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
image = cv2.imread(img_path)
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)

cat = Image.open(img_path)
glasses = Image.open("okulary.png")
cat = cat.convert("RGB")
glasses = glasses.convert("RGB")

for (x,y,w,h) in cat_face:
    # cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 3)
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)))
    cat.save("cat_glasses.png")
    cat_glass = cv2.imread("cat_glasses.png")
    cv2.imshow("Cat", cat_glass)
    cv2.waitKey()