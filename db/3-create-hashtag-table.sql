CREATE TABLE `tInstaHashtag` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `hashtag` varchar(100) COLLATE utf8_persian_ci NOT NULL,  
  PRIMARY KEY (`Id`),
  UNIQUE KEY `tInstaHashtag_UN` (`hashtag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;
