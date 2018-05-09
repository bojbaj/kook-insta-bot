CREATE TABLE `tInstaUsers` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `csrf` varchar(32) COLLATE utf8_persian_ci NOT NULL,
  `insta_id` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `active` tinyint(4) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `tInstaUsers_UN` (`insta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;
