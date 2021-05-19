import random
import copy


class DoubleColorBallLottery:
    def __init__(self):
        self.red_max_num = 33
        self.blue_max_num = 16
        self.red_times = 6
        self.blue_times = 1

        self.red_balls = [i for i in range(1, self.red_max_num+1)]
        self.blue_balls = [i for i in range(1, self.blue_max_num+1)]

        # print(len(red_balls))

    def print_ticket(self):
        red_balls_copy = copy.copy(self.red_balls)
        blue_balls_copy = copy.copy(self.blue_balls)
        ticket = {}
        red_ball = []
        blue_ball = []
        for i in range(self.red_times):
            index = random.randint(0, len(red_balls_copy)-1)
            rb = red_balls_copy.pop(index)
            red_ball.append(rb)

        for i in range(self.blue_times):
            index = random.randint(0, len(blue_balls_copy)-1)
            bb = blue_balls_copy.pop(index)
            blue_ball.append(bb)

        red_ball.sort()
        blue_ball.sort()

        ticket['red_ball'] = red_ball
        ticket['blue_ball'] = blue_ball
        print(ticket)

    def print_tickets(self, times):
        ticket_list = []
        for time in range(times):
            red_balls_copy = copy.copy(self.red_balls)
            blue_balls_copy = copy.copy(self.blue_balls)
            ticket = {}
            red_ball = []
            blue_ball = []
            for i in range(self.red_times):
                index = random.randint(0, len(red_balls_copy)-1)
                rb = red_balls_copy.pop(index)
                red_ball.append(rb)

            for i in range(self.blue_times):
                index = random.randint(0, len(blue_balls_copy)-1)
                bb = blue_balls_copy.pop(index)
                blue_ball.append(bb)

            red_ball.sort()
            blue_ball.sort()

            ticket['red_ball'] = red_ball
            ticket['blue_ball'] = blue_ball
            print(ticket)

            ticket_list.append(ticket)


d = DoubleColorBallLottery()
d.print_tickets(5)
