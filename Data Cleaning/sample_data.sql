use test;

CREATE TABLE my_table (
    id INT PRIMARY KEY,
    column1 INT NULL,
    column2 VARCHAR(50) NULL
);

INSERT INTO my_table (id, column1, column2) VALUES
(1, 5, 'Ravi'),
(2, 18, 'Anu'),
(3, NULL, 'Karthik'),
(4, 22, 'Meena'),
(5, 11, NULL),
(6, NULL, 'Suresh'),
(7, 9, 'Priya'),
(8, 35, 'Arun'),
(9, 14, NULL),
(10, 6, 'Divya'),
(11, 27, 'Manoj'),
(12, NULL, 'Nisha'),
(13, 19, 'Rahul'),
(14, 8, NULL),
(15, 40, 'Santosh');

