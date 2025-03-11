WITH front_skill AS (
    SELECT SUM(code) code
    FROM skillcodes
    WHERE category = "Front End"
), set_grade AS (
    SELECT *,
        CASE
            WHEN skill_code & (SELECT code FROM skillcodes WHERE name = "Python") = (SELECT code FROM skillcodes WHERE name = "Python")
            AND skill_code & (SELECT code FROM front_skill) > 0
            THEN "A"
            WHEN skill_code & (SELECT code FROM skillcodes WHERE name = "C#") = (SELECT code FROM skillcodes WHERE name = "C#")
            THEN "B"
            WHEN skill_code & (SELECT code FROM front_skill) > 0
            THEN "C"
            ELSE NULL
        END grade
    FROM developers
)

SELECT grade, id, email
FROM set_grade
WHERE grade IS NOT NULL
ORDER BY 1, 2;