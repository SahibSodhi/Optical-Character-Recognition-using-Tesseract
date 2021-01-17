from PIL import Image
import pytesseract
# Replace test.png with your image name
img = Image.open("test.png")
text = pytesseract.image_to_string(img, lang="en")
print(text)