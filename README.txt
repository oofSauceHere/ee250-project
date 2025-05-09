Team Members: Deccan Maniam, Sahil Pandit

Install Instructions:
- the libraries and dependencies can be installed using "pip install -r requirements.txt"
- also do "pip install flask numpy requests librosa soundfile"
- the code for each node doesn't need much setup besides directory setup (i.e. as long as the directories are set up properly, "python NODE_CODE.py" is sufficient)
    - for the server, the code will handle checking that the server_files dir exists (if not it will be created)-- server is basically just receiving files, processing, and storing new files to send; there isn't much to be done in terms of setup
    - for the vizualser, make sure that the working directory has a templates and static folder, which will store the visualiser page's html and the elements to be displayed respectively
        - We are using flask and so we have the file structure set up this way as a means of following convention

Libraries Used:
- All in requirements.txt