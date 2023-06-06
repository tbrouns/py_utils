from datetime import date, datetime


def get_month_and_day_format():
    return "%m-%d"


def get_short_date_format():
    return "%Y-%m-%d"


def get_long_date_format():
    return f"{get_short_date_format()}T%H:%M"


def convert_date_to_string(date_to_convert, format_type="short"):
    if format_type == "short":
        dateformat = get_short_date_format()
    elif format_type == "long":
        dateformat = get_long_date_format()
    else:
        raise f"Format type {format_type} not supported!"
    return date_to_convert.strftime(dateformat)


def convert_string_to_date(date_string):
    format_short = get_short_date_format()
    formats = [format_short, get_long_date_format(), f"{format_short}T-%H:%M"]
    dt = None
    for f in formats:
        try:
            dt = datetime.strptime(date_string, f)
            break
        except:
            dt = None
    return dt


def aggregate_data_for_time_window(data_dict, data_for_timescale, variable_list):
    for time_window in data_dict.keys():
        for hour in data_dict[time_window]["hour_indices"]:
            for variable in variable_list:
                if variable not in data_dict[time_window]:
                    data_dict[time_window][variable] = []
                datapoint = data_for_timescale[variable][hour]
                data_dict[time_window][variable].append(datapoint)
    return data_dict


def get_weekday_and_hours(date_string, no_year=False):
    dt = convert_string_to_date(date_string)
    if no_year:
        date_format = get_month_and_day_format()
    else:
        date_format = f"{get_short_date_format()},%A"
    weekday = dt.strftime(date_format)
    hours = dt.hour
    return weekday, hours


def get_current_date():
    today = date.today()
    return today.strftime("%Y-%m-%d")


def get_week_number(date_string):
    dt = convert_string_to_date(date_string)
    week_number = date(dt.year, dt.month, dt.day).isocalendar()[1]
    return f"{dt.year} {week_number}"
