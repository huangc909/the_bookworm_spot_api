#!/bin/bash

curl "http://localhost:8000/books/${ID}/" \
  --include \
  --request PATCH \
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
