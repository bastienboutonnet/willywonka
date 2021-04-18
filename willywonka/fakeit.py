"""Data faker module wrapping around Faker."""
import numpy as np
import pandas as pd
from faker import Faker

from willywonka.connectors.postgres_connector import PostgresConnector

fake = Faker()


def create_data(x):
    """Create data."""
    # dictionary
    people_data = {}
    for i in range(0, x):
        people_data[i] = {}
        people_data[i]["name"] = fake.name()
        people_data[i]["address"] = fake.address()
        people_data[i]["city"] = fake.city()
        people_data[i]["chocolate_bars"] = np.random.randint(0, 5)
        people_data[i]["weight"] = np.random.uniform(40.0, 100.0)

    return people_data


CONNECTION_DETAILS = {
    "host": "localhost",
    "user": "willywonka_user",
    "password": "magical_password",
    "database": "willywonka_test",
    "port": "5432",
}


def main():
    """Main."""
    people = create_data(1000)
    fake_data = pd.DataFrame.from_dict(people, orient="index")
    print(fake_data.head())
    connector = PostgresConnector(CONNECTION_DETAILS)
    fake_data.to_sql("people", connector.engine.connect(), if_exists="replace")


if __name__ == "__main__":
    main()
