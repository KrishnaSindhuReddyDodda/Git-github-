Initially we have created a python files ( Amstrong.py , Diamond.py , Pascal triangle.py and Palindrome.py ) in system. These files are uploaded into Github repository named "Git-github-". This Github repository is also named as "origin". Now coming to LOCAL REPOSITORY we have created folder named "repo" on desktop.

Open the file "repo" and Right click on it and select Git Bash.
It opens Git Bash and to create a ".git" file 

   i) Type git init command.
   
Now type below commands to push files in remote repository to local repository 

   i) git remote add origin "https://github.com/KrishnaSindhuReddyDodda/Git-github-.git" 
   ii)git push origin main

Here I created a files (file1.txt , login.html , university_website.html) in local repositories but these are not in Index, so to push into Index or Staging area. Since these are untracked files we need to track them. To commit them following commands need to be performed. 

i) git add -A # Multiple files to add into Index area. For each commit we need to write a commit message 
   ii) git commit -a -m "This is my first multiple commit" 

To find the status of the files like whether the files are tracked or untracked following command should be performed. 

i) git status To see the commit files ($git commit) Here each commit will have unique commit-id. Where each commit-id contains Time of commit, when and by whom commit is done and uploaded information will be identified in it.

Here branch named "branch" is created with following command 

i) git checkout branch               # It will checkout into branch named branch from "master branch" To merge branches we have created two branches named first_branch_file.txt                                          and second_branch_file.txt like 
   i) git add -A 
   ii) git commit -a -m "This is my first commit on branches" 
   iii) git merge master From the above command It will merge branch into master branch so that we have all files into branch1 branch. 

To list all files perform " $ls " command. while pushing local data into remote data we can find all files into it, that can be performed using following command
   i) git push master origin
