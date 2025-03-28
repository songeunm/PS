WITH rented AS (
    SELECT DISTINCT car_id
    FROM car_rental_company_rental_history
    WHERE start_date <= "2022-11-30" AND end_date >= "2022-11-01"
)

SELECT car_id, c.car_type, round(daily_fee*30*(100-discount_rate)/100) fee
FROM car_rental_company_car c
LEFT JOIN car_rental_company_discount_plan d
ON c.car_type = d.car_type
AND c.car_type in ("세단", "SUV")
AND d.duration_type = "30일 이상"
WHERE car_id NOT IN (SELECT * FROM rented)
    AND daily_fee*30*(100-discount_rate)/100 BETWEEN 500000 AND 2000000-1
ORDER BY 3 DESC, 2 ASC, 1 DESC;