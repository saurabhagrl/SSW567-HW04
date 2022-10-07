# SSW-567-HW04

## Homework 04a 
Develop with the Perspective of the Tester in mind

**Q**. Write a description of what you thought about when you were designing the code.  What did *you* think was important to do to make it easy to test the program.  What are some of the challenges that you faced when testing this assignment

**Ans**. I had to learn about requests and learn about Github API from https://docs.github.com/en/rest this website. I did this by implementing constant files and it made my life easy by importing them to the githubapi.py file to get the required results. For testing, I did this by implementing a simple unittest package and self-asserting to the gihubapi, and capturing and running the package to the output. Then for automating it, I used CircleCI and added commands for output to be added to the Test Result folder.

The challenge that I faced during this was configuring the config.yml file. It took almost 15 CircleCI steps to get my success status for this assignment. 


[![NehharShah](https://circleci.com/gh/NehharShah/SSW-567-HW04.svg?style=svg)](https://app.circleci.com/pipelines/github/NehharShah/SSW-567-HW04?branch=main&filter=all)
