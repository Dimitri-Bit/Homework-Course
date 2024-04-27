def is_covering_curtain(curtain_top_left, curtain_bottom_right, window_top_left, window_bottom_right):
    curtain_width = curtain_bottom_right[0] - curtain_top_left[0]
    curtain_height = curtain_bottom_right[1] - curtain_top_left[1]
    
    window_width = window_bottom_right[0] - window_top_left[0]
    window_height = window_bottom_right[1] - window_top_left[1]
    
    return curtain_width >= window_width and curtain_height >= window_height

curtain_top_left = tuple(map(int, input("top left coordinate of the curtain (x y): ").split()))
curtain_bottom_right = tuple(map(int, input("bottom right coordinate of the curtain (x y): ").split()))

window_top_left = tuple(map(int, input("top left coordinate of the window (x y): ").split()))
window_bottom_right = tuple(map(int, input("bottom right coordinate of the window (x y): ").split()))

if is_covering_curtain(curtain_top_left, curtain_bottom_right, window_top_left, window_bottom_right):
    print("curtain will cover the window.")
else:
    print("curtain will not cover the window.")
