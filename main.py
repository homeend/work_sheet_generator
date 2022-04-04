import datetime


def main(week_offset: int = 0):
    today = datetime.datetime.now()
    today += datetime.timedelta(weeks=week_offset)
    offset_to_week_begin = datetime.timedelta(days=today.weekday())
    week_begin = today - offset_to_week_begin
    week_end = today - offset_to_week_begin + datetime.timedelta(days=4)
    template = f"""
Timesheet:
Pay period: {week_begin:%d/%m/%Y} - {week_end:%d/%m/%Y}
{week_begin:%d/%m/%Y}: xx:00-xx:00 (CET) - xx hours
{week_begin + datetime.timedelta(days=1):%d/%m/%Y}: xx:00-xx:00 (CET) - xx hours
{week_begin + datetime.timedelta(days=2):%d/%m/%Y}: xx:00-xx:00 (CET) - xx hours
{week_begin + datetime.timedelta(days=3):%d/%m/%Y}: xx:00-xx:00 (CET) - xx hours
{week_begin + datetime.timedelta(days=4):%d/%m/%Y}: xx:00-xx:00 (CET) - xx hours
    """
    print(template)


if __name__ == "__main__":
    print("-" * 10)
    main(-1)
    print("-" * 10)
    main()
    print("-" * 10)
    main(1)
