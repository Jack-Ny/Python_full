SELECT COUNT(*) FROM actors;
INSERT INTO actors (first_name) VALUES ('Kurokos');
-- -> ERROR:  null value in column "last_name" of relation "actors" violates not-null constraint