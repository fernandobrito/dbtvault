@fixture.set_workdir
Feature: Satellites Loaded in cycles using separate manual loads

  @fixture.satellite_cycle
  Scenario: [SAT-CYCLE] SATELLITE load over several cycles
    Given the RAW_STAGE stage is empty
    And the SATELLITE sat is empty

    # ================ DAY 1 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
      | 1002        | Beth          | 1995-08-07   | 2019-05-04     | 2019-05-04 | *      |
      | 1003        | Charley       | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
      | 1010        | Jenny         | 1991-03-21   | 2019-05-04     | 2019-05-04 | *      |
      | 1012        | Albert        | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 2 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1002        | Beah          | 1995-08-07   | 2019-05-05     | 2019-05-05 | *      |
      | 1003        | Chris         | 1990-02-03   | 2019-05-05     | 2019-05-05 | *      |
      | 1004        | David         | 1992-01-30   | 2019-05-05     | 2019-05-05 | *      |
      | 1010        | Jenny         | 1991-03-25   | 2019-05-05     | 2019-05-05 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 3 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1002        | Beth          | 1995-08-07   | 2019-05-06     | 2019-05-06 | *      |
      | 1003        | Claire        | 1990-02-03   | 2019-05-06     | 2019-05-06 | *      |
      | 1005        | Elwyn         | 2001-07-23   | 2019-05-06     | 2019-05-06 | *      |
      | 1006        | Freia         | 1960-01-01   | 2019-05-06     | 2019-05-06 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 4 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1002        | Beah          | 1995-08-07   | 2019-05-07     | 2019-05-07 | *      |
      | 1003        | Charley       | 1990-02-03   | 2019-05-07     | 2019-05-07 | *      |
      | 1007        | Geoff         | 1990-02-03   | 2019-05-07     | 2019-05-07 | *      |
      | 1010        | Jenny         | 1991-03-25   | 2019-05-07     | 2019-05-07 | *      |
      | 1011        | Karen         | 1978-06-16   | 2019-05-07     | 2019-05-07 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # =============== CHECKS ===================
    Then the SATELLITE table should contain expected data
      | CUSTOMER_PK | HASHDIFF                             | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | md5('1001') | md5('1990-02-03\|\|1001\|\|ALBERT')  | Albert        | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
      | md5('1002') | md5('1995-08-07\|\|1002\|\|BETH')    | Beth          | 1995-08-07   | 2019-05-04     | 2019-05-04 | *      |
      | md5('1002') | md5('1995-08-07\|\|1002\|\|BEAH')    | Beah          | 1995-08-07   | 2019-05-05     | 2019-05-05 | *      |
      | md5('1002') | md5('1995-08-07\|\|1002\|\|BETH')    | Beth          | 1995-08-07   | 2019-05-06     | 2019-05-06 | *      |
      | md5('1002') | md5('1995-08-07\|\|1002\|\|BEAH')    | Beah          | 1995-08-07   | 2019-05-07     | 2019-05-07 | *      |
      | md5('1003') | md5('1990-02-03\|\|1003\|\|CHARLEY') | Charley       | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
      | md5('1003') | md5('1990-02-03\|\|1003\|\|CHRIS')   | Chris         | 1990-02-03   | 2019-05-05     | 2019-05-05 | *      |
      | md5('1003') | md5('1990-02-03\|\|1003\|\|CLAIRE')  | Claire        | 1990-02-03   | 2019-05-06     | 2019-05-06 | *      |
      | md5('1003') | md5('1990-02-03\|\|1003\|\|CHARLEY') | Charley       | 1990-02-03   | 2019-05-07     | 2019-05-07 | *      |
      | md5('1004') | md5('1992-01-30\|\|1004\|\|DAVID')   | David         | 1992-01-30   | 2019-05-05     | 2019-05-05 | *      |
      | md5('1005') | md5('2001-07-23\|\|1005\|\|ELWYN')   | Elwyn         | 2001-07-23   | 2019-05-06     | 2019-05-06 | *      |
      | md5('1006') | md5('1960-01-01\|\|1006\|\|FREIA')   | Freia         | 1960-01-01   | 2019-05-06     | 2019-05-06 | *      |
      | md5('1007') | md5('1990-02-03\|\|1007\|\|GEOFF')   | Geoff         | 1990-02-03   | 2019-05-07     | 2019-05-07 | *      |
      | md5('1010') | md5('1991-03-21\|\|1010\|\|JENNY')   | Jenny         | 1991-03-21   | 2019-05-04     | 2019-05-04 | *      |
      | md5('1010') | md5('1991-03-25\|\|1010\|\|JENNY')   | Jenny         | 1991-03-25   | 2019-05-05     | 2019-05-05 | *      |
      | md5('1011') | md5('1978-06-16\|\|1011\|\|KAREN')   | Karen         | 1978-06-16   | 2019-05-07     | 2019-05-07 | *      |
      | md5('1012') | md5('1990-02-03\|\|1012\|\|ALBERT')  | Albert        | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
  
  # recently added  
  @fixture.satellite_cycle
  Scenario: [SAT-CYCLE-NULLS] SATELLITE load over several cycles with NULL records
    Given the RAW_STAGE stage is empty
    And the SATELLITE sat is empty

    # ================ DAY 1 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-01   | 2019-01-01     | 2019-01-01 | *      |
      | 1002        | Ben           | 17-214-233-1212 | 1990-02-02   | 2019-01-01     | 2019-01-01 | *      |
      | 1003        | Chad          | 17-214-233-1213 | 1990-02-03   | 2019-01-01     | 2019-01-01 | *      |
      | 1004        | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-01     | 2019-01-01 | *      |
      | 1005        | Frida         | 17-214-233-1215 | 1990-02-05   | 2019-01-01     | 2019-01-01 | *      |
      | 1006        | George        | 17-214-233-1216 | 1990-02-06   | 2019-01-01     | 2019-01-01 | *      |
      | 1007        | Harry         | 17-214-233-1217 | 1990-02-07   | 2019-01-01     | 2019-01-01 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 2 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | <null>      | <null>        | <null>          | 1990-02-01   | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | <null>        | 17-214-233-1211 | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | Albert        | <null>          | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | 1001        | <null>        | <null>          | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | <null>        | 17-214-233-1212 | 1990-02-02   | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | Ben           | 17-214-233-1212 | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | 1002        | <null>        | 17-214-233-1212 | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | Chad          | <null>          | 1990-02-03   | 2019-01-02     | 2019-01-02 | *      |
      | 1003        | <null>        | <null>          | 1990-02-03   | 2019-01-02     | 2019-01-02 | *      |
      | 1004        | Dom           | <null>          | <null>       | 2019-01-02     | 2019-01-02 | *      |

    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 3 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1005        | Frida         | <null>          | 1990-02-05   | 2019-01-03     | 2019-01-03 | *      |
      | 1006        | George        | 17-214-233-1216 | <null>       | 2019-01-03     | 2019-01-03 | *      |
      | 1007        | <null>        | 17-214-233-1217 | 1990-02-07   | 2019-01-03     | 2019-01-03 | *      |
      | <null>      | Charlie       | 17-214-233-1222 | 1988-08-08   | 2019-01-03     | 2019-01-03 | *      |

    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 4 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1311 | 1990-02-01   | 2019-01-04     | 2019-01-04 | *      |
      | 1002        | Ben           | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | 1003        | Chad          | 17-214-233-1313 | 1990-02-03   | 2019-01-04     | 2019-01-04 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-04   | 2019-01-04     | 2019-01-04 | *      |
      | 1005        | Frida         | 17-214-233-1315 | 1990-02-05   | 2019-01-04     | 2019-01-04 | *      |
      | 1006        | George        | 17-214-233-1316 | 1990-02-06   | 2019-01-04     | 2019-01-04 | *      |
      | 1007        | Harry         | 17-214-233-1317 | 1990-02-07   | 2019-01-04     | 2019-01-04 | *      |

    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # =============== CHECKS ===================
    Then the SATELLITE table should contain expected data
      | CUSTOMER_PK | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | HASHDIFF                                               | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | md5('1001') | Alice         | 17-214-233-1211 | 1990-02-01   | md5('1990-02-01\|\|1001\|\|ALICE\|\|17-214-233-1211')  | 2019-01-01     | 2019-01-01 | *      |
      | md5('1002') | Bob           | 17-214-233-1212 | 1990-02-02   | md5('1990-02-02\|\|1002\|\|BOB\|\|17-214-233-1212')    | 2019-01-01     | 2019-01-01 | *      |
      | md5('1003') | Chad          | 17-214-233-1213 | 1990-02-03   | md5('1990-02-03\|\|1003\|\|CHAD\|\|17-214-233-1213')   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1004') | Dom           | 17-214-233-1214 | 1990-02-04   | md5('1990-02-04\|\|1004\|\|DOM\|\|17-214-233-1214')    | 2019-01-01     | 2019-01-01 | *      |
      | md5('1005') | Frida         | 17-214-233-1215 | 1990-02-05   | md5('1990-02-05\|\|1005\|\|FRIDA\|\|17-214-233-1215')  | 2019-01-01     | 2019-01-01 | *      |
      | md5('1006') | George        | 17-214-233-1216 | 1990-02-06   | md5('1990-02-06\|\|1006\|\|GEORGE\|\|17-214-233-1216') | 2019-01-01     | 2019-01-01 | *      |
      | md5('1007') | Harry         | 17-214-233-1217 | 1990-02-07   | md5('1990-02-07\|\|1007\|\|HARRY\|\|17-214-233-1217')  | 2019-01-01     | 2019-01-01 | *      |
      | md5('1001') | <null>        | <null>          | <null>       | md5('^^\|\|1001\|\|^^\|\|^^')                          | 2019-01-02     | 2019-01-02 | *      |
      | md5('1002') | <null>        | 17-214-233-1212 | <null>       | md5('^^\|\|1002\|\|^^\|\|17-214-233-1212')             | 2019-01-02     | 2019-01-02 | *      |
      | md5('1003') | <null>        | <null>          | 1990-02-03   | md5('1990-02-03\|\|1003\|\|^^\|\|^^')                  | 2019-01-02     | 2019-01-02 | *      |
      | md5('1004') | Dom           | <null>          | <null>       | md5('^^\|\|1004\|\|DOM\|\|^^')                         | 2019-01-02     | 2019-01-02 | *      |
      | md5('1005') | Frida         | <null>          | 1990-02-05   | md5('1990-02-05\|\|1005\|\|FRIDA\|\|^^')               | 2019-01-03     | 2019-01-03 | *      |
      | md5('1006') | George        | 17-214-233-1216 | <null>       | md5('^^\|\|1006\|\|GEORGE\|\|17-214-233-1216')         | 2019-01-03     | 2019-01-03 | *      |
      | md5('1007') | <null>        | 17-214-233-1217 | 1990-02-07   | md5('1990-02-07\|\|1007\|\|^^\|\|17-214-233-1217')     | 2019-01-03     | 2019-01-03 | *      |
      | md5('1001') | Alice         | 17-214-233-1311 | 1990-02-01   | md5('1990-02-01\|\|1001\|\|ALICE\|\|17-214-233-1311')  | 2019-01-04     | 2019-01-04 | *      |
      | md5('1002') | Bob           | 17-214-233-1312 | 1990-02-02   | md5('1990-02-02\|\|1002\|\|BOB\|\|17-214-233-1312')    | 2019-01-04     | 2019-01-04 | *      |
      | md5('1003') | Chad          | 17-214-233-1313 | 1990-02-03   | md5('1990-02-03\|\|1003\|\|CHAD\|\|17-214-233-1313')   | 2019-01-04     | 2019-01-04 | *      |
      | md5('1004') | Dom           | 17-214-233-1314 | 1990-02-04   | md5('1990-02-04\|\|1004\|\|DOM\|\|17-214-233-1314')    | 2019-01-04     | 2019-01-04 | *      |
      | md5('1005') | Frida         | 17-214-233-1315 | 1990-02-05   | md5('1990-02-05\|\|1005\|\|FRIDA\|\|17-214-233-1315')  | 2019-01-04     | 2019-01-04 | *      |
      | md5('1006') | George        | 17-214-233-1316 | 1990-02-06   | md5('1990-02-06\|\|1006\|\|GEORGE\|\|17-214-233-1316') | 2019-01-04     | 2019-01-04 | *      |
      | md5('1007') | Harry         | 17-214-233-1317 | 1990-02-07   | md5('1990-02-07\|\|1007\|\|HARRY\|\|17-214-233-1317')  | 2019-01-04     | 2019-01-04 | *      |

  # recently added  
  @fixture.satellite_cycle
  Scenario: [SAT-CYCLE-NULLS] SATELLITE load over several cycles no PK in HASHDIFF and NULL records
    Given the RAW_STAGE stage is empty
    And the SATELLITE sat is empty

    # ================ DAY 1 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-01   | 2019-01-01     | 2019-01-01 | *      |
      | 1002        | Ben           | 17-214-233-1212 | 1990-02-02   | 2019-01-01     | 2019-01-01 | *      |
      | 1003        | Chad          | 17-214-233-1213 | 1990-02-03   | 2019-01-01     | 2019-01-01 | *      |
      | 1004        | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-01     | 2019-01-01 | *      |
      | 1005        | Frida         | 17-214-233-1215 | 1990-02-05   | 2019-01-01     | 2019-01-01 | *      |
      | 1006        | George        | 17-214-233-1216 | 1990-02-06   | 2019-01-01     | 2019-01-01 | *      |
      | 1007        | Harry         | 17-214-233-1217 | 1990-02-07   | 2019-01-01     | 2019-01-01 | *      |
    And I create the STG_CUSTOMER_NO_PK_HASHDIFF stage
    And I load the SATELLITE sat

    # ================ DAY 2 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | <null>      | <null>        | <null>          | 1990-02-01   | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | <null>        | 17-214-233-1211 | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | Albert        | <null>          | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | 1001        | <null>        | <null>          | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | <null>        | 17-214-233-1212 | 1990-02-02   | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | Ben           | 17-214-233-1212 | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | 1002        | <null>        | 17-214-233-1212 | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | <null>      | Chad          | <null>          | 1990-02-03   | 2019-01-02     | 2019-01-02 | *      |
      | 1003        | <null>        | <null>          | 1990-02-03   | 2019-01-02     | 2019-01-02 | *      |
      | 1004        | Dom           | <null>          | <null>       | 2019-01-02     | 2019-01-02 | *      |

    And I create the STG_CUSTOMER_NO_PK_HASHDIFF stage
    And I load the SATELLITE sat

    # ================ DAY 3 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1005        | Frida         | <null>          | 1990-02-05   | 2019-01-03     | 2019-01-03 | *      |
      | 1006        | George        | 17-214-233-1216 | <null>       | 2019-01-03     | 2019-01-03 | *      |
      | 1007        | <null>        | 17-214-233-1217 | 1990-02-07   | 2019-01-03     | 2019-01-03 | *      |
      | <null>      | Charlie       | 17-214-233-1222 | 1988-08-08   | 2019-01-03     | 2019-01-03 | *      |

    And I create the STG_CUSTOMER_NO_PK_HASHDIFF stage
    And I load the SATELLITE sat

    # ================ DAY 4 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1311 | 1990-02-01   | 2019-01-04     | 2019-01-04 | *      |
      | 1002        | Ben           | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | 1003        | Chad          | 17-214-233-1313 | 1990-02-03   | 2019-01-04     | 2019-01-04 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-04   | 2019-01-04     | 2019-01-04 | *      |
      | 1005        | Frida         | 17-214-233-1315 | 1990-02-05   | 2019-01-04     | 2019-01-04 | *      |
      | 1006        | George        | 17-214-233-1316 | 1990-02-06   | 2019-01-04     | 2019-01-04 | *      |
      | 1007        | Harry         | 17-214-233-1317 | 1990-02-07   | 2019-01-04     | 2019-01-04 | *      |

    And I create the STG_CUSTOMER_NO_PK_HASHDIFF stage
    And I load the SATELLITE sat

    # =============== CHECKS ===================
    Then the SATELLITE table should contain expected data
      | CUSTOMER_PK | HASHDIFF                                           | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | md5('1001') | md5('ALICE\|\|17-214-233-1211\|\|1990-02-01')      | Alice         | 17-214-233-1211 | 1990-02-01   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1002') | md5('BOB\|\|17-214-233-1212\|\|1990-02-02')        | Bob           | 17-214-233-1212 | 1990-02-02   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1003') | md5('CHAD\|\|17-214-233-1213\|\|1990-02-03')       | Chad          | 17-214-233-1213 | 1990-02-03   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1004') | md5('DOM\|\|17-214-233-1214\|\|1990-02-04')        | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1005') | md5('FRIDA\|\|17-214-233-1215\|\|1990-02-05')      | Frida         | 17-214-233-1215 | 1990-02-05   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1006') | md5('GEORGE\|\|17-214-233-1216\|\|1990-02-06')     | George        | 17-214-233-1216 | 1990-02-06   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1007') | md5('HARRY\|\|17-214-233-1217\|\|1990-02-07')      | Harry         | 17-214-233-1217 | 1990-02-07   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1001') | md5('^^\|\|^^\|\|^^')                              | <null>        | <null>          | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | md5('1002') | md5('^^\|\|17-214-233-1212\|\|^^')                 | <null>        | 17-214-233-1212 | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | md5('1003') | md5('^^\|\|^^\|\|1990-02-03')                      | <null>        | <null>          | 1990-02-03   | 2019-01-02     | 2019-01-02 | *      |
      | md5('1004') | md5('DOM\|\|^^\|\|^^')                             | Dom           | <null>          | <null>       | 2019-01-02     | 2019-01-02 | *      |
      | md5('1005') | md5('FRIDA\|\|^^\|\|1990-02-05')                   | Frida         | <null>          | 1990-02-05   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1006') | md5('GEORGE\|\|17-214-233-1216\|\|^^')             | George        | 17-214-233-1216 | <null>       | 2019-01-03     | 2019-01-03 | *      |
      | md5('1007') | md5('^^\|\|17-214-233-1217\|\|1990-02-07')         | <null>        | 17-214-233-1217 | 1990-02-07   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1001') | md5('ALICE\|\|17-214-233-1311\|\|1990-02-01')      | Alice         | 17-214-233-1311 | 1990-02-01   | 2019-01-04     | 2019-01-04 | *      |
      | md5('1002') | md5('BOB\|\|17-214-233-1312\|\|1990-02-02')        | Bob           | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | md5('1003') | md5('CHAD\|\|17-214-233-1313\|\|1990-02-03')       | Chad          | 17-214-233-1313 | 1990-02-03   | 2019-01-04     | 2019-01-04 | *      |
      | md5('1004') | md5('DOM\|\|17-214-233-1314\|\|1990-02-04')        | Dom           | 17-214-233-1314 | 1990-02-04   | 2019-01-04     | 2019-01-04 | *      |
      | md5('1005') | md5('FRIDA\|\|17-214-233-1315\|\|1990-02-05 ')     | Frida         | 17-214-233-1315 | 1990-02-05   | 2019-01-04     | 2019-01-04 | *      |
      | md5('1006') | md5('GEORGE\|\|17-214-233-1316\|\|\|\|1990-02-06') | George        | 17-214-233-1316 | 1990-02-06   | 2019-01-04     | 2019-01-04 | *      |
      | md5('1007') | md5('HARRY\|\|17-214-233-1317\|\|1990-02-07')      | Harry         | 17-214-233-1317 | 1990-02-07   | 2019-01-04     | 2019-01-04 | *      |

  # recently added
  @fixture.satellite_cycle
  Scenario: [SAT-CYCLE-DUPLICATES] SATELLITE load over several cycles with a mix of duplicate record change cases
    Given the RAW_STAGE stage is empty
    And the SATELLITE sat is empty

    # ================ DAY 1 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-01   | 2019-01-01     | 2019-01-01 | *      |
      | 1002        | Beth          | 17-214-233-1212 | 1990-02-02   | 2019-01-01     | 2019-01-01 | *      |
      | 1003        | Charley       | 17-214-233-1213 | 1990-02-03   | 2019-01-01     | 2019-01-01 | *      |
      | 1004        | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-01     | 2019-01-01 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 2 ===================
    # Between-load duplicates (or identical subsequent loads)
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-01   | 2019-01-02     | 2019-01-02 | *      |
      | 1002        | Beth          | 17-214-233-1212 | 1990-02-02   | 2019-01-02     | 2019-01-02 | *      |
      | 1003        | Charley       | 17-214-233-1213 | 1990-02-03   | 2019-01-02     | 2019-01-02 | *      |
      | 1004        | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-02     | 2019-01-02 | *      |
      | 1005        | Frida         | 17-214-233-1215 | 1990-02-05   | 2019-01-02     | 2019-01-02 | *      |

    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 3 ===================
    # Change of count/cdk/payload (and hashdiff) + intra-load duplicates
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-03     | 2019-01-03 | *      |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-03     | 2019-01-03 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-03     | 2019-01-03 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-03     | 2019-01-03 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-03     | 2019-01-03 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-03     | 2019-01-03 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-03     | 2019-01-03 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-03     | 2019-01-03 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-03     | 2019-01-03 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |

    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 4 ===================
    # Between-load + intra-load duplicates
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-04     | 2019-01-04 | *      |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-04     | 2019-01-04 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-04     | 2019-01-04 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-04     | 2019-01-04 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-04     | 2019-01-04 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-04     | 2019-01-04 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-04     | 2019-01-04 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-04     | 2019-01-04 | *      |

    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # =============== CHECKS ===================
    Then the SATELLITE table should contain expected data
      | CUSTOMER_PK | HASHDIFF                                                | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | md5('1001') | md5('1001\|\|ALBERT\|\|17-214-233-1211\|\|1990-02-01')  | Albert        | 17-214-233-1211 | 1990-02-01   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1002') | md5('1002\|\|BETH\|\|17-214-233-1212\|\|1990-02-02')    | Beth          | 17-214-233-1212 | 1990-02-02   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1003') | md5('1003\|\|CHARLEY\|\|17-214-233-1213\|\|1990-02-03') | Charley       | 17-214-233-1213 | 1990-02-03   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1004') | md5('1004\|\|DOM\|\|17-214-233-1214\|\|1990-02-04')     | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1005') | md5('1005\|\|FRIDA\|\|17-214-233-1215\|\|1990-02-05')   | Frida         | 17-214-233-1215 | 1990-02-05   | 2019-01-02     | 2019-01-02 | *      |
      | md5('1001') | md5('1001\|\|ALBERT\|\|17-214-233-1211\|\|1990-02-11')  | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1002') | md5('1002\|\|BETH\|\|17-214-233-1312\|\|1990-02-02')    | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1003') | md5('1003\|\|CHARLIE\|\|17-214-233-1213\|\|1990-02-03') | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1004') | md5('1004\|\|DOM\|\|17-214-233-1314\|\|1990-02-14')     | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1005') | md5('1005\|\|FREYA\|\|17-214-233-1315\|\|1990-02-15')   | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |
 
  # recently added
  @fixture.satellite_cycle
  Scenario: [SAT-CYCLE-DUPLICATES] SATELLITE load over several cycles with no PK in HASHDIFF and a mix of duplicate record change cases
    Given the RAW_STAGE stage is empty
    And the SATELLITE sat is empty

    # ================ DAY 1 ===================
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-01   | 2019-01-01     | 2019-01-01 | *      |
      | 1002        | Beth          | 17-214-233-1212 | 1990-02-02   | 2019-01-01     | 2019-01-01 | *      |
      | 1003        | Charley       | 17-214-233-1213 | 1990-02-03   | 2019-01-01     | 2019-01-01 | *      |
      | 1004        | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-01     | 2019-01-01 | *      |
    And I create the STG_CUSTOMER_NO_PK_HASHDIFF stage
    And I load the SATELLITE sat

    # ================ DAY 2 ===================
    # Between-load duplicates (or identical subsequent loads)
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-01   | 2019-01-02     | 2019-01-02 | *      |
      | 1002        | Beth          | 17-214-233-1212 | 1990-02-02   | 2019-01-02     | 2019-01-02 | *      |
      | 1003        | Charley       | 17-214-233-1213 | 1990-02-03   | 2019-01-02     | 2019-01-02 | *      |
      | 1004        | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-02     | 2019-01-02 | *      |
      | 1005        | Frida         | 17-214-233-1215 | 1990-02-05   | 2019-01-02     | 2019-01-02 | *      |

    And I create the STG_CUSTOMER_NO_PK_HASHDIFF stage
    And I load the SATELLITE sat

    # ================ DAY 3 ===================
    # Change of count/cdk/payload (and hashdiff) + intra-load duplicates
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-03     | 2019-01-03 | *      |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-03     | 2019-01-03 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-03     | 2019-01-03 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-03     | 2019-01-03 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-03     | 2019-01-03 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-03     | 2019-01-03 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-03     | 2019-01-03 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-03     | 2019-01-03 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-03     | 2019-01-03 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |

    And I create the STG_CUSTOMER_NO_PK_HASHDIFF stage
    And I load the SATELLITE sat

    # ================ DAY 4 ===================
    # Between-load + intra-load duplicates
    When the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-04     | 2019-01-04 | *      |
      | 1001        | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-04     | 2019-01-04 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | 1002        | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-04     | 2019-01-04 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-04     | 2019-01-04 | *      |
      | 1003        | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-04     | 2019-01-04 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-04     | 2019-01-04 | *      |
      | 1004        | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-04     | 2019-01-04 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-04     | 2019-01-04 | *      |
      | 1005        | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-04     | 2019-01-04 | *      |

    And I create the STG_CUSTOMER_NO_PK_HASHDIFF stage
    And I load the SATELLITE sat

    # =============== CHECKS ===================
    Then the SATELLITE table should contain expected data
      | CUSTOMER_PK | HASHDIFF                                        | CUSTOMER_NAME | CUSTOMER_PHONE  | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | md5('1001') | md5('ALBERT\|\|17-214-233-1211\|\|1990-02-01')  | Albert        | 17-214-233-1211 | 1990-02-01   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1002') | md5('BETH\|\|17-214-233-1212\|\|1990-02-02')    | Beth          | 17-214-233-1212 | 1990-02-02   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1003') | md5('CHARLEY\|\|17-214-233-1213\|\|1990-02-03') | Charley       | 17-214-233-1213 | 1990-02-03   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1004') | md5('DOM\|\|17-214-233-1214\|\|1990-02-04')     | Dom           | 17-214-233-1214 | 1990-02-04   | 2019-01-01     | 2019-01-01 | *      |
      | md5('1005') | md5('FRIDA\|\|17-214-233-1215\|\|1990-02-05')   | Frida         | 17-214-233-1215 | 1990-02-05   | 2019-01-02     | 2019-01-02 | *      |
      | md5('1001') | md5('ALBERT\|\|17-214-233-1211\|\|1990-02-11')  | Albert        | 17-214-233-1211 | 1990-02-11   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1002') | md5('BETH\|\|17-214-233-1312\|\|1990-02-02')    | Beth          | 17-214-233-1312 | 1990-02-02   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1003') | md5('CHARLIE\|\|17-214-233-1213\|\|1990-02-03') | Charlie       | 17-214-233-1213 | 1990-02-03   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1004') | md5('DOM\|\|17-214-233-1314\|\|1990-02-14')     | Dom           | 17-214-233-1314 | 1990-02-14   | 2019-01-03     | 2019-01-03 | *      |
      | md5('1005') | md5('FREYA\|\|17-214-233-1315\|\|1990-02-15')   | Freya         | 17-214-233-1315 | 1990-02-15   | 2019-01-03     | 2019-01-03 | *      |

  @fixture.satellite_cycle
  @fixture.sha
  Scenario: [SAT-CYCLE-SHA] SATELLITE load over several cycles
    Given the RAW_STAGE stage is empty
    And the SATELLITE sat is empty

    # ================ DAY 1 ===================
    And the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1001        | Albert        | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
      | 1002        | Beth          | 1995-08-07   | 2019-05-04     | 2019-05-04 | *      |
      | 1003        | Charley       | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
      | 1010        | Jenny         | 1991-03-21   | 2019-05-04     | 2019-05-04 | *      |
      | 1012        | Albert        | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 2 ===================
    And the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1002        | Beah          | 1995-08-07   | 2019-05-05     | 2019-05-05 | *      |
      | 1003        | Chris         | 1990-02-03   | 2019-05-05     | 2019-05-05 | *      |
      | 1004        | David         | 1992-01-30   | 2019-05-05     | 2019-05-05 | *      |
      | 1010        | Jenny         | 1991-03-25   | 2019-05-05     | 2019-05-05 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 3 ===================
    And the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1002        | Beth          | 1995-08-07   | 2019-05-06     | 2019-05-06 | *      |
      | 1003        | Claire        | 1990-02-03   | 2019-05-06     | 2019-05-06 | *      |
      | 1005        | Elwyn         | 2001-07-23   | 2019-05-06     | 2019-05-06 | *      |
      | 1006        | Freia         | 1960-01-01   | 2019-05-06     | 2019-05-06 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # ================ DAY 4 ===================
    And the RAW_STAGE is loaded
      | CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | 1002        | Beah          | 1995-08-07   | 2019-05-07     | 2019-05-07 | *      |
      | 1003        | Charley       | 1990-02-03   | 2019-05-07     | 2019-05-07 | *      |
      | 1007        | Geoff         | 1990-02-03   | 2019-05-07     | 2019-05-07 | *      |
      | 1010        | Jenny         | 1991-03-25   | 2019-05-07     | 2019-05-07 | *      |
      | 1011        | Karen         | 1978-06-16   | 2019-05-07     | 2019-05-07 | *      |
    And I create the STG_CUSTOMER stage
    And I load the SATELLITE sat

    # =============== CHECKS ===================
    Then the SATELLITE table should contain expected data
      | CUSTOMER_PK | HASHDIFF                             | CUSTOMER_NAME | CUSTOMER_DOB | EFFECTIVE_FROM | LOAD_DATE  | SOURCE |
      | sha('1001') | sha('1990-02-03\|\|1001\|\|ALBERT')  | Albert        | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
      | sha('1002') | sha('1995-08-07\|\|1002\|\|BETH')    | Beth          | 1995-08-07   | 2019-05-04     | 2019-05-04 | *      |
      | sha('1002') | sha('1995-08-07\|\|1002\|\|BEAH')    | Beah          | 1995-08-07   | 2019-05-05     | 2019-05-05 | *      |
      | sha('1002') | sha('1995-08-07\|\|1002\|\|BETH')    | Beth          | 1995-08-07   | 2019-05-06     | 2019-05-06 | *      |
      | sha('1002') | sha('1995-08-07\|\|1002\|\|BEAH')    | Beah          | 1995-08-07   | 2019-05-07     | 2019-05-07 | *      |
      | sha('1003') | sha('1990-02-03\|\|1003\|\|CHARLEY') | Charley       | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |
      | sha('1003') | sha('1990-02-03\|\|1003\|\|CHRIS')   | Chris         | 1990-02-03   | 2019-05-05     | 2019-05-05 | *      |
      | sha('1003') | sha('1990-02-03\|\|1003\|\|CLAIRE')  | Claire        | 1990-02-03   | 2019-05-06     | 2019-05-06 | *      |
      | sha('1003') | sha('1990-02-03\|\|1003\|\|CHARLEY') | Charley       | 1990-02-03   | 2019-05-07     | 2019-05-07 | *      |
      | sha('1004') | sha('1992-01-30\|\|1004\|\|DAVID')   | David         | 1992-01-30   | 2019-05-05     | 2019-05-05 | *      |
      | sha('1005') | sha('2001-07-23\|\|1005\|\|ELWYN')   | Elwyn         | 2001-07-23   | 2019-05-06     | 2019-05-06 | *      |
      | sha('1006') | sha('1960-01-01\|\|1006\|\|FREIA')   | Freia         | 1960-01-01   | 2019-05-06     | 2019-05-06 | *      |
      | sha('1007') | sha('1990-02-03\|\|1007\|\|GEOFF')   | Geoff         | 1990-02-03   | 2019-05-07     | 2019-05-07 | *      |
      | sha('1010') | sha('1991-03-21\|\|1010\|\|JENNY')   | Jenny         | 1991-03-21   | 2019-05-04     | 2019-05-04 | *      |
      | sha('1010') | sha('1991-03-25\|\|1010\|\|JENNY')   | Jenny         | 1991-03-25   | 2019-05-05     | 2019-05-05 | *      |
      | sha('1011') | sha('1978-06-16\|\|1011\|\|KAREN')   | Karen         | 1978-06-16   | 2019-05-07     | 2019-05-07 | *      |
      | sha('1012') | sha('1990-02-03\|\|1012\|\|ALBERT')  | Albert        | 1990-02-03   | 2019-05-04     | 2019-05-04 | *      |