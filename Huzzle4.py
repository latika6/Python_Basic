def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()

def step():
    turn_right()
    move()

while not at_goal():
    if wall_in_front() and not right_is_clear():
        jump()
    elif right_is_clear():
        step()
    elif wall_in_front() and right_is_clear():
        turn_left()
    elif right_is_clear() and not wall_in_front():
        turn_right()
    else:
        move()
