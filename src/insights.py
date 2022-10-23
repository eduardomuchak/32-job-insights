from src.jobs import read


def get_unique_job_types(path):
    content = read(path)
    job_types = set()
    for job in content:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    content = read(path)
    industries = set()
    for job in content:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    content = read(path)
    max_salary = []
    for job in content:
        if job["max_salary"].isdigit():
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    content = read(path)
    min_salary = []
    for job in content:
        if job["min_salary"].isdigit():
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Job does not have min_salary or max_salary")

    is_min_salary_a_integer = type(job["min_salary"]) is int
    is_max_salary_a_integer = type(job["max_salary"]) is int

    if not is_min_salary_a_integer or not is_max_salary_a_integer:
        raise ValueError("Job does not have min_salary or max_salary")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")

    if type(salary) != int:
        raise ValueError("Salary is not an integer")

    return True if job["min_salary"] <= salary <= job["max_salary"] else False


def filter_by_salary_range(jobs, salary):
    content = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                content.append(job)
        except ValueError:
            print("Job does not have min_salary or max_salary")
    return content
