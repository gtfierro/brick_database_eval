import sys
import pandas as pd
from matplotlib import pyplot as plt
from rdfrun import *
from benchmark_queries import *
import time
prefix = sys.argv[1] if len(sys.argv) > 1 else ''

init = False
NUM_RUNS = 200
TIME_BTWN = .5

def start():
    init = True
    hod = HodDB(init=init)
    rdf3x = RDF3X(init=init)
    rdflib = RDFlib(init=init)
    fuseki = Fuseki(init=init)
    allegro = AlegroGraph(init=init)
    blaze = BlazeGraph(init=init)
    init=False
    time.sleep(30)

hod = HodDB(init=init)
rdf3x = RDF3X(init=init)
rdflib = RDFlib(init=init)
fuseki = Fuseki(init=init)
allegro = AlegroGraph(init=init)
blaze = BlazeGraph(init=init)


def do_runs(db, query, num=NUM_RUNS):
    runs = []
    for i in range(num):
        t1 = time.time()*1000
        resp = db.query(query)
        t2 = time.time()*1000
        if resp is None: break
        runs.append(t2-t1)
        time.sleep(TIME_BTWN)
    return runs    
def overlap_hist(df):
    plt.clf()
    bins = pd.np.linspace(0, df.max().max(), 100)
    for col in df.columns:
        plt.hist(df[col], alpha=0.5, label=col)
    plt.legend(loc='upper right')
    plt.show()
def overlap_cdf(df,title=''):
    plt.clf()
    plt.figure()
    for col in df.columns:
        #plt.hist(df[col], alpha=0.5, label=col)
        ax = df[col].hist(cumulative=True, normed=1, bins=100, histtype='step',label=col)
        #x.set_label(col)
    plt.legend(loc='lower right')
    ax.get_figure().set_dpi(200)
    plt.xlabel("Latency (ms)")
    plt.ylabel("Portion of requests")
    plt.title(title)

# VAV Enum
start()
print("##### VAV ENUM #####")
q = benchqueries['VAVEnum']
print("Run Hod")
hod_data= do_runs(hod, q['hod'])
print("Run RDF3X")
rdf3x_data = do_runs(rdf3x, q['sparql'])
print("Run RDFLib")
rdflib_data = do_runs(rdflib, q['sparql'])
print("Run Fuseki")
fuseki_data = do_runs(fuseki, q['sparql'])
print("Run Allegro")
allegro_data = do_runs(allegro, q['sparql'])
print("Run Blaze")
blaze_data = do_runs(blaze, q['sparql'])

vavdf = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data})
print(vavdf.describe())
vavdf.to_csv(prefix+'vavenum.csv',index=False,header=True)


# Temp Sensor
start()
print("##### Temp Sensor #####")
q = benchqueries['TempSensor']
print("Run Hod")
hod_data= do_runs(hod, q['hod'])
print("Run RDF3X")
rdf3x_data = do_runs(rdf3x, q['sparql'])
print("Run RDFLib")
rdflib_data = do_runs(rdflib, q['sparql'])
print("Run Fuseki")
fuseki_data = do_runs(fuseki, q['sparql'])
print("Run Allegro")
allegro_data = do_runs(allegro, q['sparql'])
print("Run Blaze")
blaze_data = do_runs(blaze, q['sparql'])

tempsensedf = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data})
print(tempsensedf.describe())
tempsensedf.to_csv(prefix+'tempsense.csv',index=False,header=True)

# AHU Children
start()
print("##### AHU Children #####")
q = benchqueries['AHUChildren']
print("Run Hod")
hod_data= do_runs(hod, q['hod'])
print("Run RDF3X")
rdf3x_data = do_runs(rdf3x, q['sparql'])
print("Run RDFLib")
rdflib_data = do_runs(rdflib, q['sparql'])
print("Run Fuseki")
fuseki_data = do_runs(fuseki, q['sparql'])
print("Run Allegro")
allegro_data = do_runs(allegro, q['sparql'])
print("Run Blaze")
blaze_data = do_runs(blaze, q['sparql'])

ahuchildren = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data})
print(ahuchildren.describe())
ahuchildren.to_csv(prefix+'ahuchildren.csv',index=False,header=True)

# Spatial Mapping
start()
print("##### Spatial Mapping #####")
q = benchqueries['SpatialMapping']
print("Run Hod")
hod_data= do_runs(hod, q['hod'])
print("Run RDF3X")
rdf3x_data = do_runs(rdf3x, q['sparql'])
print("Run RDFLib")
rdflib_data = do_runs(rdflib, q['sparql'])
print("Run Fuseki")
fuseki_data = do_runs(fuseki, q['sparql'])
print("Run Allegro")
allegro_data = do_runs(allegro, q['sparql'])
print("Run Blaze")
blaze_data = do_runs(blaze, q['sparql'])

spatialmapping = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data})
print(spatialmapping.describe())
spatialmapping.to_csv(prefix+'spatialmapping.csv',index=False,header=True)

# Sensors in Rooms
start()
print("##### Sensors in Rooms #####")
q = benchqueries['SensorsInRooms']
print("Run Hod")
hod_data= do_runs(hod, q['hod'])
print("Run RDF3X")
rdf3x_data = do_runs(rdf3x, q['sparql'])
print("Run RDFLib")
rdflib_data = do_runs(rdflib, q['sparql'])
print("Run Fuseki")
fuseki_data = do_runs(fuseki, q['sparql'])
print("Run Allegro")
allegro_data = do_runs(allegro, q['sparql'])
print("Run Blaze")
blaze_data = do_runs(blaze, q['sparql'])

sensorsinrooms = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data})
print(sensorsinrooms.describe())
sensorsinrooms.to_csv(prefix+'sensorsinrooms.csv',index=False,header=True)

# VAV Relships
start()
print("##### VAV relships #####")
q = benchqueries['VAVRelships']
print("Run Hod")
hod_data= do_runs(hod, q['hod'])
print("Run RDF3X")
rdf3x_data = do_runs(rdf3x, q['sparql'])
print("Run RDFLib")
rdflib_data = do_runs(rdflib, q['sparql'])
print("Run Fuseki")
fuseki_data = do_runs(fuseki, q['sparql'])
print("Run Allegro")
allegro_data = do_runs(allegro, q['sparql'])
print("Run Blaze")
blaze_data = do_runs(blaze, q['sparql'])

vavrelships = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data})
print(vavrelships.describe())
vavrelships.to_csv(prefix+'vavrelships.csv',index=False,header=True)

# GreyBox
start()
print("##### Grey Box #####")
q = benchqueries['GreyBox']
print("Run Hod")
hod_data= do_runs(hod, q['hod'])
print("Run RDF3X")
rdf3x_data = do_runs(rdf3x, q['sparql'])
print("Run RDFLib")
rdflib_data = do_runs(rdflib, q['sparql'])
print("Run Fuseki")
fuseki_data = do_runs(fuseki, q['sparql'])
print("Run Allegro")
allegro_data = do_runs(allegro, q['sparql'])
print("Run Blaze")
blaze_data = do_runs(blaze, q['sparql'])

greybox = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data})
print(greybox.describe())
greybox.to_csv(prefix+'greybox.csv',index=False,header=True)
