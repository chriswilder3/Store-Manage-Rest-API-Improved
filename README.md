# Store Manager REST API V2.O

This project is a RESTful API built with Flask to manage stores and items. It is an improved version of the previous one. It provides endpoints for CRUD operations on stores and items, allowing users to view, add, and retrieve specific stores and items by unique identifiers. The API uses `uuid` to generate unique IDs for stores and items, making it suitable for educational or prototyping purposes.

## Features

- **Stores Management**:
  - `GET /store`: Retrieve all stores.
  - `POST /store`: Create a new store with a unique ID.
  - `GET /store/<store_id>`: Retrieve details of a specific store by ID.

- **Items Management**:
  - `GET /item`: Retrieve all items.
  - `POST /item`: Add a new item to a store, identified by its store ID.
  - `GET /item/<item_id>`: Retrieve details of a specific item by ID.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/store-manager-rest-api.git
   ```
