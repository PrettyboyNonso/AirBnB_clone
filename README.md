# Project: 0x00. AirBnB clone - The console
![65f4a1dd9c51265f49d0](https://github.com/a3ela/AirBnB_clone/assets/117747814/4c0534cc-714e-4d4e-abd5-8c867104ed60)

The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
![image1](https://github.com/a3ela/AirBnB_clone/assets/117747814/6acc2078-274a-4854-822d-a8ce26c5463b)

## Resources

#### Read or watch:

- [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
- [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
- [packages concept page]()
- [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
- [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
- [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
- [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
- [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
- [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
- [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)

### how to run it

- Open the Command Prompt and type <br>
  <code>python console.py</code>
- Type Help once the console runs to see the commands <br>
  <code> (HBNB) Help </code>

## Learning Objectives

### General

- How to create a Python package
- How to create a command interpreter in Python using the <code>cmd</code> module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage <code>datetime</code>
- What is an <code>UUID</code>
- What is <code>\*args</code> and how to use it
- What is <code>\*\*kwargs</code> and how to use it
- How to handle named arguments in a function

## Discribtion and commands for the interface

| Command                                                     | Description                                                                                                              |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `quit`                                                      | Quits the console                                                                                                        |
| `Ctrl+D`                                                    | Quits the console                                                                                                        |
| `help` or `help <command>`                                  | Displays all commands or displays instructions for a specific command                                                    |
| `create <class>`                                            | Creates an object of type `<class>`, saves it to a JSON file, and prints the object's ID                                 |
| `show <class> <ID>`                                         | Shows the string representation of an object                                                                             |
| `destroy <class> <ID>`                                      | Deletes an object                                                                                                        |
| `all` or `all <class>`                                      | Prints all string representations of all objects or prints all string representations of all objects of a specific class |
| `update <class> <id> <attribute name> "<attribute value>"`  | Updates an object with a certain attribute (new or existing)                                                             |
| `<class>.all()`                                             | Same as `all <class>`                                                                                                    |
| `<class>.count()`                                           | Retrieves the number of objects of a certain class                                                                       |
| `<class>.show(<ID>)`                                        | Same as `show <class> <ID>`                                                                                              |
| `<class>.destroy(<ID>)`                                     | Same as `destroy <class> <ID>`                                                                                           |
| `<class>.update(<ID>, <attribute name>, <attribute value>)` | Same as `update <class> <ID> <attribute name> <attribute value>`                                                         |
| `<class>.update(<ID>, <dictionary representation>)`         | Updates an object based on a dictionary representation of attribute names and values                                     |
