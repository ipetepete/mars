#!/bin/bash
# Test a thread-thru-the-system.
# Successful ingest:
# 1. rsync file to mtn dropbox from mock DOME
# 2. post initial audit record from mock DOME
# 3. mtn: compress, update audit, rsync to valley DATAQ
# 4. valley: pop DATAQ, ingest via NATICA webservice
# 5. do natica/search (mock portal) to find ingested file

