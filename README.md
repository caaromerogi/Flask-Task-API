# Flask Api

This api was developed with Python using flask framework and connected with SQLite.

### How to use

I recommend to have virtualenv dependency to work with flask. Inside this repo you will find a Virtual Environment called venv, is not necessary (but recommended) to have virtualenv dependency to activate the venv. To acivate the environment follow the next steps:

1. Make sure that you are inside Flask directory in command line, you will see something like this:

```
C:\Users\carlo\OneDrive\Escritorio\Flask>
```

2. Once completed the last step, execute the file activate.ps1 inside venv/Script folder. To do this, in the command line writes the next line (./venv/Scripts/activate.ps1):

```
PS C:\Users\carlo\OneDrive\Escritorio\Flask> .\venv\Scripts\activate.ps1
```

3. If the process was successfully executed you will see the prefix (venv) in your command line as the next:

```
(venv) PS C:\Users\carlo\OneDrive\Escritorio\Flask>
```

4. (Optiona) You can deactivate the venv writing the command "deactivate" in command line an you won't see anymor (venv) prefix in command line.

```
PS C:\Users\carlo\OneDrive\Escritorio\Flask> deactivate
```

Remember, if you want to install a dependency for a specific don't do it outside of a venv, becase you will install the dependecy globally and this can cause compatibility issues in the future. Make sure to create a venv for every python project that you do.
