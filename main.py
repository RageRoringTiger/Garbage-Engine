import GameEngine as GE

GE.setup(resize_x=False, resize_y=False)

text = GE.Gui.Text("test")

o = GE.Sprite(50, 50, color="red")
a = GE.Sprite(50, 50, color="blue")
s = GE.Sprite(50, 50, image="Default-Icon.png")

o.draw_sprite(10, 10)
a.draw_sprite(70, 10)
s.draw_sprite(150, 10)

def up():
    o.move_sprite(o.x, o.y - 10)
def down():
    o.move_sprite(o.x, o.y + 10)
def left():
    o.move_sprite(o.x - 10, o.y)
def right():
    o.move_sprite(o.x + 10, o.y)

GE.KeyPress("w", up)
GE.KeyPress("s", down)
GE.KeyPress("a", left)
GE.KeyPress("d", right)

GE.main_loop()

# import GameEngine as GE
# GE.setup(resize_x=False, resize_y=False)
# sprite = GE.Sprite(50, 50, color="red")
# sprite.draw_sprite(10, 10)
# sprite1 = GE.Sprite(50, 50, color="orange")
# sprite1.draw_sprite(60, 10)
# sprite2 = GE.Sprite(50, 50, color="yellow")
# sprite2.draw_sprite(110, 10)
# sprite3 = GE.Sprite(50, 50, color="green")
# sprite3.draw_sprite(160, 10)
# sprite4 = GE.Sprite(50, 50, color="blue")
# sprite4.draw_sprite(210, 10)
# sprite5 = GE.Sprite(50, 50, color="purple")
# sprite5.draw_sprite(260, 10)
# GE.main_loop()