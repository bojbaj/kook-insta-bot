CREATE TABLE `tInstaTarget` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `insta_id` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `target_hashtags` varchar(500) COLLATE utf8_persian_ci NOT NULL,  
  `ignore_hashtags` varchar(500) COLLATE utf8_persian_ci NOT NULL,  
  `target_accounts` varchar(500) COLLATE utf8_persian_ci NOT NULL,
  `ignore_accounts` varchar(500) COLLATE utf8_persian_ci NOT NULL,  
  PRIMARY KEY (`Id`),
  UNIQUE KEY `tInstaUsers_UN` (`insta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;
