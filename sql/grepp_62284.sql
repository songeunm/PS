/*
우유와 요거트가 담긴 장바구니
Summer/Winter Coding(2019)
GROUP BY, JOIN
*/

-- 방법 1 (오답)
SELECT CART_ID
FROM (
SELECT DISTINCT NAME, CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt')
GROUP BY CART_ID
HAVING COUNT(CART_ID) >= 2
) as T1
ORDER BY CART_ID;

-- 방법 1 (정답)
SELECT CART_ID
from (
SELECT DISTINCT NAME, CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt')
) as T1
GROUP BY CART_ID
HAVING COUNT(CART_ID) >= 2
ORDER BY 1;

-- 방법 2 (정답)
SELECT CART_ID
FROM
    (SELECT DISTINCT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = 'Milk') T1
JOIN
    (SELECT DISTINCT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = 'Yogurt') T2
USING (CART_ID)
ORDER BY 1;
