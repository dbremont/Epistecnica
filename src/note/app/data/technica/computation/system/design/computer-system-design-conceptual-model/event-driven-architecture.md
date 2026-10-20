---
tags: [architectural-style]
---

# Event-Driven Architecture


> Components communicate through events, where producers generate events and consumers react to them.
> 

**Characteristics:**

- Asynchronous communication
- Decoupled components

**Advantages:**

- Scalability
- Flexibility
- Real-time processing

**Disadvantages:**

- Debugging and maintenance complexity
- Event ordering and consistency challenges

![](https://i.imgur.com/fwHDXKY.png)

event

Event-Driven Architecture (EDA) or Event-Oriented Architecture is an architectural style that focuses on the communication and processing of events, which are discrete, meaningful occurrences or observations that have significance within a system or business domain. In an event-driven architecture, components or services communicate by producing and consuming events. This approach is used to build systems that are highly decoupled, scalable, responsive, and capable of handling real-time or near-real-time scenarios. Here are some key concepts and components of event-driven architecture:

1. **Event**: An event is a representation of a significant occurrence or piece of information within a system. Events can be of various types, such as data changes, user actions, system notifications, or external inputs. Events carry data that describes what happened and often include metadata like timestamps.
2. **Event Producer**: An event producer is a component or service responsible for generating and emitting events when certain conditions or actions occur. Event producers publish events to a central event bus or message broker.
3. **Event Consumer**: An event consumer is a component or service that subscribes to events from the event bus or message broker. When an event of interest is published, the event consumer processes it and takes appropriate actions.
4. **Event Bus or Message Broker**: An event bus or message broker acts as an intermediary that facilitates the communication between event producers and consumers. It ensures that events are delivered to the right consumers, often based on topics or channels.
5. **Event Stream**: An event stream is a continuous flow of events that represent a specific category or type of information. Event consumers can subscribe to event streams to receive relevant events in real-time.
6. **Event Sourcing**: Event sourcing is a design pattern where an application’s state is derived from a series of events. Instead of storing the current state, all changes to the state are captured as a sequence of events. This approach is often used in systems requiring audit trails and historical data.
7. **Event-driven Microservices**: Event-driven architecture is commonly used in microservices-based systems. Each microservice can act as both an event producer and consumer, allowing for loosely coupled and independently scalable services.
8. **Pub/Sub (Publish/Subscribe)**: Pub/Sub is a messaging pattern commonly associated with event-driven architectures. Event producers publish events to specific topics, and event consumers subscribe to topics of interest. This decouples producers and consumers.
9. **Event Handlers**: Event handlers are components within consumers that process incoming events. They execute business logic based on the content of the event, potentially updating the application’s state or triggering other events.
10. **Scalability**: Event-driven architecture promotes scalability because components can be added or removed without disrupting the overall system. It allows for distributed and parallel processing of events.
11. **Asynchronous Processing**: Events are processed asynchronously, which means that consumers can handle events at their own pace, making the system more responsive and fault-tolerant.
12. **Complex Event Processing (CEP)**: CEP is a technique used in event-driven architectures to analyze patterns and correlations within streams of events. It can be used for real-time analytics, fraud detection, and more.

Event-driven architecture is commonly used in various domains, including financial services, IoT (Internet of Things), e-commerce, and real-time analytics. It enables systems to react quickly to changing conditions and provides a flexible and scalable foundation for modern applications.

## References

- [Event-driven architecture, state machines et al.](https://250bpm.com/blog:25/index.html)