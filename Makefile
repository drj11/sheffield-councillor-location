2018-data/geom.geojson: bin/geojson.py 2018-data/joined 2018-data/map-subject-distance.tsv
	bin/geojson.py 2018-data/joined

2018-data/map-subject-distance.tsv: bin/map-subject-distance.py 2018-data/subject.tsv data/map-postcode-latlon.tsv
	bin/map-subject-distance.py 2018-data/subject.tsv

data/geom.geojson: bin/geojson.py data/joined data/map-subject-distance.tsv
	bin/geojson.py data/joined

2018-data/joined: bin/join-the-things 2018-data/subject.tsv data/map-postcode-latlon.tsv data/map-postcode-ward.tsv data/map-ward-latlon.tsv
	bin/join-the-things 2018-data/subject.tsv > 2018-data/joined

data/joined: bin/join-the-things data/subject.tsv data/map-postcode-latlon.tsv data/map-postcode-ward.tsv data/map-ward-latlon.tsv
	bin/join-the-things > data/joined

data/map-postcode-ward.tsv: bin/map-postcode-ward.py data/map-postcode-latlon.tsv
	bin/map-postcode-ward.py

data/map-ward-latlon.tsv: bin/map-ward-latlon.py
	bin/map-ward-latlon.py
