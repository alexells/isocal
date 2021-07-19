from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


# get the page contents

URL = "https://allocation.miq.govt.nz/portal/"
hdr = {"User-Agent": "Mozilla/5.0"}
req = Request(URL, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "html.parser")

results = soup.find(id="accommodation-calendar-home")


# assert the values on the page are consistent with no availability

expected_end_date = "2021-11-30"
expected_max_date = "2021-11-30"
expected_arrival_dates = "badvalue"

returned_end_date = results["data-end-date"]
returned_max_date = results["data-max-date"]
returned_arrival_dates = results["data-arrival-dates"]

assert (
    returned_end_date == expected_end_date
), f"New dates may be available to book! New data-end-date detected: {returned_end_date}"

assert (
    returned_max_date == expected_max_date
), f"New dates may be available to book! New data-max-date detected: {returned_max_date}"

assert (
    returned_arrival_dates == expected_arrival_dates
), f"New dates may be available to book! New data-arrival-dates detected: {returned_arrival_dates}"


# if the assertions all pass, print the values received

print(
    f"""
    Completed check with no unexpected values
    data-end-date={returned_end_date}
    data-max-date={returned_max_date}
    data-arrival-dates={returned_arrival_dates}
    """
)
