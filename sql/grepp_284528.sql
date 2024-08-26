"""
연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기
GROUP BY
"""

-- 사번(HR_EMPLOYEES.EMP_NO/HR_GRADE.EMP_NO)
-- 성명(HR_EMPLOYEES.EMP_NAME)
-- 평가등급(HR_GRADE.SCORE)
-- 성과금-> 연봉(HR_EMPLOYEES.SAL)*비율

SELECT EMP_NO, EMP_NAME, GRADE,
    CASE
        WHEN GRADE = 'S' THEN SAL*0.2
        WHEN GRADE = 'A' THEN SAL*0.15
        WHEN GRADE = 'B' THEN SAL*0.1
        ELSE SAL*0
    END AS BONUS
FROM (SELECT emp_no, CASE
            WHEN avg(score) >= 96 THEN "S"
            WHEN avg(score) >= 90 THEN "A"
            WHEN avg(score) >= 80 THEN "B"
            ELSE "C"
        END AS "GRADE"
    FROM hr_employees AS e LEFT JOIN hr_grade AS g
    USING (EMP_NO)
    GROUP BY 1) AS ADD_GRADE LEFT JOIN HR_EMPLOYEES
USING (EMP_NO)
ORDER BY 1
;