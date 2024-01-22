def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = 0
    position = -30001
    for route in routes:
        if route[0] > position:
            camera += 1
            position = route[1]
    return camera
