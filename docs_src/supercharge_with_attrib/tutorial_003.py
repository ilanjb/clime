import attr

from clime import clime

import datetime


def year_month_day_to_date(year_month_day) -> datetime.date:
    """
    '2000-11-22' ->
    :param year_month_day:
    :return:
    """
    return datetime.datetime.strptime(year_month_day, "%Y-%m-%d").date()


@attr.s
class Dude:
    birthday: datetime.date = attr.ib(converter=year_month_day_to_date)
    # attributes with explicity converters will be taken with argument parser as strings
    # you can do whatver you want with them!

    def print_my_birthday(self):
        print(f"My birthday is {self.birthday}")


def main():
    clime(Dude).print_my_birthday()


if __name__ == "__main__":
    main()
