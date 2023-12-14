import cv2
import torch
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from matplotlib import pyplot as plt

def load_image(loc):
    img = cv2.imread(str(loc))
    if img is None:
        raise FileNotFoundError(f"Image not found at {loc}")
    return img

def rgb2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def show_image(img):
    plt.imshow(img, cmap='gray')  # Assuming img is grayscale
    plt.axis('off')
    plt.show()

def convert_to_tensor(img):
    return torch.from_numpy(img)

def preprocess_image(image_location, threshold=100):
    img = load_image(image_location)
    gray = rgb2gray(img)
    bw = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)[1]
    return bw

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Processing GUI")

        self.label = tk.Label(self, text="Select an image:")
        self.label.pack(pady=10)

        self.button = tk.Button(self, text="Browse", command=self.browse_image)
        self.button.pack(pady=10)

        self.threshold_entry = tk.Entry(self, width=10)
        self.threshold_entry.insert(0, "100")
        self.threshold_entry.pack(pady=10)

        self.process_button = tk.Button(self, text="Process Image", command=self.process_image)
        self.process_button.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        self.label.config(text=f"Selected Image: {file_path}")

    def process_image(self):
        threshold = int(self.threshold_entry.get())
        file_path = self.label.cget("text").split(": ")[1]

        preprocessed_img = preprocess_image(file_path, threshold)
        tensor_img = convert_to_tensor(preprocessed_img)

        show_image(preprocessed_img)

    

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
