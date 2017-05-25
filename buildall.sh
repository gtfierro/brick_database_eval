for i in alegrograph blazegraph rdf3x rdflib hod fuseki ; do
    echo $i
    cd $i
    ./build.sh
    cd -
done
