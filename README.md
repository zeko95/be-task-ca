# Backend Task - Clean Architecture

This project is a very naive implementation of a simple shop system. It mimics in its structure a real world example of a service that was prepared for being split into microservices and uses the current Helu backend tech stack.

## Goals

Please answer the following questions:

1. Why can we not easily split this project into two microservices?
    - Shared Database which contradicts a core microservices principle. True microservice independence requires each service to manage its own data store.
    - Cross-Service Repository Access. In a microservices setup, this would require inter-service communication (e.g., via HTTP or messaging), not direct access to another module’s database to prevent coupling between services.
    - There are shared utility modules (e.g., common.py, database.py) used across domains, which further hinders separation. Proper microservices should isolate logic, infrastructure, and data per domain.
    - Tight coupling, making independent deployment and scaling difficult.
2. Why does this project not adhere to the clean architecture even though we have seperate modules for api, repositories, usecases and the model?
    - Tight Coupling. User use cases directly depend on the Item repository, violating the principle that inner layers should not depend on outer layers. There's no abstraction (interface) to decouple them;
   Use cases depend on the persistence layer (repository.py). Clean Architecture requires that inner layers (use cases) depend only on abstractions (interfaces), not on outer layers like persistence;
   Dependency on the web framework within the business layer, raise FastAPI's HTTPException;
    - Even though we are trying to have good structure it doesn't mean we have good architecture. Clean Architecture dictates: "Dependencies must always point inward." The inner layers (entities, use cases) should not depend on outer layers (frameworks, databases, APIs).
   We would need to add Domain Entities, avoid depending on a framework, move DTOs to API level, add dedicated business entities, implement interface in repository.
3. What would be your plan to refactor the project to stick to the clean architecture?
    - Thoroughly review the existing codebase to identify business logic, data access code, and framework-specific elements.
    - Clearly define and implement the layers of Clean Architecture:
      - Core Layer: Create domain entities representing core business rules and models. These must be independent of any framework or database.
      - Application Layer: Implement application-specific business rules and workflows that interact solely with domain entities.
      - Interface Adapters: Define abstract interfaces for repositories that use cases will depend on. Relocate DTOs (schemas) and their conversion logic to this layer, specifically within the API adapter, as they are for external communication
      - Infrastructure Layer: All connections to external databases, framework, aplications.
4. How can you make dependencies between modules more explicit?
    - Make sure to use interfaces for abstractions and not on specific implementations.
    - Implement dependency injection, favor injecting dependencies through class constructors, FastAPI's built-in dependency injection system can be leveraged for managing dependencies at the API endpoint level, ensuring that services and repositories are provided correctly.
*Please do not spend more than 2-3 hours on this task.*

Stretch goals:
* Fork the repository and start refactoring
* Write meaningful tests
* Replace the SQL repository with an in-memory implementation

## References
* [Clean Architecture by Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
* [Clean Architecture in Python](https://www.youtube.com/watch?v=C7MRkqP5NRI)
* [A detailed summary of the Clean Architecture book by Uncle Bob](https://github.com/serodriguez68/clean-architecture)

## How to use this project

If you have not installed poetry you find instructions [here](https://python-poetry.org/).

1. `docker-compose up` - runs a postgres instance for development
2. `poetry install` - install all dependency for the project
3. `poetry run schema` - creates the database schema in the postgres instance
4. `poetry run start` - runs the development server at port 8000
5. `/postman` - contains an postman environment and collections to test the project

## Other commands

* `poetry run graph` - draws a dependency graph for the project
* `poetry run tests` - runs the test suite
* `poetry run lint` - runs flake8 with a few plugins
* `poetry run format` - uses isort and black for autoformating
* `poetry run typing` - uses mypy to typecheck the project

## Specification - A simple shop

* As a customer, I want to be able to create an account so that I can save my personal information.
* As a customer, I want to be able to view detailed product information, such as price, quantity available, and product description, so that I can make an informed purchase decision.
* As a customer, I want to be able to add products to my cart so that I can easily keep track of my intended purchases.
* As an inventory manager, I want to be able to add new products to the system so that they are available for customers to purchase.