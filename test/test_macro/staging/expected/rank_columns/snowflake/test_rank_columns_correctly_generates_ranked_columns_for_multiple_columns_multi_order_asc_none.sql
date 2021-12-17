RANK() OVER (PARTITION BY "CUSTOMER_ID" ORDER BY "BOOKING_DATE" ASC, "ORDER_DATE") AS "DBTVAULT_RANK",
RANK() OVER (PARTITION BY "TRANSACTION_ID" ORDER BY "TRANSACTION_DATE" DESC) AS "SAT_RANK"