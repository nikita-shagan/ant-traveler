from PIL import Image, ImageDraw

RIGHT = 0
TOP = 90
LEFT = 180
BOTTOM = 270
BLACK = 'black'
WHITE = 'white'


class Map:
    def __init__(self, size):
        self.dots_count = 0
        self.size = size
        self.map = [[0 for _ in range(size)] for _ in range(size)]
        self.image = Image.new('RGB', (size, size), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

    def draw_dot(self, x, y, color):
        if color == BLACK:
            self.map[x][y] = 1
            self.dots_count += 1
        else:
            self.map[x][y] = 0
            self.dots_count -= 1
        self.draw.rectangle([x, y, x + 1, y + 1], fill=color, width=0)

    def save_map_image(self):
        self.image.save('res.png')


class Ant:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y

    def turn_right(self):
        self.direction = (self.direction - 90) % 360

    def turn_left(self):
        self.direction = (self.direction + 90) % 360

    def move_forward(self):
        if self.direction == TOP:
            self.y -= 1
        elif self.direction == BOTTOM:
            self.y += 1
        elif self.direction == RIGHT:
            self.x += 1
        elif self.direction == LEFT:
            self.x -= 1

    def go(self, route_map: Map):
        while 0 <= self.x < route_map.size and 0 <= self.y < route_map.size:
            if route_map.map[self.y][self.x] == 0:
                self.turn_right()
                route_map.draw_dot(self.y, self.x, BLACK)
                self.move_forward()
            else:
                self.turn_left()
                route_map.draw_dot(self.y, self.x, WHITE)
                self.move_forward()


if __name__ == '__main__':
    ant_map = Map(1024)
    ant = Ant(TOP, 511, 511)
    ant.go(ant_map)
    ant_map.save_map_image()
    print(ant_map.dots_count)
