367/ suna88
352/naga28121998


WF -  P1. Top-N / Highest, P2. 3MA/Rolling, P3. Avg-vs-group/Running /Cummulative, P4. Previous , compare with last, P5. %rank, P6. First , earliest,      P7.Accumulate / Compare P8.  Nth,   
P6. P7. Max/Min by group, P8. Not-in, P10. Correlated, P11. 2nd lowest / highest, P13. Most-recent
P14.  Count-filter, Having-avg, P.17 Group-distinct-rank
P18. Multi-table, P19. Self-join, P.21 Anti-join(LEFT IS NULL), P23. Level-hierarchy
P24. Aggregate / Group-by-date, P.26 Conditional-case, P27. Span(TIMESTAMPDIFF), P28. Transform(STR_TO_DATE)
P29.  view, P30. CTE-then-rank.  
P31. Cast-money, P32. Split-name, P33. NULL-avoid, P34. LIKE-filter  P.35 Ratio-of-avgs, Aggregate-percentage, Percent-rank-filter
 P.38  Union (stack two result sets)
   
P6. SELECT * FROM table_name WHERE col = (SELECT MAX(col) FROM table_name); - -- Global max: -- Max per group (correlated): - 'country with highest X', 'cheapest house in each location', 'max price record'
P7. SELECT * FROM table_name t1 WHERE col = (SELECT MIN(col) FROM table_name t2 WHERE t2.group_col = t1.group_col); - Correlated subquery runs once per outer row. Use for 'cheapest in each location', 'highest per dept'.
P8. -- NOT IN: SELECT * FROM customers WHERE customerNumber NOT IN ( SELECT DISTINCT customerNumber FROM orders); -- 'customers who have NOT ordered', 'circuits with no races', 'inactive clients', 'movies without rating'
P9. SELECT c.* FROM customers c LEFT JOIN orders o ON c.customerNumber = o.customerNumber WHERE o.orderNumber IS NULL; - 
P10. SELECT first_name, last_name, salary FROM employees e WHERE salary > ( SELECT AVG(salary) FROM employees WHERE department_id = e.department_id  -- e. binds to outer row ); - The inner query references the outer query's row (e.department_id). Runs once per outer row.  -- 'employees earning above avg of their own dept', 'Paris office using correlated subquery'
P11. -- Second lowest: WHERE col = ( SELECT MIN(col) FROM table_name WHERE col > (SELECT MIN(col) FROM table_name) ); --  'second lowest budget department', '2nd highest salary'
P12. -- 2nd highest salary: SELECT MIN(salary) FROM (SELECT salary FROM employees ORDER BY salary DESC LIMIT 2) t;
P13. SELECT Country_name, Perceptions_of_corruption FROM world_happiness_report WHERE year = (SELECT MAX(year) FROM world_happiness_report) ORDER BY Perceptions_of_corruption ASC LIMIT 1; 'most recent year available', 'latest year in the data' -- Always use (SELECT MAX(year) FROM ...) 
P14. SELECT department, COUNT(*) AS emp_count FROM employees GROUP BY department HAVING COUNT(*) > 2;  -- 'depts with more than 2 employees', 'customers with same first name', 'locations with > 5 houses'
P15. SELECT name FROM departments WHERE code IN ( SELECT department FROM employees GROUP BY department HAVING COUNT(*) > 2); --  Never use aggregate in WHERE
P16. SELECT location, ROUND(AVG(price),2) AS avg_price FROM bangalore_houses GROUP BY location HAVING AVG(price) > 100 ORDER BY avg_price DESC; -- 'locations where avg price > 100', 'depts with avg salary > X', 'catalogue items with avg price > 1000' -- HAVING can use any aggregate: AVG, SUM, MAX. Remember: no alias in HAVING — repeat the expression or use the column.
P17. SELECT customerid, COUNT(DISTINCT albumid) AS unique_albums, DENSE_RANK() OVER ( ORDER BY COUNT(DISTINCT albumid) DESC ) AS album_rank FROM invoice JOIN invoiceline USING(invoiceid) JOIN track USING(trackid) GROUP BY customerid ORDER BY album_rank;  -- COUNT DISTINCT inside GROUP BY + DENSE_RANK() in the SELECT. The window function operates on the already-grouped result. --  'rank customers by unique albums purchased', 'rank by number of distinct items'
P18. SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS total_value FROM customers c JOIN orders o        ON c.customerNumber  = o.customerNumber JOIN orderdetails od ON o.orderNumber     = od.orderNumber JOIN products p      ON od.productCode    = p.productCode JOIN productlines pl ON p.productLine     = pl.productLine WHERE c.country = 'USA' AND pl.productLine = 'Classic Cars' GROUP BY c.customerNumber, c.customerName ORDER BY total_value DESC; -- Joins in the direction data flows: customer → orders → details → product → category. Always alias tables. Add WHERE after all JOINs.-- 'total value of USA Classic Cars orders', 'customer film rental report'



P19. SELECT DISTINCT a.Country_name FROM world_happiness_report a JOIN world_happiness_report b ON a.Country_name = b.Country_name WHERE a.year = 2019 AND a.Freedom_to_make_life_choices > 0.8 AND b.year = 2020 AND  b.Freedom_to_make_life_choices > 0.8;  --  'countries where X > 0.8 in BOTH 2019 AND 2020', 'customers with same first name' -- The self-join approach (alias a, b) is cleaner for two-year conditions. The HAVING approach works for duplicate-value detection. -- Two-year condition (same table joined to itself): 
SELECT region_id
FROM region_yearly_stats
WHERE year IN (2023,2024)
AND growth_rate > 5
GROUP BY region_id
HAVING COUNT(DISTINCT year) = 2;

SELECT r2023.region_id
FROM region_yearly_stats r2023
JOIN region_yearly_stats r2024
ON r2023.region_id = r2024.region_id
WHERE r2023.year = 2023
AND r2024.year = 2024
AND r2023.growth_rate > 5
AND r2024.growth_rate > 5;

P20. SELECT c1.customerid, c1.firstname FROM customer c1 WHERE c1.firstname IN ( SELECT firstname FROM customer GROUP BY firstname HAVING COUNT(*) > 1); -- -- Same first name:
P21. SELECT c.circuitId, c.name FROM circuits c LEFT JOIN races r ON c.circuitId = r.circuitId WHERE r.raceId IS NULL;  -- NULL means no matching row = no race. -- 'circuits where no races held', 'films never rented' -- LEFT JOIN keeps all left-table rows. WHERE right_table.id IS NULL filters to only rows with no match. This is the anti-join pattern.

P22. -- 3-level catalogue (child → parent → grandparent): SELECT c1.Catalogue_Entry_Description AS Prod_Desc, c2.Catalogue_Entry_Description AS Sub_Prod_Desc, c3.Catalogue_Entry_Description AS Main_Prod_Desc FROM catalogue c1 JOIN catalogue c2 ON c1.Parent_Catalogue_Entry_id = c2.Catalogue_Entry_id JOIN catalogue c3 ON c2.Parent_Catalogue_Entry_id = c3.Catalogue_Entry_id;  -- Each self-join adds one level. LEFT JOIN for manager so employees without a manager (CEO) still appear. --  'item + parent + grandparent description', 'reporting manager'
P.23 -- Manager lookup (employee → manager): SELECT e.Employee_name, m.Employee_name AS Manager_Name FROM resources e LEFT JOIN resources m ON e.Manager_id = m.Employee_id;
P24. -- Group by year: SELECT YEAR(Order_Date) AS yr, SUM(Sales) FROM orders WHERE YEAR(Order_Date) = 2020 GROUP BY YEAR(Order_Date); -- DATE_FORMAT('%Y-%m') groups by month. DATE_FORMAT('%Y-%m-01') gives a proper date for sorting. YEAR() alone groups by year only.
P25. -- Group by year-month: SELECT DATE_FORMAT(Date,'%Y-%m') AS month, MAX(Temp9am) FROM australiaweather GROUP BY DATE_FORMAT(Date,'%Y-%m') ORDER BY month; -- Trigger words: 'monthly sessions', 'total sales in 2020', 'max temp per month', 'profitable months'

P26. SELECT ROUND(AVG(CASE WHEN DATE_FORMAT(Date,'%Y-%m') = '2008-01' THEN Rainfall END), 2) AS avg_jan, ROUND(AVG(CASE WHEN DATE_FORMAT(Date,'%Y-%m') = '2008-07' THEN Rainfall END), 2) AS avg_jul FROM australiaweather; --  CASE WHEN inside AVG/SUM — a pivot pattern. Each CASE becomes a separate column. Works for any pivot (months, sources, devices). -- 'compare Jan 2008 vs Jul 2008 rainfall', 'compare two months in one row'

P27. SELECT first_name, last_name, hire_date, TIMESTAMPDIFF(YEAR, hire_date, CURDATE()) AS tenure_years FROM employees ORDER BY tenure_years DESC LIMIT 3; -- TIMESTAMPDIFF(YEAR, start, end) gives integer years. Use CURDATE() for 'up to today'. DATEDIFF() gives difference in days. --  'tenure in years', 'longest serving employee', 'years since hire date'

P28. SELECT mp.name, ABS(DATEDIFF( STR_TO_DATE(mp.tenure_start, '%Y-%d-%m'), STR_TO_DATE(mla.tenure_start, '%Y-%d-%m') )) AS gap_days FROM mp JOIN mla ON mp.name = mla.name ORDER BY gap_days DESC LIMIT 1; -- STR_TO_DATE(string, format) converts any string to a proper DATE. Wrap in ABS() to always get a positive gap regardless of order. -- 'dates stored as YYYY-DD-MM', 'date format not standard'

P29. Trigger : Trigger words:
-- Step 1: Create the view: CREATE OR REPLACE VIEW view_name AS SELECT col1, col2, aggregate_col FROM table1 JOIN table2 ON ... GROUP BY col1, col2; --  'create a virtual table', 'create a view called X', 'using the view fetch...'

CREATE VIEW customer_order_value AS
SELECT
c.customer_id,
c.customer_name,
SUM(oi.quantity * oi.unit_price) AS total_order_value
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY
c.customer_id,
c.customer_name;


-- (b) Query the view to show customers whose total order value exceeds 3000,
-- highest first

SELECT
customer_id,
customer_name,
total_order_value
FROM customer_order_value
WHERE total_order_value > 3000
ORDER BY total_order_value DESC;

-- Step 2 : Use a select statement to check if the view works.
-- Step 2: Query the view (can add WHERE, ORDER BY, window functions): SELECT * FROM view_name WHERE condition ORDER BY col;


P30. WITH customer_totals AS ( SELECT customerNumber, customerName, SUM(amount) AS total_payments FROM customers JOIN payments USING(customerNumber) GROUP BY customerNumber, customerName ) SELECT *, DENSE_RANK() OVER (ORDER BY total_payments DESC) AS payment_rank FROM customer_totals ORDER BY payment_rank LIMIT 5;  --  'use CTE and window function', 'top 5 customers total payments using CTE'. -- CTE (WITH clause) names an intermediate result. Then use DENSE_RANK in the main SELECT. Can chain multiple CTEs: WITH a AS (...), b AS (...) SELECT...




P31. -- Convert '$1234.56' to DECIMAL for arithmetic: AVG(CAST(REPLACE(Average_Covered_Charges, '$', '') AS DECIMAL(15,2))) -- 'Average_Covered_Charges stored as $12345.67', money column stored as text -- REPLACE removes the $ character. CAST converts the resulting string to DECIMAL. Wrap both in AVG/SUM for aggregation.
-- Full example — insurance coverage ratio: SELECT Provider_Id, AVG(CAST(REPLACE(Average_Covered_Charges,'$','') AS DECIMAL(15,2))) / (AVG(CAST(REPLACE(Average_Total_Payments,'$','') AS DECIMAL(15,2))) + AVG(CAST(REPLACE(Average_Medicare_Payments,'$','') AS DECIMAL(15,2)))) AS ratio FROM inpatient1 GROUP BY Provider_Id;

P32. 
SELECT Customer_Name, SUBSTRING_INDEX(Customer_Name, ' ', 1) AS first_name, SUBSTRING(Customer_Name, LOCATE(' ', Customer_Name) + 1) AS last_name FROM orders; -- SUBSTRING_INDEX(str, delim, 1) takes everything before the first space. LOCATE finds the position of the space. SUBSTRING takes from position+1 to end. --  'extract first name and last name from full name', 'split on space'



P33.
ROUND(SUM(CASE WHEN source='bsearch' THEN 1 ELSE 0 END) /. -- 'bsearch as % of gsearch', 'ratio that could be 0 in denominator'
NULLIF(SUM(CASE WHEN source='gsearch' THEN 1 ELSE 0 END), 0), 4) AS b_pct_of_g. --  -- NULLIF(expr, 0) returns NULL if expr = 0, avoiding division-by-zero. Any arithmetic on NULL returns NULL, which is safe.

P34. 

 Always LOWER() before LIKE to avoid case issues. DATE_FORMAT('%D %M %Y') gives '1st January 1999' format.
-- Filter by starting letter: WHERE LOWER(g.name) LIKE 's%'
-- Full name display: CONCAT(first_name, ' ', last_name) AS full_name
-- Date formatted string: CONCAT(first_name, ' Joined on ', DATE_FORMAT(hire_date,'%D %M %Y'))





35. SELECT Provider_Id, Provider_Name, ROUND( AVG(CAST(REPLACE(col_a,'$','') AS DECIMAL(15,2))) / (AVG(CAST(REPLACE(col_b,'$','') AS DECIMAL(15,2))) + AVG(CAST(REPLACE(col_c,'$','') AS DECIMAL(15,2)))), 6 ) AS ratio FROM inpatient1 GROUP BY Provider_Id, Provider_Name ORDER BY ratio DESC;  --  'insurance coverage ratio', 'ratio of averages'. --  Ratio = numerator / denominator. When columns are money strings, wrap each in CAST(REPLACE(...,'$','') AS DECIMAL). The whole expression goes inside ROUND(..., decimals).



P36. SELECT COUNT(DISTINCT s.session_id)   AS Sessions, COUNT(DISTINCT o.order_id)     AS Orders, ROUND(COUNT(DISTINCT o.order_id) / COUNT(DISTINCT s.session_id) * 100, 4) AS Conversion FROM sessions_website s LEFT JOIN orders o ON s.session_id = o.session_id WHERE s.source_UTM = 'gsearch' AND s.campaign_UTM = 'nonbrand' AND s.visited_at <= '2020-08-24'; -- 'conversion rate from sessions to orders', 'CVR = unique orders / unique sessions' -- LEFT JOIN so sessions with no orders still count in the denominator. COUNT DISTINCT prevents double-counting. Multiply by 100 for percentage.



 


P37. SELECT DATE_FORMAT(visited_at,'%Y-%m-01') AS month, SUM(CASE WHEN source='gsearch' AND device='desktop' THEN 1 ELSE 0 END) AS g_dtop, SUM(CASE WHEN source='bsearch' AND device='desktop' THEN 1 ELSE 0 END) AS b_dtop, ROUND( SUM(CASE WHEN source='bsearch' AND device='desktop' THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN source='gsearch' AND device='desktop' THEN 1 ELSE 0 END), 0), 4) AS b_pct_of_g_dtop FROM sessions_website WHERE campaign_UTM = 'nonbrand' GROUP BY DATE_FORMAT(visited_at,'%Y-%m-01') ORDER BY month; -- SUM(CASE WHEN condition THEN 1 ELSE 0 END) counts rows matching a condition. Divide one count by another for a ratio. NULLIF protects the denominator. --  'gsearch vs bsearch sessions by device per month', 'compare two groups in one row'



P38. -- Stack two result sets (removes duplicates): SELECT name AS label FROM reviewer UNION SELECT title FROM movie ORDER BY label;
-- Keep duplicates with UNION ALL: SELECT employee_id, first_name, salary, department_id FROM employees WHERE department_id = 60 UNION SELECT employee_id, first_name, salary, department_id FROM employees WHERE department_id = 90 ORDER BY salary; --  'reviewers and movies in a single list', 'employees from dept 60 AND dept 90' -- UNION removes duplicates. UNION ALL keeps all rows (faster). Both SELECTs must have the same number of columns. ORDER BY goes at the very end, once.



ALTER TABLE australiaweather ADD COLUMN Pressure9pm INT NOT NULL DEFAULT 1001; -- --  'add a new column with default value', 'add Pressure9pm INT NOT NULL DEFAULT 1001'
-- Verify: DESCRIBE australiaweather;


Trigger : Trigger words: 'create table with check constraints', 'course_duration <= 21', 'title IN (list)'
CHECK() can be: comparison (<=, >=), IN list, or BETWEEN. Goes after the column type. Can also be table-level: CONSTRAINT chk_name CHECK (expr).



CREATE TABLE Course ( Course_ID  INT PRIMARY KEY, Course_Name       VARCHAR(100), course_duration   INT CHECK (course_duration <= 21), course_title      VARCHAR(20) CHECK (course_title IN ('Python','SQL','STATS')), course_start_date DATE );
Trigger : Trigger words: 'undo accidental update', 'transaction control', 'SET autocommit'
Key Note: 💡 Sequence: SET autocommit=0 → SAVEPOINT name → (changes) → ROLLBACK TO SAVEPOINT name → COMMIT. ROLLBACK alone undoes everything since last COMMIT.

SET autocommit = 0;         -- disable auto-commit SELECT * FROM clients;      -- see original data
SAVEPOINT a;                -- bookmark this state
UPDATE clients              -- accidental change SET client_Country = 'India';
SELECT * FROM clients;      -- verify the change
ROLLBACK TO SAVEPOINT a;    -- undo back to bookmark
SELECT * FROM clients;      -- verify restored
COMMIT;                     -- finalise (no-op here, restoring)

CTE 

WITH customer_payments AS (
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(p.amount_paid) AS total_paid
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN payments p
        ON o.order_id = p.order_id
    GROUP BY
        c.customer_id,
        c.customer_name
)
SELECT
    customer_id,
    customer_name,
    total_paid,
    RANK() OVER (ORDER BY total_paid DESC) AS payment_rank
FROM customer_payments
ORDER BY total_paid DESC
LIMIT 5;


CTE Universal Template:

WITH cte_name AS (
    SELECT
        column1,
        column2,
        aggregate_column
    FROM table_name
    WHERE condition
    GROUP BY column1, column2
)
SELECT *
FROM cte_name
WHERE condition
ORDER BY column1;


Check Constraint:

CREATE TABLE table_name (
    id_column INT PRIMARY KEY,
    column1 datatype CHECK (condition),
    column2 datatype CHECK (column2 IN ('value1','value2','value3')),
    column3 datatype CHECK (column3 BETWEEN min_value AND max_value)
);

CHECK (salary > 0)
CHECK (age >= 18)
CHECK (course_duration <= 21)
CHECK (status IN ('Active','Inactive'))
CHECK (marks BETWEEN 0 AND 100)


TCL. Steps 

SET autocommit = 0;  / makes manual

SAVEPOINT before_data_change;

INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
OR
UPDATE table_name SET column_name = new_value WHERE condition;
OR
DELETE FROM table_name WHERE condition;

SELECT * FROM table_name;

ROLLBACK TO SAVEPOINT before_data_change;    / changes are lost or accidental changes are dropped

SELECT * FROM table_name;

COMMIT;


VIEW or Virtual table:

CREATE VIEW view_name AS
SELECT
    t1.column1,
    t1.column2,
    t2.column3,
    AGG_FUNCTION(t1.column4) AS metric
FROM table1 t1
JOIN table2 t2
    ON t1.common_key = t2.common_key
WHERE condition
GROUP BY
    t1.column1,
    t1.column2,
    t2.column3
HAVING AGG_FUNCTION(t1.column4) > value;

SELECT *
FROM view_name
WHERE condition
ORDER BY column_name;
