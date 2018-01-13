import subprocess
import pandas as pd


PREFIX = "sdh"
DATABASE = "blaze"
for query in ["vavenum", "tempsensor", "ahuchildren", "spatialmapping", "sensorsinrooms", "greybox"]:
    df = pd.DataFrame()
    for db in ["hoddb","allegro","blaze", "virtuoso", "rdflib"]:
        cmd = "./rdfrun -q {0} -db {2} | tee {2}_{1}_{0}.csv".format(query, PREFIX, db)
        print(cmd)
        out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
        outdata = [int(x) / 1e6 for x in out.stdout.decode().split('\n')[:-1]]
        df[db] = outdata
    print(df.describe())
