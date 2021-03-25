from behave import fixture

from test_project.test_utils.dbt_test_utils import *

"""
The fixtures here are used to supply runtime metadata to tests, which are provided to the model generator.
"""


@fixture
def set_workdir(_):
    """
    Set the working (run) dir for dbt
    """

    os.chdir(TESTS_DBT_ROOT)


@fixture
def sha(context):
    """
    Augment the metadata for a vault structure load to work with SHA hashing instead of MD5
    """

    context.hashing = "SHA"

    if hasattr(context, "seed_config"):

        config = dict(context.seed_config)

        for k, v in config.items():

            for c, t in config[k]["+column_types"].items():

                if t == "BINARY(16)":
                    config[k]["+column_types"][c] = "BINARY(32)"

    else:
        raise ValueError("sha fixture used before vault structure fixture.")


@fixture
def staging(context):
    """
    Define the structures and metadata to load a hashed staging layer
    """

    context.seed_config = {

        "STG_CUSTOMER": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR",
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE"
            }
        },
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def single_source_hub(context):
    """
    Define the structures and metadata to load single-source hubs
    """

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "CUSTOMER_PK": "CUSTOMER_ID"
        }
    }

    context.vault_structure_columns = {
        "HUB": {
            "src_pk": "CUSTOMER_PK",
            "src_nk": "CUSTOMER_ID",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "HUB": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_ID": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def multi_source_hub(context):
    """
    Define the structures and metadata to load multi-source hubs
    """

    context.hashed_columns = {
        "STG_PARTS": {
            "PART_PK": "PART_ID"
        },
        "STG_SUPPLIER": {
            "PART_PK": "PART_ID",
            "SUPPLIER_PK": "SUPPLIER_ID"
        },
        "STG_LINEITEM": {
            "PART_PK": "PART_ID",
            "SUPPLIER_PK": "SUPPLIER_ID",
            "ORDER_PK": "ORDER_ID"
        }
    }

    context.vault_structure_columns = {
        "HUB": {
            "src_pk": "PART_PK",
            "src_nk": "PART_ID",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "HUB": {
            "+column_types": {
                "PART_PK": "BINARY(16)",
                "PART_ID": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_PARTS": {
            "+column_types": {
                "PART_ID": "VARCHAR",
                "PART_NAME": "VARCHAR",
                "PART_TYPE": "VARCHAR",
                "PART_SIZE": "VARCHAR",
                "PART_RETAILPRICE": "NUMBER(38,2)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_SUPPLIER": {
            "+column_types": {
                "PART_ID": "VARCHAR",
                "SUPPLIER_ID": "VARCHAR",
                "AVAILQTY": "FLOAT",
                "SUPPLYCOST": "NUMBER(38,2)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_LINEITEM": {
            "+column_types": {
                "ORDER_ID": "VARCHAR",
                "PART_ID": "VARCHAR",
                "SUPPLIER_ID": "VARCHAR",
                "LINENUMBER": "FLOAT",
                "QUANTITY": "FLOAT",
                "EXTENDED_PRICE": "NUMBER(38,2)",
                "DISCOUNT": "NUMBER(38,2)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def single_source_link(context):
    """
    Define the structures and metadata to load single-source links
    """

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "CUSTOMER_NATION_PK": ["CUSTOMER_ID", "NATION_ID"],
            "CUSTOMER_FK": "CUSTOMER_ID",
            "NATION_FK": "NATION_ID"
        }
    }

    context.vault_structure_columns = {
        "LINK": {
            "src_pk": "CUSTOMER_NATION_PK",
            "src_fk": ["CUSTOMER_FK", "NATION_FK"],
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "LINK": {
            "+column_types": {
                "CUSTOMER_NATION_PK": "BINARY(16)",
                "CUSTOMER_FK": "BINARY(16)",
                "NATION_FK": "BINARY(16)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "NATION_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def multi_source_link(context):
    """
    Define the structures and metadata to load single-source links
    """

    context.hashed_columns = {
        "STG_SAP": {
            "CUSTOMER_NATION_PK": ["CUSTOMER_ID", "NATION_ID"],
            "CUSTOMER_FK": "CUSTOMER_ID",
            "NATION_FK": "NATION_ID"
        },
        "STG_CRM": {
            "CUSTOMER_NATION_PK": ["CUSTOMER_ID", "NATION_ID"],
            "CUSTOMER_FK": "CUSTOMER_ID",
            "NATION_FK": "NATION_ID"
        },
        "STG_WEB": {
            "CUSTOMER_NATION_PK": ["CUSTOMER_ID", "NATION_ID"],
            "CUSTOMER_FK": "CUSTOMER_ID",
            "NATION_FK": "NATION_ID"
        },
    }

    context.vault_structure_columns = {
        "LINK": {
            "src_pk": "CUSTOMER_NATION_PK",
            "src_fk": ["CUSTOMER_FK", "NATION_FK"],
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "LINK": {
            "+column_types": {
                "CUSTOMER_NATION_PK": "BINARY(16)",
                "CUSTOMER_FK": "BINARY(16)",
                "NATION_FK": "BINARY(16)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_SAP": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "NATION_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_CRM": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "NATION_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_WEB": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "NATION_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def t_link(context):
    """
    Define the structures and metadata to load transactional links
    """

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "TRANSACTION_PK": ["CUSTOMER_ID", "ORDER_ID", "TRANSACTION_NUMBER"],
            "CUSTOMER_FK": "CUSTOMER_ID",
            "ORDER_FK": "ORDER_ID"
        }
    }

    context.derived_columns = {
        "STG_CUSTOMER": {
            "EFFECTIVE_FROM": "TRANSACTION_DATE"
        }
    }

    context.vault_structure_columns = {
        "T_LINK": {
            "src_pk": "TRANSACTION_PK",
            "src_fk": ["CUSTOMER_FK", "ORDER_FK"],
            "src_payload": ["TRANSACTION_NUMBER", "TRANSACTION_DATE",
                            "TYPE", "AMOUNT"],
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "ORDER_ID": "VARCHAR",
                "TRANSACTION_NUMBER": "NUMBER(38,0)",
                "TRANSACTION_DATE": "DATE",
                "TYPE": "VARCHAR",
                "AMOUNT": "NUMBER(38,2)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "T_LINK": {
            "+column_types": {
                "TRANSACTION_PK": "BINARY(16)",
                "CUSTOMER_FK": "BINARY(16)",
                "ORDER_FK": "BINARY(16)",
                "TRANSACTION_NUMBER": "NUMBER(38,0)",
                "TRANSACTION_DATE": "DATE",
                "TYPE": "VARCHAR",
                "AMOUNT": "NUMBER(38,2)",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def satellite(context):
    """
    Define the structures and metadata to load satellites
    """

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_ID", "CUSTOMER_DOB", "CUSTOMER_PHONE", "CUSTOMER_NAME"]}
        },
        "STG_CUSTOMER_TS": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_ID", "CUSTOMER_DOB", "CUSTOMER_PHONE", "CUSTOMER_NAME"]}
        }
    }

    context.derived_columns = {
        "STG_CUSTOMER": {
            "EFFECTIVE_FROM": "LOAD_DATE"
        },
        "STG_CUSTOMER_TS": {
            "EFFECTIVE_FROM": "LOAD_DATETIME"
        }
    }

    context.vault_structure_columns = {
        "SATELLITE": {
            "src_pk": "CUSTOMER_PK",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_PHONE", "CUSTOMER_DOB"],
            "src_hashdiff": "HASHDIFF",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "SATELLITE_TS": {
            "src_pk": "CUSTOMER_PK",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_PHONE", "CUSTOMER_DOB"],
            "src_hashdiff": "HASHDIFF",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATETIME",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "NUMBER(38, 0)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_TS": {
            "+column_types": {
                "CUSTOMER_ID": "NUMBER(38, 0)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "LOAD_DATETIME": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "SATELLITE": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SATELLITE_TS": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATETIME",
                "LOAD_DATETIME": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def satellite_cycle(context):
    """
    Define the structures and metadata to perform load cycles for satellites
    """

    context.hashed_columns = {
        "STG_CUSTOMER":
            {"CUSTOMER_PK": "CUSTOMER_ID",
             "HASHDIFF": {"is_hashdiff": True,
                          "columns": ["CUSTOMER_DOB", "CUSTOMER_ID", "CUSTOMER_NAME"]
                          }
             }
    }

    context.derived_columns = {
        "STG_CUSTOMER": {
            "EFFECTIVE_FROM": "LOAD_DATE"
        }
    }

    context.stage_columns = {
        "RAW_STAGE":
            ["CUSTOMER_ID",
             "CUSTOMER_NAME",
             "CUSTOMER_DOB",
             "EFFECTIVE_FROM",
             "LOAD_DATE",
             "SOURCE"]
    }

    context.vault_structure_columns = {
        "SATELLITE": {
            "src_pk": "CUSTOMER_PK",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_DOB"],
            "src_hashdiff": "HASHDIFF",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SATELLITE": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def eff_satellite(context):
    """
    Define the structures and metadata to load effectivity satellites
    """

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "CUSTOMER_ORDER_PK": ["CUSTOMER_ID", "ORDER_ID"],
            "CUSTOMER_PK": "CUSTOMER_ID",
            "ORDER_PK": "ORDER_ID"
        }
    }

    context.vault_structure_columns = {
        "EFF_SAT": {
            "src_pk": "CUSTOMER_ORDER_PK",
            "src_dfk": "ORDER_PK",
            "src_sfk": "CUSTOMER_PK",
            "src_start_date": "START_DATE",
            "src_end_date": "END_DATE",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "NUMBER(38, 0)",
                "ORDER_ID": "VARCHAR",
                "START_DATE": "DATE",
                "END_DATE": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "EFF_SAT": {
            "+column_types": {
                "CUSTOMER_ORDER_PK": "BINARY(16)",
                "CUSTOMER_PK": "BINARY(16)",
                "ORDER_PK": "BINARY(16)",
                "START_DATE": "DATE",
                "END_DATE": "DATE",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def eff_satellite_multipart(context):
    """
    Define the structures and metadata to load effectivity satellites with multipart keys
    """

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "CUSTOMER_ORDER_PK": ["CUSTOMER_ID", "ORDER_ID", "NATION_ID", "PLATFORM_ID", "ORGANISATION_ID"],
            "CUSTOMER_PK": "CUSTOMER_ID",
            "NATION_PK": "NATION_ID",
            "ORDER_PK": "ORDER_ID",
            "PLATFORM_PK": "PLATFORM_ID",
            "ORGANISATION_PK": "ORGANISATION_ID"
        }
    }

    context.vault_structure_columns = {
        "EFF_SAT": {
            "src_pk": "CUSTOMER_ORDER_PK",
            "src_dfk": ["ORDER_PK", "PLATFORM_PK", "ORGANISATION_PK"],
            "src_sfk": ["CUSTOMER_PK", "NATION_PK"],
            "src_start_date": "START_DATE",
            "src_end_date": "END_DATE",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "NUMBER(38, 0)",
                "NATION_ID": "VARCHAR",
                "ORDER_ID": "VARCHAR",
                "PLATFORM_ID": "VARCHAR",
                "ORGANISATION_ID": "VARCHAR",
                "START_DATE": "DATE",
                "END_DATE": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "EFF_SAT": {
            "+column_types": {
                "CUSTOMER_ORDER_PK": "BINARY(16)",
                "ORDER_PK": "BINARY(16)",
                "PLATFORM_PK": "BINARY(16)",
                "ORGANISATION_PK": "BINARY(16)",
                "CUSTOMER_PK": "BINARY(16)",
                "NATION_PK": "BINARY(16)",
                "START_DATE": "DATE",
                "END_DATE": "DATE",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def xts(context):
    """
    Define the structures and metadata to load xts
    """

    context.vault_structure_type = "xts"

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_ID", "CUSTOMER_FIRSTNAME", "CUSTOMER_LASTNAME"]}
        },
        "STG_CUSTOMER_1": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_ID", "CUSTOMER_FIRSTNAME", "CUSTOMER_LASTNAME"]}
        },
        "STG_CUSTOMER_2": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_ID", "CUSTOMER_FIRSTNAME", "CUSTOMER_LASTNAME"]}
        },
        "STG_CUSTOMER_2SAT": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF_1": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_FIRSTNAME", "CUSTOMER_LASTNAME"]},
            "HASHDIFF_2": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_DOB", "CUSTOMER_PHONE"]}
        },
        "STG_CUSTOMER_2SAT_1": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF_1": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_FIRSTNAME", "CUSTOMER_LASTNAME"]},
            "HASHDIFF_2": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_DOB", "CUSTOMER_PHONE"]}
        },
        "STG_CUSTOMER_2SAT_2": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF_1": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_FIRSTNAME", "CUSTOMER_LASTNAME"]},
            "HASHDIFF_2": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_DOB", "CUSTOMER_PHONE"]}
        },
        "STG_CUSTOMER_3SAT": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF_1": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_FIRSTNAME", "CUSTOMER_LASTNAME"]},
            "HASHDIFF_2": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_DOB", "CUSTOMER_PHONE"]},
            "HASHDIFF_3": {"is_hashdiff": True,
                           "columns": ["CUSTOMER_ID", "CUSTOMER_COUNTY", "CUSTOMER_CITY"]}
        }
    }

    context.derived_columns = {
        "STG_CUSTOMER": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "SATELLITE_NAME": "!SAT_CUSTOMER"
        },
        "STG_CUSTOMER_1": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "SATELLITE_NAME": "!SAT_CUSTOMER"
        },
        "STG_CUSTOMER_2": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "SATELLITE_NAME": "!SAT_CUSTOMER"
        },
        "STG_CUSTOMER_2SAT": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "SATELLITE_1": "!SAT_CUSTOMER",
            "SATELLITE_2": "!SAT_CUSTOMER_DETAILS",
        },
        "STG_CUSTOMER_2SAT_1": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "SATELLITE_1": "!SAT_CUSTOMER",
            "SATELLITE_2": "!SAT_CUSTOMER_DETAILS",
        },
        "STG_CUSTOMER_2SAT_2": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "SATELLITE_1": "!SAT_CUSTOMER",
            "SATELLITE_2": "!SAT_CUSTOMER_DETAILS",
        },
        "STG_CUSTOMER_3SAT": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "SATELLITE_1": "!SAT_CUSTOMER",
            "SATELLITE_2": "!SAT_CUSTOMER_DETAILS",
            "SATELLITE_3": "!SAT_CUSTOMER_LOCATION",
        }
    }

    context.vault_structure_columns = {
        "XTS": {
            "src_pk": "CUSTOMER_PK",
            "src_ldts": "LOAD_DATE",
            "src_satellite": {
                "SATELLITE_CUSTOMER": {
                    "sat_name": {
                        "SATELLITE_NAME": "SATELLITE_NAME"
                    },
                    "hashdiff": {
                        "HASHDIFF": "HASHDIFF"
                    }
                },
            },
            "src_source": "SOURCE"
        },
        "XTS_2SAT": {
            "src_pk": "CUSTOMER_PK",
            "src_ldts": "LOAD_DATE",
            "src_satellite": {
                "SATELLITE_CUSTOMER": {
                    "sat_name": {
                        "SATELLITE_NAME": "SATELLITE_1"
                    },
                    "hashdiff": {
                        "HASHDIFF": "HASHDIFF_1"
                    }
                },
                "SATELLITE_CUSTOMER_DETAILS": {
                    "sat_name": {
                        "SATELLITE_NAME": "SATELLITE_2"
                    },
                    "hashdiff": {
                        "HASHDIFF": "HASHDIFF_2"
                    }
                }
            },
            "src_source": "SOURCE"
        },
        "XTS_3SAT": {
            "src_pk": "CUSTOMER_PK",
            "src_ldts": "LOAD_DATE",
            "src_satellite": {
                "SATELLITE_CUSTOMER": {
                    "sat_name": {
                        "SATELLITE_NAME": "SATELLITE_1"
                    },
                    "hashdiff": {
                        "HASHDIFF": "HASHDIFF_1"
                    }
                },
                "SATELLITE_CUSTOMER_DETAILS": {
                    "sat_name": {
                        "SATELLITE_NAME": "SATELLITE_2"
                    },
                    "hashdiff": {
                        "HASHDIFF": "HASHDIFF_2"
                    }
                },
                "SATELLITE_CUSTOMER_LOCATION": {
                    "sat_name": {
                        "SATELLITE_NAME": "SATELLITE_3"
                    },
                    "hashdiff": {
                        "HASHDIFF": "HASHDIFF_3"
                    }
                }
            },
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR",
            }
        },
        "RAW_STAGE_1": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR",
            }
        },
        "RAW_STAGE_2": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR",
            }
        },
        "RAW_STAGE_2SAT": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR",
            }
        },
        "RAW_STAGE_2SAT_1": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR",
            }
        },
        "RAW_STAGE_2SAT_2": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR",
            }
        },
        "RAW_STAGE_3SAT": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR",
            }
        },
        "STG_CUSTOMER": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "SATELLITE_NAME": "VARCHAR",
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "STG_CUSTOMER_2SAT": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF_1": "BINARY(16)",
                "HASHDIFF_2": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "SATELLITE_1": "VARCHAR",
                "SATELLITE_2": "VARCHAR",
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "STG_CUSTOMER_3SAT": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF_1": "BINARY(16)",
                "HASHDIFF_2": "BINARY(16)",
                "HASHDIFF_3": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "SATELLITE_1": "VARCHAR",
                "SATELLITE_2": "VARCHAR",
                "SATELLITE_3": "VARCHAR",
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_FIRSTNAME": "VARCHAR",
                "CUSTOMER_LASTNAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_COUNTY": "VARCHAR",
                "CUSTOMER_CITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "XTS": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "LOAD_DATE": "DATE",
                "SATELLITE_NAME": "VARCHAR",
                "HASHDIFF": "BINARY(16)",
                "SOURCE": "VARCHAR"
            }
        },
        "XTS_2SAT": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "SATELLITE_NAME": "VARCHAR",
                "HASHDIFF": "BINARY(16)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "XTS_3SAT": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "SATELLITE_NAME": "VARCHAR",
                "HASHDIFF": "BINARY(16)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def out_of_sequence_satellite(context):
    context.vault_structure_type = "xts"

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_ID", "CUSTOMER_DOB", "CUSTOMER_PHONE", "CUSTOMER_NAME"]}
        },
        "STG_CUSTOMER_TIMESTAMP": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_ID", "CUSTOMER_DOB", "CUSTOMER_PHONE", "CUSTOMER_NAME"]}
        }
    }

    context.derived_columns = {
        "STG_CUSTOMER": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "SATELLITE_NAME": "!SAT_CUSTOMER_OOS"
        },
        "STG_CUSTOMER_TIMESTAMP": {
            "EFFECTIVE_FROM": "LOAD_DATETIME",
            "SATELLITE_NAME": "!SAT_CUSTOMER_OOS_TIMESTAMP"
        }
    }

    context.vault_structure_columns = {
        "SAT_CUSTOMER_OOS": {
            "src_pk": "CUSTOMER_PK",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_PHONE", "CUSTOMER_DOB"],
            "src_hashdiff": "HASHDIFF",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE",
            "out_of_sequence": {
                "source_xts": "XTS",
                "sat_name_col": "SATELLITE_NAME",
                "insert_date": "1993-01-03"
            }
        },
        "SAT_CUSTOMER_OOS_EARLY": {
            "src_pk": "CUSTOMER_PK",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_PHONE", "CUSTOMER_DOB"],
            "src_hashdiff": "HASHDIFF",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE",
            "out_of_sequence": {
                "source_xts": "XTS",
                "sat_name_col": "SATELLITE_NAME",
                "insert_date": "1992-12-31"
            }
        },
        "SAT_CUSTOMER_OOS_LATE": {
            "src_pk": "CUSTOMER_PK",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_PHONE", "CUSTOMER_DOB"],
            "src_hashdiff": "HASHDIFF",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE",
            "out_of_sequence": {
                "source_xts": "XTS",
                "sat_name_col": "SATELLITE_NAME",
                "insert_date": "1993-01-09"
            }
        },
        "SATELLITE": {
            "src_pk": "CUSTOMER_PK",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_PHONE", "CUSTOMER_DOB"],
            "src_hashdiff": "HASHDIFF",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "SAT_CUSTOMER_OOS_TIMESTAMP": {
            "src_pk": "CUSTOMER_PK",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_PHONE", "CUSTOMER_DOB"],
            "src_hashdiff": "HASHDIFF",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATETIME",
            "src_source": "SOURCE",
            "out_of_sequence": {
                "source_xts": "XTS_TIMESTAMP",
                "sat_name_col": "SATELLITE_NAME",
                "insert_timestamp": "1993-01-01 01:01:03"
            }
        },
        "XTS": {
            "src_pk": "CUSTOMER_PK",
            "src_ldts": "LOAD_DATE",
            "src_satellite": {
                "SAT_CUSTOMER_OOS": {
                    "sat_name": {
                        "SATELLITE_NAME": "SATELLITE_NAME"
                    },
                    "hashdiff": {
                        "HASHDIFF": "HASHDIFF"
                    }
                },
            },
            "src_source": "SOURCE"
        },
        "XTS_TIMESTAMP": {
            "src_pk": "CUSTOMER_PK",
            "src_ldts": "LOAD_DATETIME",
            "src_satellite": {
                "SAT_CUSTOMER_OOS_TIMESTAMP": {
                    "sat_name": {
                        "SATELLITE_NAME": "SATELLITE_NAME"
                    },
                    "hashdiff": {
                        "HASHDIFF": "HASHDIFF"
                    }
                },
            },
            "src_source": "SOURCE"
        }
    }

    context.seed_config = {
        "RAW_STAGE": {
            "+column_types": {
                "CUSTOMER_ID": "NUMBER(38, 0)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_TIMESTAMP": {
            "+column_types": {
                "CUSTOMER_ID": "NUMBER(38, 0)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "LOAD_DATETIME": "TIMESTAMP",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_CUSTOMER_OOS": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_CUSTOMER_OOS_EARLY": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_CUSTOMER_OOS_LATE": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SATELLITE": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_CUSTOMER_OOS_TIMESTAMP": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_PHONE": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "HASHDIFF": "BINARY(16)",
                "EFFECTIVE_FROM": "TIMESTAMP",
                "LOAD_DATETIME": "TIMESTAMP",
                "SOURCE": "VARCHAR"
            }
        },
        "XTS": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "LOAD_DATE": "DATE",
                "SATELLITE_NAME": "VARCHAR",
                "HASHDIFF": "BINARY(16)",
                "SOURCE": "VARCHAR"
            }
        },
        "XTS_TIMESTAMP": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "LOAD_DATETIME": "TIMESTAMP",
                "SATELLITE_NAME": "VARCHAR",
                "HASHDIFF": "BINARY(16)",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def bridge(context):
    """
    Define the structures and metadata to perform bridge load
    """

    context.vault_structure_type = "bridge"

    context.hashed_columns = {
        "STG_CUSTOMER_ORDER_PRODUCT": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "ORDER_PK": "ORDER_ID",
            "PRODUCT_PK": "PRODUCT_ID",
            "CUSTOMER_ORDER_PK": {"is_hashdiff": True,
                        "columns": ["CUSTOMER_ID", "ORDER_ID"]
                        },
            "ORDER_PRODUCT_PK": {"is_hashdiff": True,
                             "columns": ["ORDER_ID", "PRODUCT_ID"]
                        }
        }
    }

    context.derived_columns = {
        "STG_CUSTOMER_ORDER_PRODUCT": {
            "EFFECTIVE_FROM": "LOAD_DATE",
            "START_DATE": "LOAD_DATE"
        }
    }

    context.vault_structure_columns = {
        "HUB_CUSTOMER": {
            "source_model": "STG_CUSTOMER_ORDER_PRODUCT",
            "src_pk": "CUSTOMER_PK",
            "src_nk": "CUSTOMER_ID",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "LINK_CUSTOMER_ORDER": {
            "source_model": "STG_CUSTOMER_ORDER_PRODUCT",
            "src_pk": "CUSTOMER_ORDER_PK",
            "src_fk": ["CUSTOMER_PK", "ORDER_PK"],
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "LINK_ORDER_PRODUCT": {
            "source_model": "STG_CUSTOMER_ORDER_PRODUCT",
            "src_pk": "ORDER_PRODUCT_PK",
            "src_fk": ["ORDER_PK", "PRODUCT_PK"],
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "EFF_SAT_CUSTOMER_ORDER": {
            "source_model": "STG_CUSTOMER_ORDER_PRODUCT",
            "src_pk": "CUSTOMER_ORDER_PK",
            "src_start_date": "START_DATE",
            "src_end_date": "END_DATE",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "EFF_SAT_ORDER_PRODUCT": {
            "source_model": "STG_CUSTOMER_ORDER_PRODUCT",
            "src_pk": "ORDER_PRODUCT_PK",
            "src_fk": ["ORDER_PK", "PRODUCT_PK"],
            "src_start_date": "START_DATE",
            "src_end_date": "END_DATE",
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "BRIDGE_CUSTOMER": {
            "source_model": "HUB_CUSTOMER",
            "src_pk": "CUSTOMER_PK",
            "links_and_eff_sats": {
                "CUSTOMER_ORDER": {
                    "pk":
                        {"PK": "CUSTOMER_ORDER_PK"},
                    "end_date":
                        {"END_DATE": "END_DATE"}
                },
                "ORDER_PRODUCT": {
                    "pk":
                        {"PK": "ORDER_PRODUCT_PK"},
                    "end_date":
                        {"END_DATE": "END_DATE"}
                }
            },
            "as_of_date_table": "AS_OF_DATE"
        }
    }

    context.stage_columns = {
        "RAW_CUSTOMER_ORDER_NATION":
            ["CUSTOMER_ID",
             "ORDER_ID",
             "NATION_ID",
             "LOAD_DATE",
             "SOURCE"]
    }

    context.seed_config = {
        "RAW_CUSTOMER_ORDER_NATION": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "ORDER_ID": "VARCHAR",
                "NATION_ID": "VARCHAR",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "HUB_CUSTOMER": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_ID": "VARCHAR",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "LINK_CUSTOMER_ORDER": {
            "+column_types": {
                "CUSTOMER_ORDER_PK": "BINARY(16)",
                "CUSTOMER_FK": "BINARY(16)",
                "ORDER_FK": "BINARY(16)",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "LINK_CUSTOMER_NATION": {
            "+column_types": {
                "CUSTOMER_NATION_PK": "BINARY(16)",
                "CUSTOMER_FK": "BINARY(16)",
                "NATION_FK": "BINARY(16)",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "EFF_SAT_CUSTOMER_ORDER": {
            "+column_types": {
                "CUSTOMER_ORDER_PK": "BINARY(16)",
                "CUSTOMER_FK": "BINARY(16)",
                "ORDER_FK": "BINARY(16)",
                "START_DATE": "DATETIME",
                "END_DATE": "DATETIME",
                "EFFECTIVE_FROM": "DATETIME",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "EFF_SAT_CUSTOMER_NATION": {
            "+column_types": {
                "CUSTOMER_NATION_PK": "BINARY(16)",
                "CUSTOMER_FK": "BINARY(16)",
                "NATION_FK": "BINARY(16)",
                "START_DATE": "DATETIME",
                "END_DATE": "DATETIME",
                "EFFECTIVE_FROM": "DATETIME",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "AS_OF_DATE": {
            "+column_types": {
                "AS_OF_DATE": "DATETIME"
            }
        },
        "BRIDGE_CUSTOMER": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "AS_OF_DATE": "DATETIME",
                "LINK_CO_PK": "BINARY(16)",
                "EFF_CO_END_DATE": "DATETIME",
                "LINK_CN_PK": "BINARY(16)",
                "EFF_CN_END_DATE": "DATETIME"
            }
        }
    }


@fixture
def cycle(context):
    """
    Define the structures and metadata to perform vault load cycles
    """

    context.hashed_columns = {
        "STG_CUSTOMER": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_DOB", "CUSTOMER_ID", "CUSTOMER_NAME"]
                         }
        },
        "STG_BOOKING": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "BOOKING_PK": "BOOKING_ID",
            "CUSTOMER_BOOKING_PK": ["CUSTOMER_ID", "BOOKING_ID"],
            "HASHDIFF_BOOK_CUSTOMER_DETAILS": {"is_hashdiff": True,
                                               "columns": ["CUSTOMER_ID",
                                                           "NATIONALITY",
                                                           "PHONE"]
                                               },
            "HASHDIFF_BOOK_BOOKING_DETAILS": {"is_hashdiff": True,
                                              "columns": ["BOOKING_ID",
                                                          "BOOKING_DATE",
                                                          "PRICE",
                                                          "DEPARTURE_DATE",
                                                          "DESTINATION"]
                                              }
        }
    }

    context.derived_columns = {
        "STG_CUSTOMER": {
            "EFFECTIVE_FROM": "LOAD_DATE"
        },
        "STG_BOOKING": {
            "EFFECTIVE_FROM": "BOOKING_DATE"
        }
    }

    context.vault_structure_columns = {
        "HUB_CUSTOMER": {
            "source_model": ["STG_CUSTOMER",
                             "STG_BOOKING"],
            "src_pk": "CUSTOMER_PK",
            "src_nk": "CUSTOMER_ID",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "HUB_BOOKING": {
            "source_model": "STG_BOOKING",
            "src_pk": "BOOKING_PK",
            "src_nk": "BOOKING_ID",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "LINK_CUSTOMER_BOOKING": {
            "source_model": "STG_BOOKING",
            "src_pk": "CUSTOMER_BOOKING_PK",
            "src_fk": ["CUSTOMER_PK", "BOOKING_PK"],
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "SAT_CUST_CUSTOMER_DETAILS": {
            "source_model": "STG_CUSTOMER",
            "src_pk": "CUSTOMER_PK",
            "src_hashdiff": "HASHDIFF",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_DOB"],
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "SAT_BOOK_CUSTOMER_DETAILS": {
            "source_model": "STG_BOOKING",
            "src_pk": "CUSTOMER_PK",
            "src_hashdiff": {"source_column": "HASHDIFF_BOOK_CUSTOMER_DETAILS",
                             "alias": "HASHDIFF"},
            "src_payload": ["PHONE", "NATIONALITY"],
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "SAT_BOOK_BOOKING_DETAILS": {
            "source_model": "STG_BOOKING",
            "src_pk": "BOOKING_PK",
            "src_hashdiff": {"source_column": "HASHDIFF_BOOK_BOOKING_DETAILS",
                             "alias": "HASHDIFF"},
            "src_payload": ["PRICE", "BOOKING_DATE",
                            "DEPARTURE_DATE", "DESTINATION"],
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        }
    }

    context.stage_columns = {
        "RAW_STAGE_CUSTOMER":
            ["CUSTOMER_ID",
             "CUSTOMER_NAME",
             "CUSTOMER_DOB",
             "EFFECTIVE_FROM",
             "LOAD_DATE",
             "SOURCE"],

        "RAW_STAGE_BOOKING":
            ["BOOKING_ID",
             "CUSTOMER_ID",
             "BOOKING_DATE",
             "PRICE",
             "DEPARTURE_DATE",
             "DESTINATION",
             "PHONE",
             "NATIONALITY",
             "LOAD_DATE",
             "SOURCE"]
    }

    context.seed_config = {
        "RAW_STAGE_CUSTOMER": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_BOOKING": {
            "+column_types": {
                "BOOKING_ID": "VARCHAR",
                "CUSTOMER_ID": "VARCHAR",
                "PRICE": "NUMBER(38,2)",
                "DEPARTURE_DATE": "DATE",
                "BOOKING_DATE": "DATE",
                "PHONE": "VARCHAR",
                "DESTINATION": "VARCHAR",
                "NATIONALITY": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "HUB_CUSTOMER": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_ID": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "HUB_BOOKING": {
            "+column_types": {
                "BOOKING_PK": "BINARY(16)",
                "BOOKING_ID": "VARCHAR",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "LINK_CUSTOMER_BOOKING": {
            "+column_types": {
                "CUSTOMER_BOOKING_PK": "BINARY(16)",
                "CUSTOMER_PK": "BINARY(16)",
                "BOOKING_PK": "BINARY(16)",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_CUST_CUSTOMER_DETAILS": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_BOOK_CUSTOMER_DETAILS": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF": "BINARY(16)",
                "PHONE": "VARCHAR",
                "NATIONALITY": "VARCHAR",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_BOOK_BOOKING_DETAILS": {
            "+column_types": {
                "BOOKING_PK": "BINARY(16)",
                "HASHDIFF": "BINARY(16)",
                "PRICE": "NUMBER(38,2)",
                "BOOKING_DATE": "DATE",
                "DEPARTURE_DATE": "DATE",
                "DESTINATION": "VARCHAR",
                "EFFECTIVE_FROM": "DATE",
                "LOAD_DATE": "DATE",
                "SOURCE": "VARCHAR"
            }
        }
    }


@fixture
def pit(context):
    """
    Define the structures and metadata to perform PIT load
    """

    context.vault_structure_type = "pit"

    context.hashed_columns = {
        "STG_CUSTOMER_DETAILS": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["CUSTOMER_ADDRESS", "CUSTOMER_DOB", "CUSTOMER_NAME"]
                         }
        },
        "STG_CUSTOMER_LOGIN": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["DEVICE_USED", "LAST_LOGIN_DATE"]
                         }
        },
        "STG_CUSTOMER_PROFILE": {
            "CUSTOMER_PK": "CUSTOMER_ID",
            "HASHDIFF": {"is_hashdiff": True,
                         "columns": ["DASHBOARD_COLOUR", "DISPLAY_NAME"]
                         }
        }
    }

    context.derived_columns = {
        "STG_CUSTOMER_DETAILS": {
            "EFFECTIVE_FROM": "LOAD_DATE"
        },
        "STG_CUSTOMER_LOGIN": {
            "EFFECTIVE_FROM": "LOAD_DATE"
        },
        "STG_CUSTOMER_PROFILE": {
            "EFFECTIVE_FROM": "LOAD_DATE"
        }
    }

    context.vault_structure_columns = {
        "HUB_CUSTOMER": {
            "source_model": ["STG_CUSTOMER_DETAILS",
                             "STG_CUSTOMER_LOGIN",
                             "STG_CUSTOMER_PROFILE"],
            "src_pk": "CUSTOMER_PK",
            "src_nk": "CUSTOMER_ID",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "SAT_CUSTOMER_DETAILS": {
            "source_model": "STG_CUSTOMER_DETAILS",
            "src_pk": "CUSTOMER_PK",
            "src_hashdiff": "HASHDIFF",
            "src_payload": ["CUSTOMER_NAME", "CUSTOMER_ADDRESS", "CUSTOMER_DOB"],
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "SAT_CUSTOMER_LOGIN": {
            "source_model": "STG_CUSTOMER_LOGIN",
            "src_pk": "CUSTOMER_PK",
            "src_hashdiff": "HASHDIFF",
            "src_payload": ["LAST_LOGIN_DATE", "DEVICE_USED"],
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "SAT_CUSTOMER_PROFILE": {
            "source_model": "STG_CUSTOMER_PROFILE",
            "src_pk": "CUSTOMER_PK",
            "src_hashdiff": "HASHDIFF",
            "src_payload": ["DASHBOARD_COLOUR", "DISPLAY_NAME"],
            "src_eff": "EFFECTIVE_FROM",
            "src_ldts": "LOAD_DATE",
            "src_source": "SOURCE"
        },
        "PIT_CUSTOMER": {
            "source_model": "HUB_CUSTOMER",
            "src_pk": "CUSTOMER_PK",
            "as_of_dates_table": "AS_OF_DATE",
            "satellites":
                {
                    "SAT_CUSTOMER_DETAILS": {
                        "pk":
                            {"PK": "CUSTOMER_PK"},
                        "ldts":
                            {"LDTS": "LOAD_DATE"}
                    },
                    "SAT_CUSTOMER_LOGIN": {
                        "pk":
                            {"PK": "CUSTOMER_PK"},
                        "ldts":
                            {"LDTS": "LOAD_DATE"}
                    },
                    "SAT_CUSTOMER_PROFILE": {
                        "pk":
                            {"PK": "CUSTOMER_PK"},
                        "ldts":
                            {"LDTS": "LOAD_DATE"}
                    }
                }
        }
    }

    context.stage_columns = {
        "RAW_STAGE_DETAILS":
            ["CUSTOMER_ID",
             "CUSTOMER_NAME",
             "CUSTOMER_ADDRESS",
             "CUSTOMER_DOB",
             "LOAD_DATE",
             "SOURCE"]
        ,
        "RAW_STAGE_LOGIN":
            ["CUSTOMER_ID",
             "LAST_LOGIN_DATE",
             "DEVICE_USED",
             "LOAD_DATE",
             "SOURCE"]
        ,
        "RAW_STAGE_PROFILE":
            ["CUSTOMER_ID",
             "DASHBOARD_COLOUR",
             "DISPLAY_NAME",
             "LOAD_DATE",
             "SOURCE"]
    }

    context.seed_config = {
        "RAW_STAGE_DETAILS": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_ADDRESS": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_LOGIN": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "LAST_LOGIN_DATE": "DATETIME",
                "DEVICE_USED": "VARCHAR",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "RAW_STAGE_PROFILE": {
            "+column_types": {
                "CUSTOMER_ID": "VARCHAR",
                "DASHBOARD_COLOUR": "VARCHAR",
                "DISPLAY_NAME": "VARCHAR",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "HUB_CUSTOMER": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "CUSTOMER_ID": "VARCHAR",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_CUSTOMER_DETAILS": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF": "BINARY(16)",
                "CUSTOMER_NAME": "VARCHAR",
                "CUSTOMER_ADDRESS": "VARCHAR",
                "CUSTOMER_DOB": "DATE",
                "EFFECTIVE_FROM": "DATETIME",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_CUSTOMER_LOGIN": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF": "BINARY(16)",
                "DEVICE_USED": "VARCHAR",
                "LAST_LOGIN_DATE": "DATETIME",
                "EFFECTIVE_FROM": "DATETIME",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "SAT_CUSTOMER_PROFILE": {
            "+column_types": {
                "CUSTOMER_PK": "BINARY(16)",
                "HASHDIFF": "BINARY(16)",
                "DASHBOARD_COLOUR": "VARCHAR",
                "DISPLAY_NAME": "VARCHAR",
                "EFFECTIVE_FROM": "DATETIME",
                "LOAD_DATE": "DATETIME",
                "SOURCE": "VARCHAR"
            }
        },
        "AS_OF_DATE": {
            "+column_types": {
                "AS_OF_DATE": "DATETIME"
            }
        },
        "PIT_CUSTOMER": {
            "+column_types": {
                "AS_OF_DATE": "DATETIME",
                "CUSTOMER_PK": "BINARY(16)",
                "SAT_CUSTOMER_DETAILS_PK": "BINARY(16)",
                "SAT_CUSTOMER_DETAILS_LDTS": "DATETIME",
                "SAT_CUSTOMER_LOGIN_PK": "BINARY(16)",
                "SAT_CUSTOMER_LOGIN_LDTS": "DATETIME",
                "SAT_CUSTOMER_PROFILE_PK": "BINARY(16)",
                "SAT_CUSTOMER_PROFILE_LDTS": "DATETIME"
            }
        }
    }


@fixture
def enable_auto_end_date(context):
    """
    Indicate that auto end-dating on effectivity satellites should be enabled
    """
    context.auto_end_date = True


@fixture
def enable_full_refresh(context):
    """
    Indicate that a full refresh for a dbt run should be executed
    """
    context.full_refresh = True


@fixture
def disable_union(context):
    """
    Indicate that a list should not be created if multiple stages are specified in a scenario
    """
    context.disable_union = True


@fixture
def disable_payload(context):
    """
    Indicate that a src_payload key should be removed from the provided metadata
    """
    context.disable_payload = True
