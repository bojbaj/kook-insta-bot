DROP PROCEDURE IF EXISTS spAddTargetByMedia;

DELIMITER $$
CREATE PROCEDURE spAddTargetByMedia(
 IN MediaID VARCHAR(19), 
 IN InstaID VARCHAR(10),
 IN isLiker TINYINT
 )
BEGIN	
	-- 	INSERT target user related to this media
	IF NOT EXISTS(SELECT * FROM tInstaTargetUser t WHERE t.tInstaMedia_media_id = MediaID AND t.insta_id = InstaID AND t.is_liker = isLiker) THEN
	BEGIN
		INSERT IGNORE INTO tInstaTargetUser(tInstaMedia_media_id,insta_id,is_liker)
		VALUES(MediaID,InstaID,isLiker);		
	END;
	END IF;
END;
$$
DELIMITER ;