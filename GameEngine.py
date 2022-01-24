import tkinter as tk
from PIL import Image,ImageTk
import time

# VARIABLES FOR SETUP
game_setup = False

# VARIABLES FOR THE MAIN LOOP
continue_running = True
frame_rate = (1/30)
frame = 0

# CLASSES AND FUNCTIONS FOR INTERNAL USE
class terminal_colors:
    black = u"\u001b[30m "
    red = u"\u001b[31m "
    green = u"\u001b[32m "
    yellow = u"\u001b[33m "
    blue = u"\u001b[34m "
    magenta = u"\u001b[35m "
    cyan = u"\u001b[36m "
    white = u"\u001b[37m "
    reset = u"\u001b[0m "

def error(text, type="Error"):
    raise Exception(terminal_colors.red + f"[{type}]" + terminal_colors.yellow + text + terminal_colors.reset)

# CLASS USED TO CREATED A NEW SPRITE
class Sprite:
    """
    This is a test description.
    """
    def __init__(self, width, height, **kwargs):
        img = False
        self.width = width
        self.height = height
        if "image" in kwargs:
            img = True
            self.image=kwargs.get("image")
        if "color" in kwargs:
            if img:
                error("A sprite cannot have both an image and a color.", "Sprite Error")
            img = True
            self.color = kwargs.get("color")
        
        if not img:
            error("A sprite must have either an image or color.", "Sprite Error")
    
    def draw_sprite(self, x, y):
        global root
        try:
            if not root:
                pass
        except:
            error("The game must be setup before drawing a sprite.", "Sprite Error")
        self.x = x
        self.y = y
        self.tk_obj = tk.Frame(root, width=self.width, height=self.height)
        self.tk_obj.place(x=self.x, y=self.y)
        if hasattr(self, "color"):
            try:
                self.tk_obj["background"] = self.color
            except:
                error("Invalid sprite color.", "Sprite Error")
        if hasattr(self, "image"):
            img = ImageTk.PhotoImage(Image.open(self.image).resize((self.width, self.height)))
            self.image_label = tk.Label(self.tk_obj, image=img)
            self.image_label.pack()
    
    def hide_sprite(self):
        if self.tk_obj:
            self.tk_obj.place_forget()

class Text:
    def __init__(self):
        pass

# POSSIBLE KWARGS: window_width, window_height, window_name, window_icon, frame_rate, resize_x, resize_y
def setup(**kwargs):
    global frame_rate, game_setup
    if "frame_rate" in kwargs:
        frame_rate = kwargs.get("frame_rate")

    global root, main_frame
    root = tk.Tk()

    if "window_name" in kwargs:
        root.title("window_name")
    else:
        root.title("Game")
    
    if "winow_icon" in kwargs:
        try:
            root.iconphoto(False, tk.PhotoImage(file=kwargs.get("window_icon")))
        except:
            img_loc = kwargs.get("window_icon")
            error(f"Could not find image at '{img_loc}'!", "Setup Error")
    else:
        root.iconphoto(False, tk.PhotoImage(file="Default-Icon-Small.png"))
    
    if "window_width" in kwargs:
        window_width = kwargs.get("window_width")
    else:
        window_width = 500

    if "window_height" in kwargs:
        window_height = kwargs.get("window_height")
    else:
        window_height = 500

    root.geometry(f"{window_width}x{window_height}")
    
    resize_x = True
    resize_y = True

    if "resize_x" in kwargs:
        resize_x = kwargs.get("reize_x")

    if "resize_y" in kwargs:
        resize_y = kwargs.get("resize_y")

    root.resizable(resize_x, resize_y)

    main_frame = tk.Frame(root)
    main_frame.pack()

    game_setup = True

def main_loop():
    global game_setup, frame_rate, frame, continue_running, root
    if not game_setup:
        error("Game not setup. Please use the 'setup()' method.", "Setup Error")
    while continue_running:
        frame += 1
        root.update_idletasks()
        root.update()
        time.sleep(frame_rate)

def update():
    global game_setup, frame, root
    if not game_setup:
        error("Game not setup. Please use the 'setup()' method.", "Setup Error")
    frame += 1
    root.update_idletasks()
    root.update()