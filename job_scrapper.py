import requests
from bs4 import BeautifulSoup

url = "https://www.seek.co.nz/python-jobs?salaryrange=100000-999999&salarytype=annual"


def has_data_search(tag):
    return tag.has_attr("data-search-sol-meta")


if __name__ == "__main__":
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(has_data_search)

    for job in results:
        try:
            titleElement = job.find("a", attrs={"data-automation": "jobTitle"})
            title = titleElement.get_text()
            company = job.find("a", attrs={"data-automation": "jobCompany"}).get_text()
            jobLink = "https://www.seek.co.nz" + titleElement["href"]
            salary = job.find("span", attrs={"data-automation": "jobSalary"})
            salary = salary.get_text() if salary else 'n/a'
            job = "Titulo: {}\nEmpresa: {}\nSalario: {}\nLink: {}a\n"
            job = job.format(title, company, salary, jobLink)
            print(job)
        except Exception as e:
            print("Exception: {}".format(e))
            pass
