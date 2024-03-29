#!/bin/bash
# This script sends a GET request to the URL passed as an argument with X-School-User-Id header set to 98 and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
