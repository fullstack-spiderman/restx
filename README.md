# RESTX

[![CI](https://github.com/fullstack-spiderman/restx/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/fullstack-spiderman/restx/actions/workflows/ci.yml) [![CD](https://github.com/fullstack-spiderman/restx/actions/workflows/cd.yml/badge.svg?event=pull_request)](https://github.com/fullstack-spiderman/restx/actions/workflows/cd.yml) ![PyPI - Downloads](https://img.shields.io/pypi/dm/restx)
![GitHub Issues](https://img.shields.io/github/issues/fullstack-spiderman/restx) ![Last Commit](https://img.shields.io/github/last-commit/fullstack-spiderman/restx) ![Contributors](https://img.shields.io/github/contributors/fullstack-spiderman/restx)
![Code Size](https://img.shields.io/github/languages/code-size/fullstack-spiderman/restx) ![Version](https://img.shields.io/github/v/release/fullstack-spiderman/restx) ![License](https://img.shields.io/github/license/fullstack-spiderman/restx)

<!-- ![Code Coverage](https://codecov.io/gh/fullstack-spiderman/restx/branch/main/graph/badge.svg) -->

## Description

A Python CLI application for sending HTTP requests using different methods (GET, POST, PUT, PATCH, DELETE).

### Installation

#### Using pip

```bash
pip install restx
```

#### Or using poetry

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
restx post <url_with_endpoint> --payload '<json payload>'
# Example: restx post "https://jsonplaceholder.typicode.com/posts" --payload '{"userId": 12, "title": "test doc body"}'
```

##### HTTP PUT (Update a Record)

```bash
restx put <url_with_endpoint> --payload '<json payload>'
# Example: restx put "https://jsonplaceholder.typicode.com/posts" --payload '{"userId": 12, "title": "test doc body"}'
```

##### HTTP PATCH (Partial Update a Record)

```bash
restx patch <url_with_endpoint> --payload '<json payload>'
# Example: restx patch "https://jsonplaceholder.typicode.com/posts" --payload '{"title": "test doc body"}'
```

##### HTTP DELETE (Delete a Record)

```bash
restx delete <url_with_endpoint> --payload '<json payload>'
# Example: restx delete "https://jsonplaceholder.typicode.com/posts/23"
```

##### To provide custom Headers

```bash
restx <command> <url> --header '<json header>'
# Example:
# restx post https://jsonplaceholder.typicode.com/posts --payload '{"userId": 1, "id": 1, "title": "sunt aut facere, "body": "recusandae consequuntur expedita et"}' --header '{"Content-Type": "application/json"}'
```

##### For help

```bash
restx --help
restx <get|post|put|patch|delete> --help
```

#### Contributions

Contributions are welcome! Please follow these guidelines:

- Submit bug reports or feature requests through the issue tracker.
- Set up a development environment by cloning the repository and installing dependencies.

#### License

This project is licensed under the MIT. See the LICENSE file for details.
