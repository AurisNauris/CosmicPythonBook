# Preface

## Recommended books

Note: majority of books on software architecture etc are written in C++ or Java
- Domain-Driven Design by Eric Evans
- Patterns of Enterprise Application Architecture by Martin Fowler

## Three tools for managing complexity

### Test-driven development (TDD)
- Developing software by writing tests first and only then writing the actual code.
- Red-Green-Refactor cycle: define functionality by writing a test that needs to be passed but the test fails because the code does not exist yet (red), then write an absolute minimum of code so as to pass the test (green), now clean up and further test the code until all aditional tests are passed (refactor)
### Domain-driven design (DDD)
 - Building software that mimics the structure of the company by breaking it into departments units etc (need to double check if I got it right)

### event-driven architecture
- Build software that has event generators, event distributors, and event consumption

## soft prerequisits

- Flask: framework for Python to build web applications and APIs
- SQLAlchemy: Python SQL toolkit that allows to interact with SQL database using Pythonic language.
- pytest: used to write software tests, including units test, etc in python
- Docker: manager of containers, where container contains say my specific environment and code that needs to run
- Redis - in-memory data structure for caching, message exchange, steaming engine; also offers disk persistence.