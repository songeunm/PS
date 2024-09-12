/*
언어별 개발자 분류하기
GROUP BY
*/

-- 방법 1
WITH FRONT AS (
    SELECT SUM(CODE) as CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
), PYTHON AS (
    SELECT CODE
    FROM SKILLCODES
    WHERE NAME = 'Python'
), CSHARP AS (
    SELECT CODE
    FROM SKILLCODES
    WHERE NAME = 'C#'
), GRADES AS (
    SELECT CASE
        WHEN SKILL_CODE & (SELECT CODE FROM FRONT) <> 0
             AND SKILL_CODE & (SELECT CODE FROM PYTHON) <> 0 THEN 'A'
        WHEN SKILL_CODE & (SELECT CODE FROM CSHARP) <> 0 THEN 'B'
        WHEN SKILL_CODE & (SELECT CODE FROM FRONT) <> 0 THEN 'C'
        ELSE NULL
        END as GRADE,
        ID, EMAIL
    FROM DEVELOPERS
)

SELECT *
FROM GRADES
WHERE GRADE IS NOT NULL
ORDER BY 1, 2;

-- 방법 2
WITH GRADES AS (
    SELECT CASE
        WHEN SKILL_CODE &   (SELECT SUM(CODE) as CODE
                            FROM SKILLCODES
                            WHERE CATEGORY = 'Front End') <> 0
             AND SKILL_CODE &   (SELECT CODE
                                FROM SKILLCODES
                                WHERE NAME = 'Python') <> 0 THEN 'A'
        WHEN SKILL_CODE &   (SELECT CODE
                            FROM SKILLCODES
                            WHERE NAME = 'C#') <> 0 THEN 'B'
        WHEN SKILL_CODE &   (SELECT SUM(CODE) as CODE
                            FROM SKILLCODES
                            WHERE CATEGORY = 'Front End') <> 0 THEN 'C'
        ELSE NULL
        END as GRADE,
        ID, EMAIL
    FROM DEVELOPERS
)

SELECT *
FROM GRADES
WHERE GRADE IS NOT NULL
ORDER BY 1, 2;