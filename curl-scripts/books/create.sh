#!/bin/bash

curl "http://localhost:8000/books/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "book": {
      "title": "'"${TITLE}"'",
      "author": "'"${AUTHOR}"'",
      "note": "'"${NOTE}"'",
      "onWishlist": "'"${WL}"'",
      "onRead": "'"${READ}"'"
    }
  }'

echo
