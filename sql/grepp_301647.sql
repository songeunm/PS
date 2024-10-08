/*
부모의 형질을 모두 가지는 대장균 찾기
SELECT
*/

-- 비트마스킹
SELECT T1.ID, T1.GENOTYPE, T2.GENOTYPE PARENT_GENOTYPE
FROM ECOLI_DATA T1 LEFT JOIN ECOLI_DATA T2
ON T1.PARENT_ID = T2.ID
WHERE T1.PARENT_ID IS NOT NULL
AND (T1.GENOTYPE & T2.GENOTYPE = T2.GENOTYPE)
ORDER BY 1;