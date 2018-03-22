# Medicine

*python version: 3.5*

To use this program, you have to install Neo4j (graph database) and create an env.py file. You can find an example to the env file.
The env file is a configuration file, where you can set the database connenction username and password.

"requirements.txt" is a file containing a list of items to be installed

**Create network**
To create a network use the *finder.py* file. 
To set the start urls change the *urls.txt* file. Each url must be a new line.  The format **"http://www.example.com" : "type"**. Type can be legal, illegal or undefined. Each line must end with a comma except the last line. It's important to use *"* not apostrophe (*'*)
 
**Data**

To get datas use the *network.py* file. This file create an image of the network and a file (*.gexf*) which can import into *"Gephi"* (https://gephi.org)
