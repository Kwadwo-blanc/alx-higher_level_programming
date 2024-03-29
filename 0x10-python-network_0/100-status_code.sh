#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response
curl -s -o /tmp/response.txt -w "%{http_code}" "$1" && cat /tmp/response.txt
