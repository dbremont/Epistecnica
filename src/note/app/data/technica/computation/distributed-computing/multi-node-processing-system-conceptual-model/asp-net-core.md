---
tags: [web-server]
---

# ASP.NET Core


![](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/_static/kestrel-to-internet2.png?view=aspnetcore-7.0)

ASP.NET Core App

ASP.NET Core is designed to be a flexible and modular framework, allowing developers to build web applications and services. The architecture of ASP.NET Core can be summarized as follows:

- **HTTP Request Pipeline**: At the core of ASP.NET Core is the request processing pipeline, which is composed of various middleware components. Each middleware performs specific tasks and can be chained together to process incoming HTTP requests and generate responses.
- **Cross-Platform and Modular**: ASP.NET Core is cross-platform, meaning it can run on different operating systems (Windows, Linux, macOS). It is designed to be modular, allowing developers to choose and include only the necessary components for their application, reducing overhead and improving performance.
- **Middleware-based**: The request processing in ASP.NET Core is middleware-based, allowing developers to extend the pipeline with custom middleware to handle specific tasks like authentication, caching, logging, etc.
- **Dependency Injection (DI)**: ASP.NET Core encourages the use of dependency injection to manage the application’s dependencies and promote loose coupling between components, making the application easier to maintain and test.
- **Hosting Environment**: ASP.NET Core applications are hosted in a web server, such as Kestrel (cross-platform) or Internet Information Services (IIS), or other host environments, depending on the deployment scenario.
- **Support for MVC and Web APIs**: ASP.NET Core provides built-in support for Model-View-Controller (MVC) architecture, allowing developers to build web applications following the MVC pattern. Additionally, it has excellent support for creating Web APIs using the same request processing pipeline.
- **Configuration and AppSettings**: ASP.NET Core provides a flexible configuration system that allows developers to configure various aspects of the application, such as connection strings, logging settings, and more, through configuration files (like appsettings.json) or environment variables.
- **Razor View Engine**: Razor is the default view engine in ASP.NET Core, enabling developers to create dynamic HTML views with server-side C# code seamlessly.
- **Middleware for Authentication and Authorization**: ASP.NET Core includes middleware components for handling authentication and authorization using various authentication schemes like cookies, JWT, OAuth, etc.
- **NuGet Package Management**: ASP.NET Core leverages NuGet for package management, making it easy to include and update libraries and dependencies in the application.

## Programming Model

> The ASP.NET programming model provides a framework for building web applications and services using Microsoft’s ASP.NET technology. It follows the Model-View-Controller (MVC) architecture and includes various components and patterns to facilitate web development.
> 

Here’s an overview of the ASP.NET programming model:

- **Model-View-Controller (MVC) Architecture**: The primary architectural pattern used in ASP.NET is MVC. It separates the application into three main components:
    - **Model**: Represents the data and business logic of the application.
    - **View**: Handles the user interface and presentation logic.
    - **Controller**: Acts as an intermediary between the Model and View, processing user requests, invoking appropriate actions, and updating the Model.
- **Routing and URL Mapping**: ASP.NET uses routing to map incoming URLs to specific controller actions. The routing system directs requests to the appropriate controller and action based on the URL pattern.
- **Razor View Engine**: Razor is the default view engine in ASP.NET, which provides a clean and concise syntax for creating dynamic HTML views with server-side C# code. Razor views allow developers to embed C# code directly into the HTML markup.
- **Dependency Injection (DI)**: ASP.NET supports dependency injection, allowing developers to define and manage dependencies within the application using built-in DI containers. DI promotes loose coupling between components, making the application more maintainable and testable.
- **Middleware-based Request Processing**: ASP.NET Core follows a middleware-based request processing pipeline, where each middleware component can process incoming HTTP requests and responses. Developers can chain multiple middleware to handle tasks such as authentication, logging, and caching.
- **Web API Support**: ASP.NET supports building Web APIs using the same MVC framework. Developers can create RESTful APIs to expose data and functionality to client applications.
- **Authentication and Authorization**: ASP.NET includes built-in middleware for handling authentication and authorization. Developers can integrate various authentication schemes like cookies, JWT, OAuth, etc., to secure their applications.
- **State Management**: ASP.NET offers various options for managing state, including client-side options like cookies and local storage, as well as server-side options like session and cache management.
- **Configuration and Settings**: ASP.NET allows developers to configure the application using various configuration sources, such as JSON files (appsettings.json), environment variables, and other providers.
- **Data Access**: ASP.NET provides robust data access capabilities through Entity Framework Core, allowing developers to interact with databases using object-relational mapping (ORM).
- **Validation and Data Binding**: ASP.NET supports data validation and binding, enabling automatic mapping of form data to model objects and validating input data.

Overall, the ASP.NET programming model simplifies web development by following established patterns and providing a set of powerful features and tools to build modern and scalable web applications and services.

## ASP.NET Core Middleware

> Middleware in ASP.NET Core refers to components that process HTTP requests and responses, allowing developers to add custom functionalities to the application’s request processing pipeline.
> 

![](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/index/_static/middleware-pipeline.svg?view=aspnetcore-7.0)

middleware

- **Routing Middleware**: Responsible for directing incoming HTTP requests to the appropriate endpoint or controller action based on the URL.
- **Static Files Middleware**: Used to serve static files such as HTML, CSS, JavaScript, images, etc., from the web server.
- **Authentication Middleware**: Enables authentication for incoming requests, allowing you to implement different authentication schemes like cookies, JWT, etc.
- **Authorization Middleware**: Used to perform authorization checks on incoming requests based on defined policies or roles.
- **Cors Middleware**: Enables Cross-Origin Resource Sharing (CORS) to allow or restrict cross-origin requests.
- **Session Middleware**: Provides support for managing user sessions using cookies or distributed caching.
- **Exception Middleware**: Captures unhandled exceptions and returns appropriate HTTP responses.
- **Response Caching Middleware**: Allows caching of HTTP responses to improve performance.
- **Response Compression Middleware**: Compresses the HTTP response to reduce its size and improve performance.
- **Request Localization Middleware**: Enables localization and sets the culture for incoming requests based on request headers or query parameters.
- **HTTPS Redirection Middleware**: Redirects HTTP requests to HTTPS to enforce secure communication.
- **Health Checks Middleware**: Allows you to define health checks for the application to monitor its status.
- **Middleware for MVC**: The Middleware for MVC in .NET Core handles incoming HTTP requests, performs routing, and invokes the appropriate controller action for processing and generating responses.
- **Razor Pages**: The Razor middleware in .NET Core handles rendering Razor views to generate dynamic HTML responses for web applications.
- **Serilog Middleware**: Integrates Serilog for structured logging.
- **SignalR Middleware**: Adds support for real-time communication using SignalR.
- **Swagger Middleware**: Integrates Swagger UI for documenting and testing APIs.
- **GraphQL Middleware**: Allows the usage of GraphQL in the ASP.NET Core application.

## Kastrel

> Connection middleware is different from ASP.NET Core Middleware. Connection middleware runs per-connection instead of per-request.
> 

[Connection middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/connection-middleware?view=aspnetcore-7.0)

## Authentication Schemes

In ASP.NET Core, the `authenticationScheme` parameter is used to specify the scheme for authentication. Different authentication schemes can represent various methods of authentication, such as cookies, JWTs, OAuth, etc. Here’s a list of some commonly used authentication schemes in ASP.NET Core:

1. **Cookie Authentication:** `CookieAuthenticationDefaults.AuthenticationScheme`: Represents cookie-based authentication.
2. **JWT Bearer Authentication:** `JwtBearerDefaults.AuthenticationScheme`: Represents JWT token authentication.
3. **OAuth Authentication (Generic):** `OAuthDefaults.AuthenticationScheme`: Represents OAuth authentication (can be used for various OAuth providers).
4. **OpenID Connect Authentication:** `OpenIdConnectDefaults.AuthenticationScheme`: Represents OpenID Connect authentication.
5. **Google Authentication:** `GoogleDefaults.AuthenticationScheme`: Represents Google authentication using OAuth.
6. **Facebook Authentication:** `FacebookDefaults.AuthenticationScheme`: Represents Facebook authentication using OAuth.
7. **Twitter Authentication:** `TwitterDefaults.AuthenticationScheme`: Represents Twitter authentication using OAuth.
8. **Microsoft Account Authentication:** `MicrosoftAccountDefaults.AuthenticationScheme`: Represents Microsoft Account authentication using OAuth.
9. **GitHub Authentication:** `GitHubDefaults.AuthenticationScheme`: Represents GitHub authentication using OAuth.
10. **LinkedIn Authentication:** `LinkedInDefaults.AuthenticationScheme`: Represents LinkedIn authentication using OAuth.
11. **Apple Authentication:** `AppleSignInDefaults.AuthenticationScheme`: Represents Apple authentication using Apple’s Sign In with Apple.

These are just a few examples, and there are many other authentication schemes available depending on the third-party providers or methods you want to integrate into your application.

When setting up authentication in your application’s `Startup.cs`, you’ll use the appropriate constants from these schemes to configure authentication middleware. The actual constant names may be slightly different based on the version of ASP.NET Core and the specific authentication libraries you’re using. Always refer to the official documentation or code samples for the most accurate and up-to-date information.

## References

[ASP.NET documentation](https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-7.0)

[ASP.NET Core Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-7.0)

[Chain-Of-Responsibility Pattern](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)

[Understanding .NET Generic Host Model](https://sahansera.dev/dotnet-core-generic-host/)

[.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-7.0)

[Advanced Architecture for ASP.NET Core Web API](https://www.infoq.com/articles/advanced-architecture-aspnet-core/)