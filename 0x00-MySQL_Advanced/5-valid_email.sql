-- Create a trigger that resets the attribute valid_email only when the email has been changed.

CREATE TRIGGER chang AFTER UPDATE ON users
FOR EACH ROW UPDATE users SET valid_email = IF(NEW.email = OLD.email, 1, 0) WHERE NEW.id = id;
