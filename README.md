# SDA-TODO-API

This is a cloud application that was developed for the SDA interview process. The aim of the application is to provide a simple API that allows the clients to perform the whole CRUD.
The application was developed with the following cloud tools provided by AWS:

- API Geteway
- Lambda functions
- DynamoDB

The sections below will explain about the selected API architecture and another possible way to implement it.

## TODO Architecture

![SDA-Arc drawio (1)](https://user-images.githubusercontent.com/50907344/185396779-f6e374ed-95b6-41dc-85cf-d719f35fc7d5.png)

### Why did I select this architecture ?

With this architecture, it is possible to divide the services, that is, having separate functions for each implementation can give us more flexibility. If the team decides to scale the application, only the bottleneck will scale, not the entire block as is often the case with monolithic architectures. With this in hand, you can deduce that this would reduce application costs, as your application is a group of small packages and each package can be scaled independently without changing the others.

### API Gateway

It provides 2 resources (routes) for the application, they are:
- /todo
- /todo/{todo-id}

Those routes are connected with the lambda functions, and those functions work in individual tasks.

The Gateway is deployed and the first stage deployed is called v1 (version 1), it means that the whole URL will have following format:
- https:// --AWS URL--/v1/todo/{todo-id}

#### /TODO

This resource has 2 methods, they are:
- List all the todos
- Create a new instance

#### /TODO/{todo-id}

This resource has 3 methods, they are:
- Retrieve a specific todo
- Update a specific todo
- Delete a specific todo

### DynamoDB

It has the TODO table where the lambda functions have full access (write and read).

### Lambda Functions

They are responsible for establishing the communication between the "client" and the DB. Each function is responsible for one task.

## Documentation

The documentation can be found at the following URL, where there is a postman collection and the user can try to use the TODO-API.

https://documenter.getpostman.com/view/13023755/VUqoPHgK#2ff6a985-2b18-493b-a134-2c1f4514f55d
https://www.getpostman.com/collections/a5135dbe67a030ed3d52

