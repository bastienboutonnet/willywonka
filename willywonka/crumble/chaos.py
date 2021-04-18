"""Holds classes to create data chaos."""
# TODO:
# - null inserter
# - target a specific table on a database
# - targer a specific column on that table
# - insert nulls
# filtered where "something = foo"
# control the percentage of nulls interted over the partition.
from typing import Any, Mapping, Sequence

from sqlalchemy import MetaData, Table, and_
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

from willywonka.connectors.postgres_connector import PostgresConnector


class NullInserter:
    """Inserts Nulls."""

    def __init__(self, sql_engine: Engine) -> None:
        self._engine = sql_engine

    def update_table(
        self,
        target_schema: str,
        target_table: str,
        value_to_insert: int,
        payload: Sequence[Mapping[str, Mapping[str, Any]]],
    ) -> None:
        """Update a certain proportion of rows with nulls."""
        metadata = MetaData(bind=None, schema=target_schema)
        metadata.reflect(bind=self._engine, only=[target_table])
        table = Table(target_table, metadata, autoload=True, autoload_with=self._engine)

        Session = sessionmaker(bind=self._engine)
        session = Session()

        stmt = table.update().where(and_(func.random() > 0.5)).values({"weight": 0})

        session.execute(stmt)
        session.commit()


if __name__ == "__main__":
    connection_params = {
        "user": "willywonka_user",
        "password": "magical_password",
        "database": "willywonka_test",
        "port": 5432,
        "host": "localhost",
    }
    connector = PostgresConnector(connection_params=connection_params)
    eng = connector.engine
    inserter = NullInserter(eng)
    inserter.update_table("public", "people")
