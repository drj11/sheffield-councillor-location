data/geom.geojson: data/joined
	bin/geojson.py

data/joined: data/addr.tsv data/latlon.tsv data/postcode-ward.tsv data/ward-points.tsv
	bin/join-the-things > data/joined

data/postcode-ward.tsv: data/latlon.tsv
	bin/ll-ward.py
