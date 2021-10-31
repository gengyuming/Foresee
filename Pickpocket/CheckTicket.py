
class CheckTicket:
    def __init__(self, win_ticket):
        self.pro_zone_times = 6
        self.post_zone_times = 1

        self.win_pro_zone = []
        self.win_post_zone = []

        self.win_ticket = win_ticket.split(' ')

    def check(self, tickets):
        self.win_pro_zone = self.win_ticket[:self.pro_zone_times]
        self.win_post_zone = self.win_ticket[-self.post_zone_times:]

        total_bonus = []

        for ticket in tickets:
            ticket = ticket.split(' ')
            print(self.win_ticket)
            print(ticket)
            ticket_pro_zone = ticket[:self.pro_zone_times]
            ticket_post_zone = ticket[-self.post_zone_times:]
            win_pro_zone_no = self.check_pro_zone_no(ticket_pro_zone)
            win_post_zone_no = self.check_post_zone_no(ticket_post_zone)
            bonus = self.match_rules(win_pro_zone_no, win_post_zone_no)
            if bonus[1] != '0':
                total_bonus.append(bonus[1])

        print('共计中奖金额： ' + ', '.join(total_bonus))

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
        return '奖励等级', '金额'


class CheckLottoTicket(CheckTicket):
    def __init__(self, win_ticket):
        super().__init__(win_ticket)

        self.red_times = 5
        self.blue_times = 2
        self.check_tickets = []

    def match_rules(self, win_pro_zone_no, win_post_zone_no):
        print('前区正确个数： ' + str(win_pro_zone_no))
        print('后区正确个数： ' + str(win_post_zone_no))

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
        print('前区正确个数： ' + str(win_pro_zone_no))
        print('后区正确个数： ' + str(win_post_zone_no))

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

    lotto_win_ticket = '08 23 26 27 33 08 09'
    lottor_check_tickets = [
        '02 16 24 29 31 03 05',
        '12 16 23 30 35 03 10',
        '06 09 ',
        '04 08 11 20 29 33 13',
        '02 20 22 29 31 32 07'
    ]

    lotto_check = CheckLottoTicket(lotto_win_ticket)
    lotto_check.check(lottor_check_tickets)

    # double_color_win_ticket = '04 12 28 18 05 15 07'
    # double_color_check_tickets = [
    #     '06 09 10 14 15 27 11',
    #     '02 15 29 30 32 33 07',
    #     '15 19 21 23 25 27 05',
    #     '04 08 11 20 29 33 13',
    #     '02 20 22 29 31 32 07'
    # ]
    #
    # double_color_check = CheckDoubleColorTicket(double_color_win_ticket)
    # double_color_check.check(double_color_check_tickets)
