#!/bin/bash

curl "http://localhost:8000/books/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
