CREATE DATABASE IF NOT EXISTS foresee DEFAULT CHARACTER  SET utf8mb4 DEFAULT COLLATE utf8mb4_0900_ai_ci;
USER foresee;

CREATE TABLE `ticket_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `draw_number` int DEFAULT NULL,
  `draw_result` varchar(255) DEFAULT '',
  `draw_time` datetime DEFAULT NULL,
  `ticket_type` int DEFAULT NULL COMMENT '1: 大乐透, 2: 双色球',
  PRIMARY KEY (`id`),
  UNIQUE KEY `draw_number` (`draw_number`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
