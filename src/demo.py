import cv2
import pytesseract
from spellchecker import SpellChecker

# Load and preprocess image
image_path = 'test3.png'
image = cv2.imread(image_path)

# Grayscale conversion
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Denoise and Thresholding
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
_, thresh_image = cv2.threshold(blur_image, 150, 255, cv2.THRESH_BINARY_INV)

# Resize to improve OCR performance
resized_image = cv2.resize(thresh_image, None, fx=1.5, fy=1.5)

# Perform OCR using Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(resized_image, lang='eng', config='--psm 6')

# Post-processing: Spell-checking
spell = SpellChecker()
words = text.split()
corrected_words = [spell.correction(word) if word in spell.unknown(words) else word for word in words]

# Output corrected text
corrected_text = " ".join(corrected_words)
print(corrected_text)
