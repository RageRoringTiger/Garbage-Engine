import GameEngine as GE

o = GE.Sprite(50, 50, color="red")
a = GE.Sprite(50, 50, image="Default-Icon.png")

GE.setup(resize_x=False, resize_y=False)

o.draw_sprite(10, 10)
a.draw_sprite(60, 60)

GE.main_loop()