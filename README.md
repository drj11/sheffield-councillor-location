# Sheffield councillor location data

## Sources

Councillors are taken from Sheffield City Council's web pages.

Their names, party affiliations, and postcodes
are taken from the
2016 SOPN (Statement of Persons Nominated),
and other SOPNs for by-elections.
I used the SOPN that someone had helpfully uploaded to Democracy Club:
https://candidates.democracyclub.org.uk/media/official_documents/MTW%3AE05010879/statement-of-persons-nominated.pdf

Manual step: Postcodes are converted to lat / long using
https://gridreferencefinder.com/postcodeBatchConverter/ .

Ward boundaries are from MapIt, https://mapit.mysociety.org/ .

## Data correction

Data has not been extensively qualified or assured.

Noted and corrected data errors:

1 candidate for Shiregreen & Brightside ward
lists their postcode as `S35 8GN`,
but that does not seem to be a valid postcode;
corrected to `S35 8NG`.
