# Blog API with JWT Authentication

This is a backend blog application built using Django Rest Framework (DRF) and JWT (JSON Web Token) authentication. The app allows users to add, edit, modify, and view blogs. It is designed for API-only interaction and does not include a frontend.

## Features

- **User authentication**: Secure user login with JWT token authentication.
- **CRUD operations** for blogs:
  - Add new blogs
  - Edit existing blogs
  - Modify blogs
  - Delete blogs
  - Search for blogs
- Pagination and search functionality for blogs.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django Rest Framework
- djangorestframework-simplejwt

## API Endpoint
  - `GET /api/blogs/`: Get all blogs (supports pagination and search).
  - `POST /api/blogs/`: Create a new blog (requires authentication).
  - `PATCH /api/blogs/`: Update an existing blog (requires authentication).
  - `DELETE /api/blogs/`: Delete a blog (requires authentication).

## Authentication

JWT token authentication is used in this application. To access protected endpoints, you need to provide the JWT token in the `Authorization` header.

