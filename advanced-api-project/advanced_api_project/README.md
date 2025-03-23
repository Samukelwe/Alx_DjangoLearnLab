# API Views Documentation

## Book Views

### BookListView
- Description: This view lists all the books available in the database.
- Endpoint: `/books/`
- Method: GET
- Permissions: Allows read-only access to unauthenticated users.
- Custom Settings: Uses IsAuthenticatedOrReadOnly permission class.

### BookDetailView
- Description: This view retrieves details of a single book based on the provided ID.
- Endpoint: `/books/<id>/`
- Method: GET
- Permissions: Allows read-only access to unauthenticated users.
- Custom Settings: Uses IsAuthenticatedOrReadOnly permission class.

... (Add similar documentation for other views)

## Custom Settings
- Include any additional custom settings, permissions, or hooks used in the views here.