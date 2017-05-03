# Shannon Switching Game
A two-player abstract strategy game coded by Laura Isby and Ivy Lai Miller.
### Basic Requirements
Requires the installation of python 2.7, NetworkX, and NetworkX Viewer. The latter two can be installed via the terminal using pip.

NetworkX: http://networkx.github.io

NetworkX Viewer: https://github.com/jsexauer/networkx_viewer

## 1. Introduction to Shannon Switching Game

### Rules


Laura
## 2. Loading an input file
The file requires an input file of type .txt (although .input files should also work). The input file should have the information shown below. Comments can be made within the setup file with a line starting with '#'.

Designate the number of nodes/points as follows

    P [number of points/nodes]
Designate the special nodes (2) as follows.

    S [Special Node 1] [Special Node 2]

Designate the link between nodes as follows. If number of same links unspecified, the game will assume there is only one link.

    L [Node 1] [Node 2] [Number of same links]

## 3. Gameplay

### Playing the game
Start running the code in terminal. The code accepts the setup file as an input argument (using argv). For example, if the sample board is in the same folder as the code, you can type the following in your command line:


    > python [file_name].py [sample_board]


For example, I can type:

    > python shannon_switch.py Board_2.txt

After importing the block, you may see an error message if you have not fully specified the game. Otherwise, the game will ask Player 1 to choose if he/she wants to play in the _SHORT_ or _CUT_ mode. As explained earlier, _SHORT_ has the ability to "glue" connected notes to make them one node. _CUT_ has the ability to delete any link between two nodes.

After choosing the mode, a window should pop out to display the current network of nodes and links. The special nodes will be red and all other nodes will be blue. Once you close the window, you can enter the name of the two nodes (as integers) which you wish to cut or short. If there is no link between the node, you will get an error message and the player will need to try again.

The game always ends with one of the two players winning. If the special nodes cannot be connected (ie there is no path between the nodes), then _CUT_ wins. If the two special nodes have merged, then _SHORT_ wins.

## 4. Code Explanation/Run-Through

This code uses a Game class that will be initialized with a setup file. The initialization will be checked for errors and bugs within the setup file. There may be some interpretation issues if file is written on a Windows-based computer and read on a Linux or Mac. Simply copy the text in the input file and paste to a new file.

Next, the run function will create the board and display it once the first player designates his/her mode.
