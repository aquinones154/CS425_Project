CREATE FUNCTION funct(param)
  RETURNS INTEGER
  BEGIN
    DECLARE name
  END

  -- Check if stadium capacity is positive value
CREATE TRIGGER before_insert_stadium_capacity BEFORE INSERT ON Stadium
FOR EACH ROW
BEGIN
  IF NEW.Capacity < 0 THEN
    SET NEW.amount = 0;
  END IF;
END;

