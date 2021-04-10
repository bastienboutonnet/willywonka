"""Data faker module wrapping around Faker."""
import pandas as pd
from faker import Faker
import numpy as np
from willywonka.connectors.postgres_connector import PostgresConnector

fake = Faker()


def create_data(x):

    # dictionary
    friends_data = {}
    for i in range(0, x):
        friends_data[i] = {}
        friends_data[i]["name"] = fake.name()
        friends_data[i]["address"] = fake.address()
        friends_data[i]["city"] = fake.city()
        friends_data[i]["chocolate_bars"] = np.random.randint(0, 5)
        friends_data[i]["closeness (1-5)"] = np.random.randint(0, 5)

    return friends_data


CONNECTION_DETAILS = {
    "host": "localhost",
    "user": "willywonka_user",
    "password": "magical_password",
    "database": "willywonka_test",
    "port": "5432",
}


def main():
    friends = create_data(1000)
    fake_data = pd.DataFrame.from_dict(friends, orient="index")
    print(fake_data)
    connector = PostgresConnector(CONNECTION_DETAILS)
    fake_data.to_sql("friends", connector.engine.connect(), if_exists="replace")


if __name__ == "__main__":
    main()
