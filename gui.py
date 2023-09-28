import tkinter as tk
from PIL import Image, ImageTk

# Create a Tkinter window
window = tk.Tk()
window.title("J.A.R.V.I.S.")
window.geometry("500x400")

# Load the GIF image
gif = Image.open("gui2.gif")
frames = []
try:
    while True:
        frames.append(ImageTk.PhotoImage(gif))
        gif.seek(len(frames))  # skip to next frame
except EOFError:
    pass  # end of sequence
frame_index = 0

# Define a function to animate the GIF image
def animate_gif():
    global frame_index
    frame_index += 1
    if frame_index == len(frames):
        frame_index = 0
    gif_label.configure(image=frames[frame_index])
    gif_label.image = frames[frame_index]  # keep a reference to avoid garbage collection
    window.after(20, animate_gif)  # update every 100 milliseconds



# Create a label to display the GIF image
gif_label = tk.Label(window, image=frames[0])
gif_label.pack()

# Start animating the GIF image
animate_gif()

# Start the Tkinter event loop
window.mainloop()


