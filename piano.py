import pgzrun
def on_key_down(key):
    if key == keys.SPACE:
        print("SPACE")
        music.play_once('Piano11')

    elif key == keys.UP:
        print("UP")

    elif key == keys.DOWN:
        print("DOWN")

    elif key == keys.LEFT:
        print("LEFT")

    elif key == keys.RIGHT:
        print("RIGHT")

pgzrun.go()