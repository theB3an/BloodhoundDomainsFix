# Bloodhound Domains File Fix

If using the Kali included version of `bloodhound-python` the "TrustType" and "TrustDirection" mappings use an int value instead of string and must be converted to properly ingest into Bloodhound CE.
