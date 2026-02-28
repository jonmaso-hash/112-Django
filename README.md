1. create the folder for the project 
2. Create the virtual enviroment (python -m venv venv)
3. Active venv .\venv\Scripts\activate
4. Install django ()
5. upload dependcies into requirement file (pip freeze > requirement)
6. Complete the structure of the project (create templates and static folders)
7. finish the settings

Notes for repos
1. make sure all of your files are saved!
2. on the terminal (make sure you're in the right folder) excute the command **git init**
3. If you need a gitignore file, make sure to create that file and set up correctly. 
4. add all of the files from your project, by executing: **git add -A**
5.save all of those in a single group (called, commit) **git commit -m**
6. Create the main branch (the space where we are going to store all of the comits): **git branch -M main**
7. add teh remote to our project ( teh repo from github where we are going to communicate): **git remote add orgin 
git@github.com: your_github_username/name-of-your-repo.gi
8. optional: if you want to verify which repo it's linked: **git remore -v**
9. send everything to github (push the elements to the repo) **git push orginal main**

git remote add origin https://github.com/jonmaso-hash/112-Django.git
git branch -M main
git push -u origin main

manage.py runserver