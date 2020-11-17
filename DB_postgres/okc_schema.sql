---All code to be executed in PostgreSQL

---Tables
CREATE TABLE "Bots"( 
    email        varchar(250),
    user_name     varchar(50) NOT NULL,
    password     varchar(100) NOT NULL,
    phone_number varchar(20) NOT NULL,
    first_name   varchar(100) NOT NULL,
    last_name    varchar(100) NOT NULL,
    PRIMARY KEY (email) );

-- Constraints