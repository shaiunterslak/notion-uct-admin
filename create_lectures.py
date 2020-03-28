from notion.client import NotionClient
from scrape_dates import get_dates_arr
import datetime

COURSE_CODES = ["ECO3020F", "CSC3002F", "CSC3022F"]
NOTION_BLOCK_LINK = ""
TOKEN_V2 = ""


# takes an unformatted date string and returns a date object
def process_date_str(date_input):
    date_input = date_input.split()
    day_str = date_input[0]
    day_num = int(day_str)
    month_str = date_input[1]
    month_num = int(datetime.datetime.strptime(month_str, '%b').month)
    date = datetime.datetime(2020, month_num, day_num)
    return date


# Creates an individual lecture ticket on the notion board with the date field
# filled and the relevant course tagges
def make_lecture_todo(block, course_code, date, lecture_number):

    lectures = block.collection
    lecture = lectures.add_row()
    lecture.name = "Lecture "+lecture_number
    lecture.course = course_code
    lecture.date = process_date_str(date)
    lecture.status = 'up next'


# Uses all helper methods to fully process and add all of the lectures for all
# of the courses specified
def make_all_lectures(block_link):
    print("Initialising notion client...")
    client = NotionClient(
        token_v2=TOKEN_V2)
    block = client.get_block(block_link)

    for course_code in COURSE_CODES:
        dates = get_dates_arr(course_code)
        print("Creating "+course_code+" lectures in notion...")

        num_dates = len(dates)
        for i in range(num_dates):
            make_lecture_todo(block, course_code, dates[i], str(num_dates-i))


make_all_lectures(NOTION_BLOCK_LINK)
