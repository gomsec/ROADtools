#!/usr/bin/env python3

import sys
import os

# Add the roadlib directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'roadlib'))

from roadtools.roadlib.constants import WELLKNOWN_RESOURCES
from roadtools.roadlib.auth import Authentication

def test_aliases():
    print("Testing Microsoft Graph aliases:")
    print()
    
    # Test the aliases
    aliases_to_test = ['msgraph', 'msgraph-us', 'msgraph-com']
    
    for alias in aliases_to_test:
        if alias in WELLKNOWN_RESOURCES:
            url = WELLKNOWN_RESOURCES[alias]
            print(f"{alias:<12} -> {url}")
        else:
            print(f"{alias:<12} -> NOT FOUND")
    
    print()
    print("Testing lookup_resource_uri method:")
    
    auth = Authentication()
    for alias in aliases_to_test:
        resolved = auth.lookup_resource_uri(alias)
        print(f"{alias:<12} -> {resolved}")
    
    print()
    print("All aliases in WELLKNOWN_RESOURCES:")
    for alias, url in WELLKNOWN_RESOURCES.items():
        print(f"{alias:<12} -> {url}")

if __name__ == "__main__":
    test_aliases()