#Sorting visualizer
Simple application to compare multiple sorting algorithm "nearly" at the same time. Each algorithm is started as a
separate thread without any synchronization mechanism so minute discrepancies might occur due to CPU resource allocation.

Application provides possibility to include any 3rd party sorting algorithm via plugin manager.

##Installing
To install application create new virtual environment:

    python3 -m venv /path/to/new/virtual/environment

Activate newly created venv. For windows users:

    [my-venv-directory]\Scripts\activate.bat

For Linux users:

    source [my-venv-directory]/bin/activate

Then install all required packages:

    pip install -r requirements.txt

##Using
To start application simply type:
    
    python main.py

Main screen:

![Main screen](pictures/main_screen.py)

In the header two parameters can be specified:
1. Sorting speed - due to poor performance of Tkinter graphic rendering capability function is not implemented - it is
    always moderately quick :)
2. Data type - initial data set. For "Random" option button "Generate array" becomes active in order to re-generate set

For each row separate algorithm can be chosen. Each row always operate on the same data set.

At the bottom buttons that allow to add/remove additional row to compare more/less algorithms at the same time.

Press start to... start.

##Plugin architecture
Application allows implementing additional algorithms without changing source codes. To add new algorithm:

Add new element in <code>algorithms</code> array where <code>name</code> is an algorithm name (visible later in 
"Algorithm" drop list for each row) and <code>algorithm</code> points to implementation in plugins folder.

###Plugin impelementation
Plugin must take positional arguments:
1. <code>data</code> - data to operate on
2. <code>canvas</code> - Tkinter Canvas object to draw on

To draw new data on canvas call somewhere in code:

    self.canvas_ui.draw(i, j, data)

Where:
* <code>i</code> and <code>j</code> are number of elements to be swapped on canvas
* <code>data</code> is array after iteration

Plugin also must use below import

    from algorithms.algorithm_provider import AlgorithmProvider

to implement below function:

    def initialize():
        AlgorithmProvider.register("QuickSort", QuickSortAlgorithm)

<code>initialize()</code> function from each plugin module is called during startup to register itself as plugin.

Example implementation of plugin can be found here:
[QuickSortAlgorithm.py](plugins/QuickSortAlgorithm.py)


