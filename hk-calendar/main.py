import calendar

if __name__ == "__main__":
    week_days = {
        calendar.MONDAY: "MONDAY",
        calendar.TUESDAY: "TUESDAY",
        calendar.WEDNESDAY: "WEDNESDAY",
        calendar.THURSDAY: "THURSDAY",
        calendar.FRIDAY: "FRIDAY",
        calendar.SATURDAY: "SATURDAY",
        calendar.SUNDAY: "SUNDAY"
    }

    month, day, year = map(int, input().split())
    print(week_days.get(calendar.weekday(year, month, day)))
