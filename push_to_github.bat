@echo off
echo ========================================
echo  Python QuickStart Course - GitHub Setup
echo ========================================
echo.
echo This script will push your code to GitHub.
echo Make sure you've created the repository first!
echo.
echo Repository URL: https://github.com/wiradjuri/python-quickstart-course
echo.
pause

echo Adding GitHub remote...
git remote add origin https://github.com/wiradjuri/python-quickstart-course.git

echo Renaming branch to main...
git branch -M main

echo Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo  SUCCESS! Your code is now on GitHub!
echo ========================================
echo.
echo Next steps:
echo 1. Go to: https://github.com/wiradjuri/python-quickstart-course
echo 2. Check the Actions tab to see the workflow running
echo 3. Create a release (v1.0.0) to trigger the full build process
echo.
echo See setup_github.md for detailed instructions!
echo.
pause
