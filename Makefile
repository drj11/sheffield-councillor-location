data/geom.geojson: data/joined bin/geojson.py
	bin/geojson.py

data/joined: data/addr.tsv data/map-postcode-latlon.tsv data/map-postcode-ward.tsv data/ward-points.tsv
	bin/join-the-things > data/joined

data/map-postcode-ward.tsv: bin/map-postcode-ward.py data/map-postcode-latlon.tsv
	bin/map-postcode-ward.py

data/ward-points.tsv: bin/centroid-ward.py
	bin/centroid-ward.py
