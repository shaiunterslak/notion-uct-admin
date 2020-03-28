# returns true if a string can be represented as an int
def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# searches through each line of the file for a date and appends it to
# an array which is later returned


def get_dates_arr(course):
    file_name = "./course-lecture-pages/"+course+".txt"
    print("Fetching dates from "+course+".txt...")
    file = open(file_name, "r")
    dates = []
    for line in file:
        first_char = line[0:1]

        # If the line starts with an int, it is presumed to be a date
        if is_int(first_char):
            date_input = line.split()[0:2]
            day_str = date_input[0]
            month_str = date_input[1]
            date_formatted = day_str+" "+month_str
            try:
                dates.index(date_formatted)

            except:
                dates.append(date_formatted)

    return dates
