import cv2
import os

# List all files in the current directory for debugging
print("Files in the current directory:")
for file in os.listdir("."):
    print(file)  # This will print all files in the current directory

# Read the image
img = cv2.imread("landscape.jpg")  # Update this line with your image file name

# Ensure image is loaded
if img is None:
    raise FileNotFoundError("Image not found")  # Raise error if image is not found

# Get image dimensions
height, width, _ = img.shape

# Get message and password from user
msg = input("Enter secret message: ")
password = input("Enter password: ")

# Check if the message can fit into the image
if len(msg) * 3 > height * width:
    raise ValueError("Message is too long to fit in the image")

# Character to ASCII mapping
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Encode the message into the image
index = 0
for i in range(len(msg)):
    row = index // width
    col = index % width
    img[row, col, 0] = d[msg[i]]
    index += 1

# Save the encrypted image
cv2.imwrite("Encryptedmsg.jpg", img)
print("Message encrypted and saved to Encryptedmsg.jpg")

# Decryption
message = ""
index = 0

# Get decryption password
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        row = index // width
        col = index % width
        message += c[img[row, col, 0]]
        index += 1
    print("Decrypted message:", message)
else:
    print("Invalid key")
