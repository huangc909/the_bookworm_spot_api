#!/bin/bash

curl "http://localhost:8000/all-books/" \
  --include \
  --request GET \
  --header "Content-Type: application/json" \

echo
