import sqlparse

def are_dml_statements(statements):
    results = []
    
    for statement in statements:
        # Check if the last token of the last statement is a semicolon
        last_token = statement.tokens[-1] if statement.tokens else None
        has_semicolon = isinstance(last_token, sqlparse.sql.Token) and last_token.value == ';'
        results.append(not has_semicolon)
    
    return results

def detect_missing_semicolon(sql):
    # Split the SQL string into statements
    statements = sqlparse.split(sql)
    
    # Detect missing semicolons
    results = are_dml_statements(sqlparse.parse(sql))
    
    # Check if the first query is missing a semicolon
    first_query_missing_semicolon = results[0] if results else False
    
    return first_query_missing_semicolon

# Example usage
sql = "SELECT * FROM table1 UPDATE table2 SET column1 = value1; DELETE FROM table3"
is_missing_semicolon = detect_missing_semicolon(sql)

if is_missing_semicolon:
    print("The first query is missing a semicolon.")
else:
    print("The first query either ends with a semicolon or is not a DML statement.")
