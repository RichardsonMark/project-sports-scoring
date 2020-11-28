# project-sports-scoring

# Many to Many Zombies Lab

### Sports scoring
An app that lets a sports fan keep track of their favourite sports league.

## Set Up

First, you will need to ensure that you have a database called sports_scoring (if you've already done part of this and are starting from scratch, or have a db of the same name, first drop the db.)

```sh
createdb sports_scoring
```

Once the database exists, you'll need to run the SQL file against it to create the tables.

```sh
psql -d sports_scoring -f ./db/sports_scoring.sql
```
