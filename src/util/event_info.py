def info_me(event):
    print(repr(event))
    print(f"x: {event.x}, y: {event.y}, keysym: {event.keysym}")