CREATE TABLE `tInstaFollow` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `insta_id` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `follow_id` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `accepted` tinyint(4) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `tInstaUsers_UN` (`insta_id`, `follow_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;
