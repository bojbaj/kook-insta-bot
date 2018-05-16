CREATE TABLE `tInstaTargetUser` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `insta_id` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `tInstaMedia_media_id` varchar(19) COLLATE utf8_persian_ci NOT NULL,
  `is_liker` tinyint(4) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `tInstaTarget_UN` (`tInstaMedia_media_id`, `insta_id`, `is_liker`),
  CONSTRAINT `tInstaTarget_tInstaMedia_FK` FOREIGN KEY (`tInstaMedia_media_id`) REFERENCES `tInstaMedia` (`media_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;
