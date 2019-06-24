MERGE INTO DV_PROTOTYPE_DB.TEST_VLT.HUB_CUSTOMER AS hub
USING (
SELECT DISTINCT a.CUSTOMER_PK, a.CUSTOMERKEY, a.LOADDATE, a.SOURCE 
FROM DV_PROTOTYPE_DB.TEST_STG.STG_CUSTOMER AS a ORDER BY a.LOADDATE) AS stg
ON hub.CUSTOMER_PK=stg.CUSTOMER_PK
WHEN NOT MATCHED THEN INSERT (hub.CUSTOMER_PK, hub.CUSTOMERKEY, hub.LOADDATE, hub.SOURCE) 
VALUES (stg.CUSTOMER_PK, stg.CUSTOMERKEY, stg.LOADDATE, stg.SOURCE)