---
tags: [model-of-computation]
---

# Actor Model of Computation


> The Actor Model of Computation is a theoretical framework for concurrent computation based on autonomous actors that communicate through asynchronous message passing.
> 

![](https://www.brianstorti.com/assets/images/actors.png)

**¿What computations does the model help us to encode?**

The model helps us encode computations involving concurrent processes that can operate independently and communicate with each other by exchanging messages.

**¿What is the abstract machine?**

The abstract machine in the Actor Model consists of a collection of actors, each with its own state and mailbox for incoming messages, and follows rules for message delivery and actor behavior.

**¿How to encode computations?**

Computations in the Actor Model are encoded by defining individual actors with their initial state, message processing rules, and message-passing interactions with other actors.

**¿What is an actor?**

An actor is a computational entity that, in response to a message it receives, can concurrently:

- send a finite number of messages to other actors;
- create a finite number of new actors;
- designate the behavior to be used for the next message it receives.

## References

Agha, G. (1985). ACTORS: A Model of Concurrent Computation in Distributed Systems. https://dspace.mit.edu/handle/1721.1/6952

[The actor model in 10 minutes](https://www.brianstorti.com/the-actor-model/)

[Understanding The Actor Model To Build Non-blocking, High-throughput Distributed Systems - Scaleyourapp](https://scaleyourapp.com/actor-model/)