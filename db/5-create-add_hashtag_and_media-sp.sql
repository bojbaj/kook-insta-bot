DROP PROCEDURE IF EXISTS spAddHashtag;

DELIMITER $$
CREATE PROCEDURE spAddHashtag(
 IN Hashtag VARCHAR(100),
 OUT HashtagID INT
 )
BEGIN
-- 	INSERT HASHTAG if is not exists
	SET @HashtagID := (SELECT id FROM tInstaHashtag t WHERE t.hashtag = Hashtag);	
	IF (@HashtagID IS NULL) THEN
	BEGIN
 		INSERT INTO tInstaHashtag(`hashtag`) VALUES(Hashtag);
 		SET @HashtagID := LAST_INSERT_ID();
	END;
	END IF;

	SET HashtagID:= @HashtagID;	
END;
$$
DELIMITER ;


DROP PROCEDURE IF EXISTS spAddMediaByHashtag;

DELIMITER $$
CREATE PROCEDURE spAddMediaByHashtag(
 IN HashtagID INT, 
 IN MediaID VARCHAR(19),
 IN MediaCode VARCHAR(11), 
 IN OwnerID VARCHAR(10),
 IN TakenAt INT,
 IN IsVideo TINYINT
 )
BEGIN	

	-- 	INSERT MEDIA related to this hashtag
	IF NOT EXISTS(SELECT * FROM tInstaMedia t WHERE t.media_id = MediaID) THEN
	BEGIN
		INSERT IGNORE INTO tInstaMedia(media_id, shortcode,tInstaHashtag_id,insta_id,taken_at_timestamp,is_video)
		VALUES(MediaID,MediaCode,HashtagID,OwnerID,TakenAt,IsVideo);		
	END;
	END IF;
END;
$$
DELIMITER ;