import configparser
import psycopg2
from sql_setup_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

    print("drop done")

def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
    print("create done")
def main():

    config = configparser.ConfigParser()
    config.read('dag_setup_config.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}"\
            .format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
