# How to use git

## Start a repo from scratch
- create a folder which contains the project
- initialize the git repository inside the folder
```shell
git init
```
- add the files to the repository with
```shell
git add
```
- commit the files/changes to the repo
```
git commit 
```

## Start a repo from an existing project
- initialize a new repo inside the existing folder
- `git add` all the relevant files
- add an .gitignore file 
```shell
git add .gitignore
```
- `git commit` your files/changes

## Connect an existing project to GitHub
- remote add the existing GitHub repo to your local folder
```shell
git remote add origin git@github.com:username/new_repo
# or use
git remote add origin https://github.com/username/new_repo
```
- push the changes/files to the GitHub repo
```shell
git push -u origin master
```
