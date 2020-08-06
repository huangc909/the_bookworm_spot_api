#!/bin/bash

curl "http://localhost:8000/books/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
