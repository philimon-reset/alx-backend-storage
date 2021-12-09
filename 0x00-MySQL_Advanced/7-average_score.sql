-- computes and store the average score for a student.

DELIMITER //
DELIMITER //
CREATE
  PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
  BEGIN
    DECLARE
      stud_avg FLOAT;
    SET stud_avg = (SELECT
                    AVG(score)
                    FROM corrections
                    WHERE corrections.user_id = user_id);
    UPDATE users
    SET average_score = stud_avg
    WHERE users.id = user_id;
  END //
DELIMITER ;