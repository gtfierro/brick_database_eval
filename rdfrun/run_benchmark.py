import sys
import pandas as pd
import requests
from matplotlib import pyplot as plt
from rdfrun import *
from benchmark_queries import *
import time
prefix = sys.argv[1] if len(sys.argv) > 1 else ''

#name = "2"

init = False
NUM_RUNS = 200
TIME_BTWN = .2

def start():
    init = True
    hod = HodDB(init=init)
    rdf3x = RDF3X(init=init)
    rdflib = RDFlib(init=init)
    fuseki = Fuseki(init=init)
    allegro = AlegroGraph(init=init)
    blaze = BlazeGraph(init=init)
    virt = Virtuoso(init=init)
    init=False
    time.sleep(30)

hod = HodDB(init=init)
rdf3x = RDF3X(init=init)
rdflib = RDFlib(init=init)
fuseki = Fuseki(init=init)
allegro = AlegroGraph(init=init)
blaze = BlazeGraph(init=init)
virt = Virtuoso(init=init)


def do_runs(db, query, num=NUM_RUNS):
    runs = []
    for i in range(num):
        t1 = time.time()*1000
        try:
            resp = db.query(query)
        except requests.exceptions.Timeout:
            return [300000]*num
        except Exception as e:
            print(e)
            return [300000]*num
        else:
            t2 = time.time()*1000
            if resp is None: break
            if (t2-t1) > 300000: # 5 min
                return [300000]*num
            runs.append(t2-t1)
            time.sleep(TIME_BTWN)
    #print(len(resp))
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

if __name__ == '__main__':
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
    print("Run Virtuoso")
    virt_data = do_runs(virt, q['sparql'])

    vavdf = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data,'virtuoso': virt_data})
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
    print("Run Virtuoso")
    virt_data = do_runs(virt, q['sparql'])

    tempsensedf = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data,'virtuoso': virt_data})
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
    print("Run Virtuoso")
    virt_data = do_runs(virt, q['sparql'])

    ahuchildren = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data,'virtuoso': virt_data})
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
    print("Run Virtuoso")
    virt_data = do_runs(virt, q['sparql'])

    spatialmapping = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data,'virtuoso': virt_data})
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
    rdflib_data = [300000]*NUM_RUNS#do_runs(rdflib, q['sparql'])
    print("Run Fuseki")
    #fuseki_data = do_runs(fuseki, q['sparql'])
    fuseki_data = [300000]*NUM_RUNS#do_runs(rdflib, q['sparql'])
    print("Run Allegro")
    allegro_data = do_runs(allegro, q['sparql'])
    print("Run Blaze")
    blaze_data = do_runs(blaze, q['sparql'])
    print("Run Virtuoso")
    virt_data = do_runs(virt, q['sparql'])

    sensorsinrooms = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data,'virtuoso': virt_data})
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
    print("Run Virtuoso")
    virt_data = do_runs(virt, q['sparql'])

    vavrelships = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data,'virtuoso': virt_data})
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
    rdflib_data = [300000]*NUM_RUNS#do_runs(rdflib, q['sparql'])
    print("Run Fuseki")
    fuseki_data = do_runs(fuseki, q['sparql'])
    print("Run Allegro")
    allegro_data = do_runs(allegro, q['sparql'])
    print("Run Blaze")
    blaze_data = do_runs(blaze, q['sparql'])
    print("Run Virtuoso")
    virt_data = do_runs(virt, q['sparql'])

    greybox = pd.DataFrame.from_records({'hod':hod_data,'rdf3x':rdf3x_data, 'rdflib':rdflib_data,'allegro':allegro_data,'blaze':blaze_data,'fuseki':fuseki_data,'virtuoso': virt_data})
    print(greybox.describe())
    greybox.to_csv(prefix+'greybox.csv',index=False,header=True)
