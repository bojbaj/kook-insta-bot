CREATE TABLE `tInstaMedia` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `insta_id` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `media_id` varchar(19) COLLATE utf8_persian_ci NOT NULL,
  `shortcode` varchar(20) COLLATE utf8_persian_ci NOT NULL,
  `tInstaHashtag_id` int(11) NULL,
  `is_video` tinyint(4) NOT NULL,
  `taken_at_timestamp` INT NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `tInstaMedia_UN` (`media_id`),
  CONSTRAINT `tInstaMedia_tInstaHashtag_FK` FOREIGN KEY (`tInstaHashtag_id`) REFERENCES `tInstaHashtag` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;
