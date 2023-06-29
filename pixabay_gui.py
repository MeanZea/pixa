import tkinter as tk
from tkinter import filedialog

import pixabay.core
import os

def download_images():
    # Initialize pixabay API
    px = pixabay.core("37377099-92dcf57dd3834f06f0e3ec044")
    
    # Query for images
    query = entry.get()
    images = px.query(query)
    
    # Create download directory
    download_path = os.path.join(os.getcwd(), "pixabay_result")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Download images
    for i, image in enumerate(images):
        image.download(download_path, filename=f"{query}_{i}.jpg", size="largeImage")
    
    # Show download path
    result_label.config(text=f"Images downloaded to:\n{download_path}")

# Create tkinter window
window = tk.Tk()
window.title("Pixabay Image Downloader")

# Create GUI elements
label = tk.Label(window, text="Enter search query:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Download Images", command=download_images)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Run the tkinter event loop
window.mainloop()
