#!/bin/bash

curl -H "User-Agent: jqb sample on `hostname`" https://api.magicthegathering.io/v1/cards | jq "`python builder.py`"
