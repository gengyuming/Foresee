import random
import copy

from Core.logger import log

double_color_ball = {
    'red_max_no': 33,
    'blue_max_no': 16,
    'red_times': 6,
    'blue_times': 1
}

lotto = {
    'red_max_no': 35,
    'blue_max_no': 12,
    'red_times': 5,
    'blue_times': 2
}


class TicketRandomTool:
    def __init__(self, red_max_no, blue_max_no, red_times, blue_times):
        self.red_max_no = red_max_no
        self.blue_max_no = blue_max_no
        self.red_times = red_times
        self.blue_times = blue_times

        self.red_balls = [i for i in range(1, self.red_max_no + 1)]
        self.blue_balls = [i for i in range(1, self.blue_max_no + 1)]

        # log(len(red_balls))

    def print_ticket(self):
        red_balls_copy = copy.copy(self.red_balls)
        blue_balls_copy = copy.copy(self.blue_balls)
        ticket = {}
        red_ball = []
        blue_ball = []
        for i in range(self.red_times):
            index = random.randint(0, len(red_balls_copy) - 1)
            rb = red_balls_copy.pop(index)
            red_ball.append(rb)

        for i in range(self.blue_times):
            index = random.randint(0, len(blue_balls_copy) - 1)
            bb = blue_balls_copy.pop(index)
            blue_ball.append(bb)

        red_ball.sort()
        blue_ball.sort()

        ticket['red_ball'] = red_ball
        ticket['blue_ball'] = blue_ball
        log(ticket)

    def print_tickets(self, times):
        ticket_list = []
        for time in range(times):
            red_balls_copy = copy.copy(self.red_balls)
            blue_balls_copy = copy.copy(self.blue_balls)
            ticket = {}
            red_ball = []
            blue_ball = []
            for i in range(self.red_times):
                index = random.randint(0, len(red_balls_copy) - 1)
                rb = red_balls_copy.pop(index)
                red_ball.append(rb)

            for i in range(self.blue_times):
                index = random.randint(0, len(blue_balls_copy) - 1)
                bb = blue_balls_copy.pop(index)
                blue_ball.append(bb)

            red_ball.sort()
            blue_ball.sort()

            ticket['red_ball'] = red_ball
            ticket['blue_ball'] = blue_ball

            red_zone = ' '.join(map(str, red_ball))
            blue_zone = ' '.join(map(str, blue_ball))
            log(red_zone + ' | ' + blue_zone)

            ticket_list.append(ticket)


d = TicketRandomTool(red_max_no=lotto['red_max_no'],
                     blue_max_no=lotto['blue_max_no'],
                     red_times=lotto['red_times'],
                     blue_times=lotto['blue_times'])
d.print_tickets(5)
