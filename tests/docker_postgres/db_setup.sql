CREATE TABLE test (id serial PRIMARY KEY, answer integer, question varchar);

INSERT INTO test VALUES
    (1, 11, 'how high does it go?'),
    (2, 42, 'what is the meaning of life?')
    ;

CREATE TABLE answers (id serial PRIMARY KEY, answer integer, question varchar);

INSERT INTO my_first_dbt_model VALUES
    (1, 11, 'how high does it go?'),
    (2, 42, 'what is the meaning of life?'),
    (3, 12, 'how high does it go?')
    ;
