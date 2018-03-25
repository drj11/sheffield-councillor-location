# Sheffield councillor location data

## Data files

There are two data sources:
`data/subject.tsv` (manual input) and a ward geometry file.

The final output file is `data/geom.geojson`.

Data files named `map-_key_-_value_.tsv` are a (TSV file)
mapping from _key_ to _value_,
and are produced by the script `bin/map-_key_-_value_.py`.
For example `data/map-postcode-ward.tsv` is a file that
contains mappings from postcodes to the wards containing them.

### `data/subject.tsv`

Councillors are taken from Sheffield City Council's web pages.

Councillor names, party affiliations, and postcodes
are taken from the
2016 SOPN (Statement of Persons Nominated),
and other SOPNs for by-elections.
I used the SOPN that someone had helpfully uploaded to Democracy Club:
https://candidates.democracyclub.org.uk/media/official_documents/MTW%3AE05010879/statement-of-persons-nominated.pdf

### Wards

Ward boundaries are from MapIt, https://mapit.mysociety.org/ .

### `data/map-postcode-latlon.tsv`

Manual step: Postcodes are converted to latitude/longitude using
https://gridreferencefinder.com/postcodeBatchConverter/ .

## Data correction

Data has not been extensively qualified or assured.

Noted and corrected data errors:

1 candidate for Shiregreen & Brightside ward
lists their postcode as `S35 8GN`,
but that does not seem to be a valid postcode;
corrected to `S35 8NG`.
