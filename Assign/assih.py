
company = {
    "Engineering": {
        "employees": [
            ("E101", "Alice", ["Python", "ML"]),
            ("E102", "Bob", ["Java", "Cloud"])
        ],
        "sub_departments": {
            "AI": {
                "employees": [
                    ("E201", "Charlie", ["Python", "Deep Learning"]),
                    ("E202", "David", ["Python", "ML"])
                ],
                "sub_departments": {}
            }
        }
    },

    "HR": {
        "employees": [
            ("E301", "Eve", ["Communication"]),
            ("E302", "Frank", ["Recruitment", "Management"])
        ],
        "sub_departments": {}
    }
}
def process_skills(skills, index, unique_skills, skill_count):
    if index == len(skills):
        return

    skill = skills[index]

    unique_skills.add(skill)
    skill_count[skill] = skill_count.get(skill, 0) + 1

    process_skills(skills, index + 1, unique_skills, skill_count)
def process_employees(emp_list, index, result):
    if index == len(emp_list):
        return

    emp_id, name, skills = emp_list[index]

    result["total_employees"] += 1

    process_skills(skills, 0, result["unique_skills"], result["skill_count"])

    if len(skills) > result["max_skill_count"]:
        result["max_skill_count"] = len(skills)
        result["max_skill_employee"] = (emp_id, name)

    process_employees(emp_list, index + 1, result)
def traverse_departments(dept_names, dept_data, index, result):
    if index == len(dept_names):
        return

    dept = dept_names[index]

    process_employees(dept_data[dept]["employees"], 0, result)

    sub_depts = dept_data[dept]["sub_departments"]
    sub_names = list(sub_depts.keys())

    traverse_departments(sub_names, sub_depts, 0, result)

    traverse_departments(dept_names, dept_data, index + 1, result)

def analyse_company(data):
    result = {
        "total_employees": 0,
        "unique_skills": set(),
        "skill_count": {},
        "max_skill_employee": (),
        "max_skill_count": 0
    }

    dept_names = list(data.keys())

    traverse_departments(dept_names, data, 0, result)

    del result["max_skill_count"]

    return result

def search_employee_skill(emp_list, index, skill, answer):
    if index == len(emp_list):
        return

    emp_id, name, skills = emp_list[index]

    if skill in skills:
        answer.append((emp_id, name))

    search_employee_skill(emp_list, index + 1, skill, answer)


def search_departments(dept_names, dept_data, index, skill, answer):
    if index == len(dept_names):
        return

    dept = dept_names[index]

    search_employee_skill(dept_data[dept]["employees"], 0, skill, answer)

    sub_depts = dept_data[dept]["sub_departments"]
    sub_names = list(sub_depts.keys())

    search_departments(sub_names, sub_depts, 0, skill, answer)

    search_departments(dept_names, dept_data, index + 1, skill, answer)


def find_employees_with_skill(data, skill):
    answer = []

    dept_names = list(data.keys())

    search_departments(dept_names, data, 0, skill, answer)

    return answer


print("PART A")
print(analyse_company(company))

print("\nPART B")
print(find_employees_with_skill(company,"Python"))
