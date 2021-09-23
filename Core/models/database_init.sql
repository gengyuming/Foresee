CREATE DATABASE IF NOT EXISTS foresee DEFAULT CHARACTER  SET utf8mb4 DEFAULT COLLATE utf8mb4_0900_ai_ci;

CREATE TABLE `ticket_history` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `draw_number` varchar(255) DEFAULT NULL COMMENT '期号',
  `draw_sort_result` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '' COMMENT '出奖号码（排列）',
  `draw_source_result` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '出奖号码（原始）',
  `draw_time` date DEFAULT NULL COMMENT '出奖日期',
  `ticket_type` int DEFAULT NULL COMMENT '1: 大乐透, 2: 双色球',
  PRIMARY KEY (`id`),
  UNIQUE KEY `draw_number` (`draw_number`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
