import math

def Check_circle_collision(mouse_pos, targX, targY, circle_rad) -> bool:
    return (math.sqrt(math.pow(mouse_pos[0] - targX, 2) + math.pow(mouse_pos[1] - targY, 2)) <= circle_rad)