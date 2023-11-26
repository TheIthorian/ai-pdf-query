# ai-pdf-query

Application to search pdfs via a HTTP REST interface

## Install

This app uses docker. To run the application:

```sh
docker compose up --build
```

## Api Keys

Set the `OPENAI_API_KEY` (from openAI dev portal) and the `APP_KEY` (generated and set by you) in `.docker.env`

## Endpoints

| Method | Url                  | Description                                    |
| ------ | -------------------- | ---------------------------------------------- |
| `GET`  | `query/:query_input` | Responds to your query with the pdf as context |
