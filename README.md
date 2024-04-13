## RESTX

[![CI/CD](https://github.com/fullstack-spiderman/restx/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/fullstack-spiderman/restx/actions/workflows/ci.yml)

#### Description

A Python CLI application for sending HTTP requests using different methods (GET, POST, PUT, PATCH, DELETE).

#### Installation

##### Using pip

```bash
pip install restx
```

##### Or using poetry

```bash
poetry add restx
```

#### Usage

##### HTTP GET (All Records)

```bash
restx get <url_with_endpoint>
# Example: restx get https://jsonplaceholder.typicode.com/posts/
```

##### HTTP GET (Read Single Record)

```bash
restx get <url_with_endpoint>
# Example: restx get https://jsonplaceholder.typicode.com/posts/54
```

##### HTTP POST (Create a Record)

```bash
restx post <url_with_endpoint> --payload '<payload json>'
# Example: restx post "https://jsonplaceholder.typicode.com/posts" --payload '{"userId": 12, "title": "test doc body"}'
```

##### HTTP PUT (Update a Record)

```bash
restx put <url_with_endpoint> --payload '<payload json>'
# Example: restx put "https://jsonplaceholder.typicode.com/posts" --payload '{"userId": 12, "title": "test doc body"}'
```

##### HTTP PATCH (Partial Update a Record)

```bash
restx patch <url_with_endpoint> --payload '<payload json>'
# Example: restx patch "https://jsonplaceholder.typicode.com/posts" --payload '{"title": "test doc body"}'
```

##### HTTP DELETE (Delete a Record)

```bash
restx delete <url_with_endpoint> --payload '<payload json>'
# Example: restx delete "https://jsonplaceholder.typicode.com/posts/23"
```

#### Contributions

Contributions are welcome! Please follow these guidelines:

- Submit bug reports or feature requests through the issue tracker.
- Set up a development environment by cloning the repository and installing dependencies.

#### License

This project is licensed under the MIT. See the LICENSE file for details.
