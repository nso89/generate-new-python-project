# project-name
Project Description

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
* A complete install of `Python 3.x`.
* Under `Projects`, `main.py`.

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract `generate-new-python-project-main.zip`.

**Example**:
```batch
C:\Users\nso89\generate-new-python-project-main
```
#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `generate-new-python-project-main` folder.

**Example**:
```batch
C:\Users\nso89>cd generate-new-python-project-main
```
2. Start the `main.py` script.

**Example**:
```batch
C:\Users\nso89\job-workflow-main>python main.py
```

3. It asks you for the `Project Name`.

**Example**:
```batch
Project Name: Hello World
Generating: hello-world
Copying C:\Users\nso89\Projects\main.py to C:\Users\nso89\Projects\hello-world
```
The script create `1` folder, with the `Project Name` as the parent. It copies the `main.py` to the new folder.

#### <a name="configuration"></a>Configuration
If you need to change the `MAIN_PY`:

1. Open the `main.py` script in any text editor.
2. Locate the `MAIN_PY` variable.

**Example**:
```python
MAIN_PY = Path.home().joinpath("Projects\\main.py")
```
3. When you finish changing the variables, save and close the editor.
