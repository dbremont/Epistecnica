---
tags: [computer-network, distributed-system]
---

# (REST) Representational State Transfer


> An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other and exchange data.
> 

> A **Representational State Transfer (REST)** API is a set of architectural principles and constraints for designing and interacting with web services that use standard **HTTP** methods and data representations to perform **CRUD** operations on resources.
> 

## Source Organization Model

When managing API versioning in source code, you can adopt several organization models to structure and maintain different versions of your APIs. Here are a few standard models:

1. **Separate Folders for Each Version:** Organize your source code into individual folders for each API version (e.g., `/v1`, `/v2`), each containing the necessary code and configurations specific to that version.
2. **Branches for Versioning:** Create different branches in your version control system (e.g., Git) for each API version, allowing you to isolate changes and merge updates separately.
3. **Namespace Prefixing:** Use namespaces to distinguish between different versions of your API’s code. Prefix classes, methods, and modules with version indicators (e.g., `V1.UsersController`, `V2.OrdersController`).
4. **Folder Structure and Feature Flags:** Organize your code into a single set of folders, and use feature flags or conditional statements to enable or disable specific version-specific code paths.
5. **API Versioning Attributes/Annotations:** Use attributes, annotations, or decorators within your code to mark and differentiate different versions of API controllers or methods (e.g., `[ApiVersion("1.0")]`).
6. **Version as a Package:** Treat each API version as a separate package or module within your project, allowing you to manage versions independently.
7. **API Gateway or Proxy:** Use an API gateway or proxy server to manage API versions externally, allowing you to route incoming requests to the appropriate backend service based on version headers or URLs.
8. **Semantic Versioning:** Follow semantic versioning (e.g., `1.0.0`, `1.1.0`) for your APIs and libraries, and manage changes to the API’s interface (major, minor, patch) accordingly.

Each organization model has its benefits and considerations. The choice of model depends on factors like your team’s preferences, project complexity, maintainability, deployment strategies, and compatibility with your development tools and practices.

## API Spec

> An API Spec, short for API specification, is a document that outlines the details of how an application programming interface (API) should behave, including its endpoints, request and response formats, authentication methods, error handling, and other technical details. API specs serve as a contract between the API provider (server) and the API consumer (client), ensuring that both parties understand how to interact with the API.
> 

## Models

There are several formats and tools for creating API specs, each with its own features and advantages. Here are some commonly used API specification formats:

1. **OpenAPI Specification (OAS) / Swagger:** This is one of the most popular API specification formats. It uses a JSON or YAML format to describe the API’s endpoints, input and output parameters, authentication methods, response formats, and more. The Swagger UI and other tools make it easy to visualize and interact with APIs based on the OpenAPI Specification.
2. **API Blueprint:** API Blueprint is a format that uses a Markdown-based syntax to describe APIs. It’s designed to be human-readable and can be transformed into HTML documentation or machine-readable formats using various tools.
3. **RAML (RESTful API Modeling Language):** RAML is another YAML-based API specification format that focuses on modeling RESTful APIs. It includes features like data types, resource hierarchies, and security definitions.
4. **GraphQL SDL (Schema Definition Language):** GraphQL APIs are defined using a schema language that describes the types of data that can be queried and manipulated. While GraphQL is more about defining a schema than specifying each endpoint, it still serves as a form of API specification.

## Parts

An API spec typically includes the following components:

- **API Endpoints:** A list of all the endpoints (URL paths) that the API exposes.
- **HTTP Methods:** The HTTP methods (GET, POST, PUT, DELETE, etc.) supported by each endpoint.
- **Request Parameters:** The parameters that can be included in the API requests, including query parameters, request headers, and request bodies.
- **Response Formats:** The format and structure of the responses returned by the API, including possible status codes and response bodies.
- **Authentication and Authorization:** Details on how clients should authenticate themselves to access the API and what level of authorization is required for different endpoints.
- **Error Handling:** How errors are communicated to clients, including error codes, messages, and recommended actions.
- **Data Models:** Definitions of data structures used in the API, including their fields, types, and relationships.
- **Examples:** Sample requests and responses for various endpoints to help developers understand how to use the API.
- **Rate Limiting and Throttling:** If applicable, information about rate limiting and throttling mechanisms.

Creating and maintaining a clear and accurate API spec is essential for effective communication between development teams, ensuring consistent implementation, and providing clear documentation for API consumers. Additionally, tools like Swagger UI, ReDoc, and others can automatically generate interactive documentation from the API spec, making it easier for developers to explore and test the API.

## API Versioning Models

API versioning is a critical aspect of API design that helps you manage changes and updates to your APIs while ensuring backward compatibility for existing clients. There are several API versioning models you can use, each with its advantages and considerations. Here’s a list of common API versioning models:

1. **URI Versioning:**
    
    In URI versioning, the version information is included directly in the API endpoint’s URL. This is one of the simplest and most transparent methods.
    
    Example:
    
    ```
    https://api.example.com/v1/resource
    https://api.example.com/v2/resource
    ```
    
2. **Accept Header Versioning:**
    
    With Accept Header versioning, clients specify the desired API version in the HTTP `Accept` header when making requests. The server then responds with the appropriate version.
    
    Example:
    
    ```
    GET /resource
    Accept: application/vnd.myapi.v1+json
    ```
    
3. **Custom Header Versioning:**
    
    In Custom Header versioning, a custom header (e.g., `X-API-Version`) is added to the HTTP request to specify the API version.
    
    Example:
    
    ```
    GET /resource
    X-API-Version: 1
    ```
    
4. **Query Parameter Versioning:**
    
    Query parameter versioning involves adding a version parameter to the query string of API requests.
    
    Example:
    
    ```
    GET /resource?version=1
    ```
    
5. **Media Type Versioning (Content Negotiation):**
    
    In Media Type versioning, the API version is embedded in the media type (MIME type) of the request and response.
    
    Example:
    
    ```
    GET /resource
    Accept: application/vnd.myapi.v1+json
    Content-Type: application/vnd.myapi.v1+json
    ```
    
6. **Subdomain Versioning:**
    
    In Subdomain versioning, the API version is represented as a subdomain of the API’s root domain.
    
    Example:
    
    ```
    https://v1.api.example.com/resource
    https://v2.api.example.com/resource
    ```
    
7. **Header and Path Versioning (Hybrid):**
    
    In this model, you combine multiple versioning methods. For example, you can use a custom header for versioning and also include the version in the URI.
    
    Example:
    
    ```
    GET /v1/resource
    X-API-Version: 1
    ```
    
8. **Date-Based Versioning:**
    
    In date-based versioning, the API version is represented using a specific date format in the URL or headers. This approach can be helpful for indicating specific release dates of API versions.
    
    Example:
    
    ```
    https://api.example.com/2023-09-14/resource
    ```
    
9. **Namespace Versioning:**
    
    Namespace versioning involves placing the API version in the namespace of your code and endpoints. This is common in frameworks like ASP.NET Web API.
    
    Example (C#):
    
    ```csharp
    namespace MyApi.V1.Controllers{    // Controller logic for version 1}
    ```
    
10. **No Versioning (Backward Compatibility):**
    
    In some cases, you may choose not to include versioning information in the API. Instead, you ensure backward compatibility by carefully managing changes and deprecating old endpoints over time.
    

Each API versioning model has its own trade-offs, and the choice depends on your specific requirements and constraints. Consider factors like ease of implementation, client support, and the potential for future changes when selecting an API versioning approach.

## References

[How to Version a REST API](https://www.freecodecamp.org/news/how-to-version-a-rest-api/)

[How do you manage the underlying codebase for a versioned API?](https://stackoverflow.com/questions/29871744/how-do-you-manage-the-underlying-codebase-for-a-versioned-api)

---

> “Representational State Transfer (REST)” is an architectural style that guides the design of networked applications, especially web services, where data is seamlessly transferred through standardized representations, while each client request encapsulates the required state, fostering a stateless interaction model.
> 

**REST**: The term consists of two key components:

1. **Representational:** This refers to the way data is presented and exchanged between clients and servers. In a RESTful system, data is typically represented in standardized formats like JSON or XML. These representations define the structure, content, and relationships within the data.
2. **State Transfer:** This emphasizes the idea that the state of an application should be transferred between clients and servers as needed, rather than being stored on the server. Each client request should contain all the information required for the server to understand and process the request. The server doesn’t retain any context or session information between requests from the same client, which simplifies server management and enhances scalability.

In essence, **REST** is a set of architectural constraints and principles that guide the design of networked systems. It encourages the use of standard **HTTP** methods **(GET, POST, PUT, DELETE)** for operations on resources and employs uniform resource identifiers **(URIs)** to identify and locate resources. RESTful **APIs** adhere to these principles to create web services that are scalable, maintainable, and easily understandable by both humans and machines. The term “Representational State Transfer” captures the essence of how data is represented and exchanged while maintaining a stateless and uniform approach to interactions.

## Style & Principles

Key principles of **REST** include:

1. **Statelessness:** Each client request to the server must contain all the information needed to understand and fulfill the request. The server doesn’t store any client context between requests, which simplifies server implementation and allows for better scalability.
2. **Client-Server Interaction:** The architecture separates the client (user interface) from the server (data storage and processing), enabling each to evolve independently.
3. **Caching:** Responses from the server can be labeled as cacheable or non-cacheable. This improves performance by allowing clients to store and reuse responses, reducing the need for repeated requests to the server.
4. **Uniform Interface:** REST APIs should have a uniform way of interacting with resources, achieved through a combination of standardized HTTP methods (GET, POST, PUT, DELETE) and well-defined resource URLs.
5. **Layered System:** Intermediaries such as proxies and gateways can be introduced between clients and servers without affecting the overall system architecture. This enhances scalability, security, and resilience.
6. **Code-On-Demand (Optional):** Clients can request executable code (e.g., JavaScript) from the server to be executed within the client’s context. While this is an optional constraint, it’s not commonly used in typical RESTful APIs.

In practice, when you interact with a RESTful API, you use HTTP methods to perform operations on resources. For example: - `GET` retrieves data from the server. - `POST` sends data to the server to create a new resource. - `PUT` updates an existing resource with new data. - `DELETE` removes a resource.

## API Design

Sure, here’s a list of common REST API examples that you might find in a backend application:

1. **GET Request for Retrieving Data:**
    - Endpoint: `/api/users`
    - Description: Retrieves a list of users from the database.
    - Example: `GET /api/users`
2. **GET Request for Retrieving a Single Resource:**
    - Endpoint: `/api/users/{id}`
    - Description: Retrieves a specific user based on their ID.
    - Example: `GET /api/users/123`
3. **POST Request for Creating a Resource:**
    - Endpoint: `/api/users`
    - Description: Creates a new user.
    - Example: `POST /api/users`
    - Request Body: JSON representing user data.
4. **PUT Request for Updating a Resource:**
    - Endpoint: `/api/users/{id}`
    - Description: Updates an existing user’s information.
    - Example: `PUT /api/users/123`
    - Request Body: JSON with updated user data.
5. **PATCH Request for Partial Updates:**
    - Endpoint: `/api/users/{id}`
    - Description: Partially updates a user’s information.
    - Example: `PATCH /api/users/123`
    - Request Body: JSON with specific fields to update.
6. **DELETE Request for Deleting a Resource:**
    - Endpoint: `/api/users/{id}`
    - Description: Deletes a user from the system.
    - Example: `DELETE /api/users/123`
7. **GET Request with Query Parameters:**
    - Endpoint: `/api/products`
    - Description: Retrieves a list of products with optional filtering.
    - Example: `GET /api/products?category=electronics&price_max=500`
8. **GET Request with Pagination:**
    - Endpoint: `/api/posts`
    - Description: Retrieves a paginated list of posts.
    - Example: `GET /api/posts?page=2&per_page=10`
9. **GET Request with Sorting:**
    - Endpoint: `/api/orders`
    - Description: Retrieves a list of orders sorted by date.
    - Example: `GET /api/orders?sort=date`
10. **POST Request with File Upload:**
    - Endpoint: `/api/upload`
    - Description: Uploads a file to the server.
    - Example: `POST /api/upload`
    - Request Body: Form data containing the file.
11. **Authentication and Authorization:**
    - Endpoint: `/api/login`
    - Description: Authenticates a user and provides an access token.
    - Example: `POST /api/login`
    - Request Body: JSON with user credentials.
    - Response: JSON with an access token.
12. **Error Handling:**
    - Endpoint: `/api/products/{id}`
    - Description: Retrieves product details, handling errors if the product doesn’t exist.
    - Example: `GET /api/products/999`
    - Response: JSON with an error message.

These examples cover a range of common scenarios you might encounter when designing a RESTful API backend. Keep in mind that the specific endpoints, request/response formats, and data structures will depend on your application’s requirements and the resources you’re dealing with.

## Pagination Models

Pagination is a common technique used in APIs to manage and retrieve large sets of data in smaller, more manageable chunks. Various pagination models are employed in APIs to control how clients can request and navigate through paginated data. Here is a list of common pagination models used in APIs:

**Offset-Based Pagination:**

- Clients specify the number of items to skip (offset) and the maximum number of items to retrieve (limit) in the API request.
- Useful for providing precise control over which records to retrieve.
- Example: `GET /items?offset=10&limit=20`

**Page-Based Pagination:**

- Clients request a specific page of data, with each page containing a fixed number of items.
- Often combined with “page” and “page_size” query parameters.
- Example: `GET /items?page=2&page_size=10`

**Cursor-Based Pagination:**

- Clients receive a cursor (usually an opaque token) to the last retrieved item in a response, which they use to fetch the next set of data.
- Suitable for real-time data or data that may change frequently.
- Example: `GET /items?after=cursor123`

**Keyset Pagination (Token-Based Pagination):**

- Clients receive a unique identifier (e.g., a primary key) for the last item in a response, which they use to fetch the next set of data.
- Works well for ordered data sets where items can be uniquely identified.
- Example: `GET /items?last_id=123`

**Time-Based Pagination:**

- Clients specify a time range to retrieve data created or updated within that range.
- Ideal for time-series data or events.
- Example: `GET /items?start_time=2023-01-01T00:00:00&end_time=2023-01-31T23:59:59`

**Token-Based Pagination (Stateful Pagination):**

- Clients receive a pagination token (opaque token or hash) that represents their current position in the data set.
- The server keeps track of client state, allowing clients to continue from where they left off.
- Example: Using a pagination token like “nextPageToken” or “prevPageToken.”

**Combination Pagination:**

- Some APIs use a combination of multiple pagination models based on the specific use case. For example, they might use offset-based pagination for precise navigation and cursor-based or keyset-based pagination for real-time updates.

**Infinite Scroll:**

- Commonly used in web applications, infinite scroll automatically loads more data as the user scrolls down a page.
- Typically implemented using cursor-based or keyset pagination in the background.

**Fixed-Size Window Pagination:**

- Similar to page-based pagination but maintains a fixed-size sliding window of items. As users navigate through pages, the window shifts accordingly.
- Useful for maintaining context when users move between pages.

**Search-Based Pagination:**

- Clients specify search parameters along with pagination settings to retrieve a subset of matching results.
- Often used in search APIs to paginate through search results.

The choice of pagination model depends on the nature of your data, the requirements of your application, and the needs of your users. Each model has its advantages and trade-offs, and it’s essential to consider factors like data integrity, performance, and user experience when selecting the appropriate pagination approach for your API.

## REST API Query Languages

> API Query Languages are used to specify parameters and data in a Uniform Resource Identifier (URI) or URL.
> 

> API Query Languages serve various purposes, from filtering and searching data to specifying how to retrieve information from APIs. The choice of query language depends on the application, its data model, and the API’s design.
> 

**URL Query Parameters**: The most basic form of query language where parameters and values are appended to a URL after a question mark (`?`) and separated by ampersands (`&`). For example: `https://example.com/search?q=query&limit=10&page=1`

**JSON in URI**: JSON can be embedded within a query parameter, although it’s less common due to URL length limitations and potential encoding issues.

```
https://example.com/api?data={"name":"John","age":30}
```

**OData**: The Open Data Protocol (OData) is a standardized query language for RESTful APIs. It allows clients to filter, sort, and page through data.

```
https://example.com/odata/Users?$filter=age ge 18 and gender eq 'Male'&$orderby=createdAt desc&$top=10
```

**SQL-Like Queries**: Some APIs use SQL-like syntax to query data. This is more common in relational database APIs.

```
https://example.com/api?sql=SELECT * FROM customers WHERE country='USA'&limit=10
```

**XML-RPC**: XML-RPC, a remote procedure call protocol encoded in XML, can be passed as a query parameter.

```
https://example.com/rpc?method=getUserData&params=<param1>John</param1><param2>Doe</param2>
```

**SPARQL**: The SPARQL Protocol and RDF Query Language is used to query data stored in Resource Description Framework (RDF) format.

```
https://example.com/sparql?query=SELECT ?subject WHERE {?subject ?predicate ?object}
```

**JQL (Jira Query Language)**: Used for advanced searching in Jira, Atlassian’s issue tracking tool.

```
https://example.com/jira/rest/api/2/search?jql=project=EXAMPLE%20AND%20status=Open
```

**Lucene Query Syntax**: Lucene query syntax is often used for full-text search in systems like Elasticsearch. `https://example.com/search?q=title:(Elasticsearch%20Tutorial)&size=10` **GraphQL**: - GraphQL is a query language for APIs that allows clients to request only the data they need. - Clients can specify the shape and structure of the response. - Example: `query {       user(id: "123") {       name       email       }    }` **FQL (Facebook Query Language)**: - FQL is a query language used to retrieve data from the Facebook Graph API. - It allows complex queries for fetching user and page data. - Example: `SELECT name, email FROM user WHERE uid = me()`.

**CMIS (Content Management Interoperability Services)**: - CMIS is a query language used for accessing content management systems like Documentum and SharePoint. - It provides operations for querying and managing content. - Example: `SELECT * FROM cmis:document WHERE cmis:name LIKE '%.pdf'`.

**Linq (Language-Integrated Query)**: - LINQ is used in .NET to query collections, databases, and XML. - It provides a unified query syntax for different data sources. - Example: `var query = from product in products where product.Price > 50 select product`.

**XQuery**: - XQuery is a query language for XML documents. - It allows for complex querying and transformation of XML data. - Example: `for $book in doc("books.xml")//book where $book/price > 30 return $book/title`.

## References

[Representational State Transfer (REST)](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)

[What is HATEOAS?](https://recaffeinate.co/post/what-is-hateoas/)

[Microsoft REST API Guidelines (github.com/microsoft)](https://news.ycombinator.com/item?id=21609807)

[Ask HN: What is your go-to example for a good REST API?](https://news.ycombinator.com/item?id=11971491)

[Best practices for REST API design (2020) (stackoverflow.blog)](https://news.ycombinator.com/item?id=26225373)

[Stop Writing REST API Clients (ttezel.github.com)](https://news.ycombinator.com/item?id=5274550)

[Rules for REST API URI Design (restcase.com)](https://news.ycombinator.com/item?id=14579248)

[REST API Alternatives (programmableweb.com)](https://news.ycombinator.com/item?id=6950444)

[Open API Stack](https://openapistack.co/)

[API key](https://en.wikipedia.org/wiki/API_key)