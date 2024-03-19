import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:





# write function to plot rankings over time for 1 roller coaster here:










plt.clf()

# write function to plot rankings over time for 2 roller coasters here:










plt.clf()

# write function to plot top n rankings over time here:










plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()


""" 
1.
In order to complete this project, you should have completed the first two lessons in the Data Analysis with Pandas course and the first two lessons in the Data Visualization in Python course. This content is also covered in the Data Scientist Career Path.

Project Requirements
2.
Roller coasters are thrilling amusement park rides designed to make you squeal and scream! They take you up high, drop you to the ground quickly, and sometimes even spin you upside down before returning to a stop. Today you will be taking control back from the roller coasters and visualizing data covering international roller coaster rankings and roller coaster statistics.

Roller coasters are often split into two main categories based on their construction material: wood or steel. Rankings for the best wood and steel roller coasters from the 2013 to 2018 Golden Ticket Awards are provided in 'Golden_Ticket_Award_Winners_Wood.csv' and 'Golden_Ticket_Award_Winners_Steel.csv', respectively. Load each csv into a DataFrame and inspect it to gain familiarity with the data.

Open the hint for more information about each column of the datasets.


Stuck? Get a hint
3.
Write a function that will plot the ranking of a given roller coaster over time as a line. Your function should take a roller coaster’s name and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.

Call your function with "El Toro" as the roller coaster name and the wood ranking DataFrame. What issue do you notice? Update your function with an additional argument to alleviate the problem, and retest your function.


Stuck? Get a hint
4.
Write a function that will plot the ranking of two given roller coasters over time as lines. Your function should take both roller coasters’ names and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.

Call your function with "El Toro" as one roller coaster name, “Boulder Dash“ as the other roller coaster name, and the wood ranking DataFrame. What issue do you notice? Update your function with two additional arguments to alleviate the problem, and retest your function.


Stuck? Get a hint
5.
Write a function that will plot the ranking of the top n ranked roller coasters over time as lines. Your function should take a number n and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.

For example, if n == 5, your function should plot a line for each roller coaster that has a rank of 5 or lower.

Call your function with a value for n and either the wood ranking or steel ranking DataFrame.


Stuck? Get a hint
6.
Now that you’ve visualized rankings over time, let’s dive into the actual statistics of roller coasters themselves. Captain Coaster is a popular site for recording roller coaster information. Data on all roller coasters documented on Captain Coaster has been accessed through its API and stored in roller_coasters.csv. Load the data from the csv into a DataFrame and inspect it to gain familiarity with the data.

Open the hint for more information about each column of the dataset.


Stuck? Get a hint
7.
Write a function that plots a histogram of any numeric column of the roller coaster DataFrame. Your function should take a DataFrame and a column name for which a histogram should be constructed as arguments. Make sure to include informative labels that describe your visualization.

Call your function with the roller coaster DataFrame and one of the column names.


Stuck? Get a hint
8.
Write a function that creates a bar chart showing the number of inversions for each roller coaster at an amusement park. Your function should take the roller coaster DataFrame and an amusement park name as arguments. Make sure to include informative labels that describe your visualization.

Call your function with the roller coaster DataFrame and an amusement park name.


Stuck? Get a hint
9.
Write a function that creates a pie chart that compares the number of operating roller coasters ('status.operating') to the number of closed roller coasters ('status.closed.definitely'). Your function should take the roller coaster DataFrame as an argument. Make sure to include informative labels that describe your visualization.

Call your function with the roller coaster DataFrame.


Stuck? Get a hint
10.
.scatter() is another useful function in matplotlib that you might not have seen before. .scatter() produces a scatter plot, which is similar to .plot() in that it plots points on a figure. .scatter(), however, does not connect the points with a line. This allows you to analyze the relationship between to variables. Find .scatter()‘s documentation here.

Write a function that creates a scatter plot of two numeric columns of the roller coaster DataFrame. Your function should take the roller coaster DataFrame and two-column names as arguments. Make sure to include informative labels that describe your visualization.

Call your function with the roller coaster DataFrame and two-column names.


Stuck? Get a hint
11.
Part of the fun of data analysis and visualization is digging into the data you have and answering questions that come to your mind.

Some questions you might want to answer with the datasets provided include:

What roller coaster seating type is most popular? And do different seating types result in higher/faster/longer roller coasters?
Do roller coaster manufacturers have any specialties (do they focus on speed, height, seating type, or inversions)?
Do amusement parks have any specialties?
What visualizations can you create that answer these questions, and any others that come to you? Share the questions you ask and the accompanying visualizations you create on the Codecademy forums.

Solution
12.
Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.

"""