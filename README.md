![image](https://github.com/abu-baasit/AirBnB_clone/assets/132352758/73a2824f-0c1a-4ce1-9a27-35f1d0bbc14f)
# AirBnB clone - The console

## Background Context

It involves Creation of a command interpreter(Cmd) to manage the hbnb projects.
The AirBnB clone project is a step towards building first full web application: the AirBnB clone. This first step is very important because its a foundation which the following project will be built upon: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and it involves:
* putting in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine
## Execution in both interractive and non-interractive
### Interractive
$ ./console.py
(hbnb) help  
###### Documented commands (type help <topic>):  
EOF  help  quit

(hbnb)  
(hbnb)  
(hbnb) quit  
$

### Non-interractive
$ echo "help" | ./console.py  
(hbnb)  
###### Documented commands (type help <topic>):
EOF  help  quit  
(hbnb)  
$  
$ cat test_help  
help  
$  
$ cat test_help | ./console.py  
(hbnb)  

###### Documented commands (type help <topic>):  
EOF  help  quit  
(hbnb)  
$  
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
