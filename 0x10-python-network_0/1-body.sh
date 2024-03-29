#!/bin/bash
# This script takes a URL, sends a GET request to the URL and displays a 200 status code response
curl -s "$1" -X GET -L
