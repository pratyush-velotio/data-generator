# ITERATIONS

### Iteration 1

1. App should support generation of 3 types of files:
   * CSV 
   * Parquet
   * JSON

2. The app should take configuration from user such as file format, number of records, name of the file (or anything deemed necessary), column data type.

3. The app should have data validation based on data type. For example, if a user wants to generate an id field with int data type, then the app should not generate a string on id field.

### Iteration 2

1. Modularize the code (Object Oriented)

2. Additional config
   * More properties added to the config - User can opt for sensible names, unique ids etc
   * Strongly modelled config - (Pydantic)

3. *OPTIONAL FOR THIS ITERATION* Inclusion of data structures(dict, list) as column types 
