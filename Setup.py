from Pickpocket.TicketHistoryData import LottoHistory


lotto_history = LottoHistory()

# 下载API数据到DB
lotto_history.add_api_lotto_history_db_data()
# lotto_history.update_db_source_result()

# 更新DB source result
lotto_history.add_db_source_result()


# lotto_history.get_img_source_result(19079)
