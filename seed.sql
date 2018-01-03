USE `mydb`;

DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `customer_no` int(20) NOT NULL,
  `risk` int(20) NOT NULL,
  `limit` int(20) NOT NULL,
  `date` int(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin5;

INSERT INTO `customers` (`id`, `customer_no`, `risk`, `limit`, `date`) VALUES
  (1, '4001', 10, 5, 201701),
  (2, '4002', 7, 9, 201701),
  (3, '4001', 8, 6, 201702),
  (4, '4002', 7, 9, 201702);
