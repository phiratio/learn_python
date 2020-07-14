# Creational:
These patterns solve the problems associated with object creation and initialization. These are problems that occur the earliest in the life cycle of problem solving with objects and classes. Take a look at the following examples:
#### The Factory pattern: The "How do I make sure I can create related class instances in a repeatable and predictable fashion?" question is solved by the Factory class of patterns
#### The Prototype pattern: The "What is a smart approach to instantiate an object, and then create hundreds of similar objects by just copying across this one object ?" question is solved by the Prototype patterns
#### Singleton and related patterns: The "How do I make sure that any instance of a class I create is created and initialized just once" or "How do I make sure that any instances of a class share the same initial state ?" questions are solved by the Singleton and related patterns

# Structural:
These patterns concern themselves with composition and assembling of objects into meaningful structures, which provides the architect and developer with reusable behaviors, where "the whole is more than the sum of its parts". Naturally, they occur in the next step of problem solving with objects, once they are created. Examples of such problems are as follows:
#### The Proxy pattern: "How do I control access to an object and its methods via a wrapper, behavior on top?"
#### The Composite pattern: "How can I represent an object which is made of many components at the same time using the same class for representing the part and the whole—for example, a Widget tree ?"

# Behavioral:
These patterns solve the problems originating with runtime interactions of objects, and how they distribute responsibilities. Naturally, they occur in the later stage, once the classes are created, and then combined into larger structures. Here are a couple of examples:
#### Using the Median pattern in such case: "Ensure that all the objects use loose coupling to refer to each other at runtime to promote run-time dynamism for interactions"
#### Using the Observer pattern in such case: "An object wants to be notified when the state of a resource changes, but it does not want to keep polling the resource to find this out. There may be many such instances of objects in the system"