import tkinter as tk
from capture_live import capture
from image_picker import recognise_from_image

def run():
    root = tk.Tk()
    root.title("NZ Coin Recognition")
    root.geometry("200x200")

    # Button for capturing live video for real-time recognition
    capture_button = tk.Button(root, text="Real-time Recognition", command=lambda: capture)
    capture_button.pack(pady=25)

    # Button for recognition with individual images from files
    detect_button = tk.Button(root, text="Detect with Image", command=recognise_from_image)
    detect_button.pack(pady=25)

    root.mainloop()


if __name__ == "__main__":
    run()