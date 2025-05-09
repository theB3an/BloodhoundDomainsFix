# Bloodhound Domains File Fix

If using the Kali included version of `bloodhound-python` the "TrustType" and "TrustDirection" mappings use an int value instead of string and must be converted to properly ingest into Bloodhound CE.


If an output file is not specified, the original will be overwritten with the updates:
`python ../FixBloodhoundDomains.py 20250509125232_domains.json` 
OR
`python ../FixBloodhoundDomains.py 20250509125232_domains.json new_domains.json`
