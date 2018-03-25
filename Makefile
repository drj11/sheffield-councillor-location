data/geom.geojson: data/joined bin/geojson.py
	bin/geojson.py

data/joined: bin/join-the-things data/addr.tsv data/map-postcode-latlon.tsv data/map-postcode-ward.tsv data/map-ward-latlon.tsv
	bin/join-the-things > data/joined

data/map-postcode-ward.tsv: bin/map-postcode-ward.py data/map-postcode-latlon.tsv
	bin/map-postcode-ward.py

data/map-ward-latlon.tsv: bin/map-ward-latlon.py
	bin/map-ward-latlon.py
