# ee250-project

Team Members: Deccan Maniam, Sahil Pandit

Install Instructions:
1. The libraries and dependencies can be installed using `pip install -r requirements.txt`
2. The code for each node doesn't need much setup besides directory setup (i.e. as long as the directories are set up properly, "python NODE_CODE.py" is sufficient)

    a. For the server, the code will handle checking that the server_files dir exists (if not it will be created)-- server is basically just receiving files, processing, and storing new files to send; there isn't much to be done in terms of setup

    b. For the vizualser, make sure that the working directory has a templates and static folder, which will store the visualiser page's html and the elements to be displayed respectively

3. Clone [this repo](https://github.com/ankanbhunia/Handwriting-Transformers) into the parent directory and follow the instructions in their README. This is *crucial* - the entire handwriting generation step depends on this model (provided by Bhunia et. al.)


Libraries Used:
- All in requirements.txt
