# ai-pdf-query

Application to search pdfs via a HTTP REST interface

## Install

This app uses docker. To run the application:

```sh
docker compose up --build
```

## Endpoints

| Method | Url                   | Description                                    |
| ------ | --------------------- | ---------------------------------------------- |
| `GET`  | `query/:query_string` | Responds to your query with the pdf as context |
