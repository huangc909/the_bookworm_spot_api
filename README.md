# The BookWorm Spot App
The BookWorm Spot app provides users a space to store their personal reading experience by being able to add books into the app, record a note for each book, and check off whether or not the book is on their wishlist and/or has been read already.

## Links
- API URL:
- Deployed Application:
- Front End Repository:

## ERD
![The_BookWorm_Spot_ERD](https://media.git.generalassemb.ly/user/28180/files/b339ba00-d703-11ea-8aa4-21365d86c34a)

## Technologies Used
- Django
- Python
- Postman
- cURL Scripts
- Heroku

## Planning


## API Information
### Books
| Verb   | URI Pattern  | Controller#Action  |
|:-------|:-------------|:-------------------|
| GET    | `/books/`     | `books#index`  |
| GET    | `/books/:id` | `books#show`   |
| POST   | `/books`     | `books#create` |
| PATCH  | `/books/:id` | `books#update` |
| DELETE | `/books/:id` | `books#destroy` |


### GET /books/
Example Curl Request:
```sh
#!/bin/bash

curl "http://localhost:8000/books/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo

```

Example Terminal Command:
```sh
TOKEN="e639034f2a1484820b684823da0e8993c49ebed0" sh curl-scripts/books/index.sh
```

Example API Response:
```md
Date: Thu, 06 Aug 2020 19:10:10 GMT
Server: WSGIServer/0.2 CPython/3.7.7
Content-Type: application/json
Vary: Accept, Origin
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 183
X-Content-Type-Options: nosniff

[{"id":8,"title":"Atomic Habits","author":"James Clear","note":"Started reading a few chapters","rating":"So far it's pretty interesting","onWishlist":false,"onRead":false,"owner":2}]
```

---
### GET /books/:id/
Example Curl Request:
```sh
#!/bin/bash

curl "http://localhost:8000/books/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
```

Example Terminal Command:
```sh
ID=8 TOKEN="e639034f2a1484820b684823da0e8993c49ebed0" sh curl-scripts/books/show.sh
```

Example API Response:
```md
HTTP/1.1 200 OK
Date: Thu, 06 Aug 2020 19:09:02 GMT
Server: WSGIServer/0.2 CPython/3.7.7
Content-Type: application/json
Vary: Accept, Origin
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 181
X-Content-Type-Options: nosniff

{"id":8,"title":"Atomic Habits","author":"James Clear","note":"Started reading a few chapters","rating":"So far it's pretty interesting","onWishlist":false,"onRead":false,"owner":2}
```

---
### POST /books/
Example Curl Request:

```sh
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
      "rating": "'"${RATING}"'",
      "onWishlist": "'"${WL}"'",
      "onRead": "'"${READ}"'"
    }
  }'

echo
```

Example Terminal Command:
```sh
TOKEN="e639034f2a1484820b684823da0e8993c49ebed0" TITLE="Atomic Habits" AUTHOR="James Clear" NOTE="Started reading a few chapters" RATING="Still pending" WL=false READ=false sh curl-scripts/books/create.sh
```

Example API Response:
```md
HTTP/1.1 201 Created
Date: Thu, 06 Aug 2020 19:03:33 GMT
Server: WSGIServer/0.2 CPython/3.7.7
Content-Type: application/json
Vary: Accept, Origin
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 164
X-Content-Type-Options: nosniff

{"id":8,"title":"Atomic Habits","author":"James Clear","note":"Started reading a few chapters","rating":"Still pending","onWishlist":false,"onRead":false,"owner":2}
```

---
### PATCH /books/:id/
Example Curl Request:
```sh
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
      "rating": "'"${RATING}"'",
      "onWishlist": "'"${WL}"'",
      "onRead": "'"${READ}"'"
    }
  }'

echo
```

Example Terminal Command:
```sh
ID=8 TOKEN="e639034f2a1484820b684823da0e8993c49ebed0" TITLE="Atomic Habits" AUTHOR="James Clear" NOTE="Started reading a few chapters" RATING="So far it's pretty interesting" WL=false READ=false sh curl-scripts/books/update.sh
```

Example API Response:
```md
HTTP/1.1 200 OK
Date: Thu, 06 Aug 2020 19:06:41 GMT
Server: WSGIServer/0.2 CPython/3.7.7
Content-Type: application/json
Vary: Accept, Origin
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 181
X-Content-Type-Options: nosniff

{"id":8,"title":"Atomic Habits","author":"James Clear","note":"Started reading a few chapters","rating":"So far it's pretty interesting","onWishlist":false,"onRead":false,"owner":2}
```

---
### DELETE /books/:id/
Example Curl Request:
```sh
#!/bin/bash

curl "http://localhost:8000/books/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
```

Example Terminal Command:
```sh
ID=8 TOKEN="e639034f2a1484820b684823da0e8993c49ebed0" sh curl-scripts/books/delete.sh
```

Example API Response:
```md
HTTP/1.1 204 No Content
Date: Thu, 06 Aug 2020 19:11:57 GMT
Server: WSGIServer/0.2 CPython/3.7.7
Vary: Accept, Origin
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 0
X-Content-Type-Options: nosniff
```
