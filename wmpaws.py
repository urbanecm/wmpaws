import os
import pymysql
import pandas as pd
import requests

def connect(dbname: str, cluster: str = 'analytics') -> pymysql.connections.Connection:
    if cluster not in ['analytics', 'web']:
        raise ValueError('"cluster" must be one of: "analytics", "web"')

    if dbname.endswith('_p'):
        dbname = dbname[:-2]
    return pymysql.connect(
        host="{dbname}.{cluster}.db.svc.wikimedia.cloud".format(dbname=dbname, cluster=cluster),
        read_default_file=os.path.expanduser("~/.my.cnf"),
        database="{dbname}_p".format(dbname=dbname),
        charset='utf8'
    )

def run_sql(query: str, connection: pymysql.connections.Connection):
    df = pd.read_sql_query(query, connection)
    for x in df:
        df[x] = df[x].apply(lambda y: y.decode('utf-8') if isinstance(y, bytes) else y)
    return df

def get_dblist(dblist):
    r = requests.get('https://noc.wikimedia.org/conf/dblists/{dblist}.dblist'.format(dblist=dblist))
    res = r.content.decode('utf-8').split('\n')
    res.pop(0)
    res.pop()
    return res
