### Check Current Configs
`current_region()`  
`current_role()`

### Use Right Roles
`use role sysadmin;`  
`use warehouse COMPUTE_WH;`  
`use database demo_db;`  
`use schema public;`  

### 1NF Functions
LATERAL, FLATTEN & SPLIT  
`LATERAL FLATTEN(INPUT => SPLIT(table.column, ',')) alias;`
TRIM  
`TRIM(alias.value)`
