-- view checking sql

CREATE VIEW need_meeting
  AS
  SELECT name
  FROM students
  WHERE (score < 80) AND ((last_meeting IS NULL) OR (MONTH(NOW()) - MONTH(last_meeting) > 1));
