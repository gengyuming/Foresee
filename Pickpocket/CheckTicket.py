
class CheckTicket:
    def __init__(self, win_ticket):
        self.pro_zone_times = 5
        self.post_zone_times = 2

        self.win_pro_zone = []
        self.win_post_zone = []

        self.win_ticket = win_ticket.split(' ')

    def check(self, tickets):
        self.win_pro_zone = self.win_ticket[:self.pro_zone_times]
        self.win_post_zone = self.win_ticket[-self.post_zone_times:]
        for ticket in tickets:
            ticket = ticket.split(' ')
            print(self.win_ticket)
            print(ticket)
            ticket_pro_zone = ticket[:self.pro_zone_times]
            ticket_post_zone = ticket[-self.post_zone_times:]
            win_pro_zone_no = self.check_pro_zone_no(ticket_pro_zone)
            win_post_zone_no = self.check_post_zone_no(ticket_post_zone)
            bonus = self.match_rules(win_pro_zone_no, win_post_zone_no)
            print(bonus)

    def check_pro_zone_no(self, ticket_pro_zone):
        win_pro_zone_no = 0
        for ball in ticket_pro_zone:
            if ball in self.win_pro_zone:
                win_pro_zone_no += 1

        return win_pro_zone_no

    def check_post_zone_no(self, ticket_post_zone):
        win_post_zone_no = 0
        for ball in ticket_post_zone:
            if ball in self.win_post_zone:
                win_post_zone_no += 1

        return win_post_zone_no

    def match_rules(self, win_pro_zone_no, win_post_zone_no):
        pass


class CheckLottoTicket(CheckTicket):
    def __init__(self, win_ticket):
        super().__init__(win_ticket)

        self.red_times = 5
        self.blue_times = 2
        self.check_tickets = []

    def match_rules(self, win_pro_zone_no, win_post_zone_no):
        bonus = {
            '一等奖': '浮动',
            '二等奖': '浮动',
            '三等奖': '10000',
            '四等奖': '3000',
            '五等奖': '300',
            '六等奖': '200',
            '七等奖': '100',
            '八等奖': '15',
            '九等奖': '5',
            '未中奖': '0'
        }
        red_difference = self.red_times - win_pro_zone_no
        blue_difference = self.blue_times - win_post_zone_no

        # 红5蓝2
        if red_difference == 0 and blue_difference == 0:
            level = '一等奖'

        # 红5蓝1
        elif red_difference == 0 and blue_difference == 1:
            level = '二等奖'

        # 红5蓝0
        elif red_difference == 0 and blue_difference == 2:
            level = '三等奖'

        # 红4蓝2
        elif red_difference == 1 and blue_difference == 0:
            level = '四等奖'

        # 红4蓝1
        elif red_difference == 1 and blue_difference == 1:
            level = '五等奖'

        # 红3蓝2
        elif red_difference == 2 and blue_difference == 0:
            level = '六等奖'

        # 红4蓝0
        elif red_difference == 1 and blue_difference == 2:
            level = '七等奖'

        # 红3蓝1 or 红2蓝2
        elif (red_difference == 2 and blue_difference == 1) or (red_difference == 3 and blue_difference == 0):
            level = '八等奖'

        # 红3蓝0 or 红1蓝2 or 红2蓝1 or 红0蓝2
        elif (red_difference == 2 and blue_difference == 2)\
                or (red_difference == 4 and blue_difference == 0)\
                or (red_difference == 3 and blue_difference == 1)\
                or (red_difference == 5 and blue_difference == 0):
            level = '九等奖'

        else:
            level = '未中奖'

        return level, bonus[level]


class CheckDoubleColorTicket(CheckTicket):
    def __init__(self, win_ticket):
        super().__init__(win_ticket)

        self.red_times = 6
        self.blue_times = 1
        self.check_tickets = []

    def match_rules(self, win_pro_zone_no, win_post_zone_no):
        bonus = {
            '一等奖': '浮动',
            '二等奖': '浮动',
            '三等奖': '3000',
            '四等奖': '200',
            '五等奖': '10',
            '六等奖': '5',
            '未中奖': '0'
        }
        red_difference = self.red_times - win_pro_zone_no
        blue_difference = self.blue_times - win_post_zone_no

        # 红6蓝1
        if red_difference == 0 and blue_difference == 0:
            level = '一等奖'

        # 红6蓝0
        elif red_difference == 0 and blue_difference == 1:
            level = '二等奖'

        # 红5蓝1
        elif red_difference == 1 and blue_difference == 0:
            level = '三等奖'

        # 红5蓝0 or 红4蓝1
        elif (red_difference == 1 and blue_difference == 1)\
                or (red_difference == 2 and blue_difference == 0):
            level = '四等奖'

        # 红4蓝0 or 红3蓝1
        elif (red_difference == 2 and blue_difference == 1)\
                or (red_difference == 3 and blue_difference == 0):
            level = '五等奖'

        # 红2蓝1 or 红1蓝1 or 红0蓝1
        elif (red_difference == 4 and blue_difference == 0)\
                or (red_difference == 5 and blue_difference == 0)\
                or (red_difference == 6 and blue_difference == 0):
            level = '六等奖'

        else:
            level = '未中奖'

        return level, bonus[level]


if __name__ == '__main__':
    win_ticket = '10 29 28 11 03 09 13'
    check_tickets = [
        '02 06 07 10 19 26 06',
        '04 08 09 10 32 33 07',
        '02 03 06 18 19 22 15',
        '16 19 21 27 29 33 04',
        '05 09 21 25 28 32 07'
    ]
    # lotto_check = CheckLottoTicket(win_ticket)
    # lotto_check.check(check_tickets)

    double_color_check = CheckDoubleColorTicket(win_ticket)
    double_color_check.check(check_tickets)
