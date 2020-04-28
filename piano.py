import pgzrun
def on_key_down(key):
    if key == keys.SPACE:
        print("SPACE")
        music.play_once('piano11')

    elif key == keys.UP:
        print("UP")
        music.play_once('piano12')

    elif key == keys.DOWN:
        print("DOWN")
        music.play_once('piano13')

    elif key == keys.LEFT:
        print("LEFT")
        music.play_once('piano14')
    elif key == keys.RIGHT:
        print("RIGHT")
        music.play_once('piano16')

pgzrun.go()