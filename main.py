import GameEngine as GE

o = GE.Sprite(50, 50, color="red")

GE.setup()

o.draw_sprite(10, 10)

GE.main_loop()