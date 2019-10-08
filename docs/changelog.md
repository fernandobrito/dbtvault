# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.2.3-pre] - 2019-10-08

### Macros

- Updated [hash](macros.md#hash) and [multi-hash](macros.md#multi_hash)
    - [hash](macros.md#hash) now accepts a third parameter, ```sort```
    which will alpha-sort provided columns when set to true.
    - [multi-hash](macros.md#multi_hash) updated to take advantage of
    the the [hash](macros.md#hash) functionality.

### Documentation

- Updated [hash](macros.md#hash) and [multi-hash](macros.md#multi_hash) according to new changes.

## [v0.2.2-pre]  - 2019-10-08

### Documentation

- Finished Satellite page
- Added Union sections to Hub and Link pages
- Updated staging page with Satellite fields
- Renamed ```stg_orders_hashed``` back to ```stg_customers_hashed```

## [v0.2.1-pre] - 2019-10-07

### Documentation

- Minor additions and corrections to documentation:
    - Fixed website URL in footer
    - Added contribution page to docs
    - Corrected version in dbt_project.yml

## [v0.2-pre] - 2019-10-07

[Feedback is welcome!](https://github.com/Datavault-UK/dbtvault/issues)
 
### Improved
Read the linked documentation for more detail on how to take advantage of
the new and improved features.

- Table Macros:
    - All table macros now no longer require the ```tgt_cols``` parameter.
    This was unnecessary duplication of metadata and removing this now makes
    creating tables much simpler.
    
- Supporting Macros:
    - [add_columns](macros.md#add_columns)
        - Simplified the process of adding constants.
        - Can now optionally provide a [dbt source](https://docs.getdbt.com/docs/using-sources) to automatically
        retrieve all source columns without needing to type them all manually.
        - If not adding any calculated columns or constants, column pairs can be omitted, enabling you to provide the 
        source parameter above only.
    - [hash](macros.md#hash) now alpha-sorts columns prior to hashing, as
    per best practises. 
   
- Staging Macros:
    - staging_footer renamed to [from](macros.md#from) and functionality for adding constants moved to
    [add_columns](macros.md#add_columns)
    - [multi-hash](macros.md#multi_hash)
        - Formatting of output now more readable
        - Now alpha-sorts columns prior to hashing, as
          per best practises. 

## [v0.1-pre] - 2019-09 / 2019-10
### Added

- Table Macros:
    - [Hub](macros.md#hub_template)
    - [Link](macros.md#link_template)
    - [Satellite](macros.md#sat_template)

- Supporting Macros:
    - [cast](macros.md#cast)
    - [hash](macros.md#hash) (renamed from md5_binary)
    - [prefix](macros.md#prefix)

- Staging Macros:
    - [add_columns](macros.md#add_columns)
    - [multi_hash](macros.md#multi_hash) (renamed from gen_hashing)
    - [staging_footer](macros.md#staging_footer) 

### Documentation
   
- Numerous changes leading up to Version 1.0 release