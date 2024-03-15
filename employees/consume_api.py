import requests


def job_converter(job_description):
    if job_description == "A+":
        return "Helpdesk"
    elif job_description == "A-" or job_description == "O+":
        return "Nurse"
    elif job_description == "B+":
        return "Janitor"
    elif job_description == "B-":
        return "Trainee"
    elif job_description == "O-":
        return "Doctor"
    elif job_description == "AB-":
        return "Security"

    return "unknown"


def create_staff(person):
    person_id = person['id']
    first_name = person['firstName']
    last_name = person['lastName']
    email = person['email']
    phone = person['phone']
    age = person['age']
    job_description = person['bloodGroup']
    job_description = job_converter(job_description)

    staff_member = {
                    "id": person_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "e_mail": email,
                    "phone": phone,
                    "age": age,
                    "profession": job_description,
                    }
    return staff_member


url = "https://dummyjson.com/users/"


def get_data():
    full_staff = []
    session = requests.Session()
    response = session.get(url)

    if response.status_code == 200:
        json_res = response.json()

        for person in json_res['users']:

            staff_member = create_staff(person)
            full_staff.append(staff_member)

        print("API CONSUMED", len(full_staff))
        return full_staff
    # TODO: write error return
    response.raise_for_status()
