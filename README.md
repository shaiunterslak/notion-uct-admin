# notion-uct-admin
A python script that uses the unofficial notion api to create dated tickets tagged by course codes for an easy university workflow.

This allows you to view all of your lectures on a calendar, tag them by week, write notes in an actual lecture object, create note templates that can be reused, easily keep track of lectures you've watched by changing their status. Tag lectures by how well you understand them, etc.


# usage

## Notion:
Navigate to the Notion board that you want to use as your university lecture page and paste the link in the NOTION_BLOCK_LINK variable at the top of the create_lectures.py file.

Create a ticket and make sure the following properties are there:
- Status (should be there by default, just make sure to change 'not started' to 'up next')
- Date (of type date)
- Course (of type select)

Obtain the token_v2 cookie from Notion (in chrome press the lock in the search bar, expand the www.notion.so toggle, expand the cookies toggle, copy the contents of the token_v2 cookie) paste the contents in the TOKEN_V2 variable at the top of the create_lectures.py file.


## Vula:
Go to the lectures tab on Vula for each course. Press cmd A (mac) or ctr A and paste the entire page contents to a text file in 'course-lecture-pages' named the course code.txt eg for ECO3020F the text file will be ECO3020F.txt

Add all of the course codes to the COURSE_CODES array at the top of the create_lectures.py file.
Run:

       pip install notion

Consult https://github.com/jamalex/notion-py for more details on the Notion library itself

Then simply run the create_lectures.py file and the Notion board will be popluated with all of the lectures that took place for each course, tagged by date and course code. 
