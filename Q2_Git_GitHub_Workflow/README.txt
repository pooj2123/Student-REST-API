QUESTION 2 - GIT AND GITHUB

GOAL
Create a local Git repository, commit your project, create a GitHub repository,
push the project, create a feature branch, and merge it into main.

REQUIREMENTS
- Git installed
- GitHub account
- Your project folder (you can use the Q1 folder)

PART A: CREATE A LOCAL REPOSITORY

STEP 1: Open your project folder in VS Code.
STEP 2: Open Terminal > New Terminal.
STEP 3: Initialize Git:
    git init

STEP 4: Add all project files:
    git add .

STEP 5: Commit:
    git commit -m "Initial commit"

If Git asks for your identity, configure it:
    git config --global user.name "Your Name"
    git config --global user.email "your-email@example.com"
Then run the commit command again.

PART B: CREATE A GITHUB REPOSITORY AND PUSH

STEP 6: Go to https://github.com and sign in.
STEP 7: Click the + icon (top-right) > New repository.
STEP 8: Enter a repository name, for example Student-REST-API.
STEP 9: Choose Public or Private. Do not initialize with a README if your local
project already has files. Click Create repository.

STEP 10: Set the main branch and connect your GitHub repository.
Replace YOUR-USERNAME and YOUR-REPOSITORY with your actual details:
    git branch -M main
    git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

STEP 11: Push:
    git push -u origin main

PART C: CREATE AND MERGE A FEATURE BRANCH

STEP 12: Create and switch to a feature branch:
    git switch -c feature-update

STEP 13: Make a small change. For example, create a file named feature.txt
and type: This is my feature branch change.

STEP 14: Add and commit the change:
    git add .
    git commit -m "Add feature update"

STEP 15: Switch back to main:
    git switch main

STEP 16: Merge the feature branch:
    git merge feature-update

STEP 17: Push the updated main branch to GitHub:
    git push origin main

STEP 18: Verify:
    git status
    git branch
    git log --oneline --all --graph

EXPECTED RESULT
- Your files are visible in the GitHub repository.
- The feature-update branch was created.
- The feature commit is included in main after merging.
- git status should say the working tree is clean.

IMPORTANT
If you get "remote origin already exists", use:
    git remote set-url origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

If GitHub asks you to sign in, complete the browser authentication prompt.
Never share your GitHub password or access token.
