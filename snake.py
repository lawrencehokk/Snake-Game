


class Snake:
    def __init__(self):
        self.speed = 10
        self.head = [100, 50]
        self.body = [[100,50], [90,50], [80, 50], [70, 50]]
        self.direction = "RIGHT"
        self.change_direction = self.direction

    def move(self):
        self.body.insert(0, list(self.head))
        if self.change_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        if self.change_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'

        if self.direction == 'RIGHT':
            self.head[0] = self.head[0] + 10
        if self.direction == 'LEFT':
            self.head[0] = self.head[0] - 10
        if self.direction == 'UP':
            self.head[1] = self.head[1] - 10
        if self.direction == 'DOWN':
            self.head[1] = self.head[1] + 10

    def add_length(self, collided):
        if collided == False:
            self.body.pop(len(self.body)-1)

    def hit_body(self):
        for i in range(1, len(self.body)):
            if self.head[0] == self.body[i][0] and self.head[1] == self.body[i][1]:
                return True
        return False

    def hit_wall(self, screen_width, screen_height):
        if self.head[0] < 0 or self.head[0]>screen_width-10:
            return True
        if self.head[1] < 0 or self.head[1]>screen_height-10:
            return True
        return False