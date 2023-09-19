import logging
from individual_lessons.models import IndividualStudent, IndividualLesson
from pyzoom import oauth_wizard
import requests


auth_token_url = "https://zoom.us/oauth/token"
api_base_url = "https://api.zoom.us/v2"


def create_meeting(student: IndividualStudent, lesson: IndividualLesson):
    topic = f"Занятие с {student.first_name}"
    duration = "30"
    start_date = lesson.date.isoformat()
    start_time = lesson.time.isoformat()
    data = {
        "grant_type": "account_credentials",
        "account_id": student.teacher.zoom_key,
        "client_secret": student.teacher.zoom_sec,
    }
    response = requests.post(
        auth_token_url,
        auth=(student.teacher.zoom_client, student.teacher.zoom_sec),
        data=data,
    )

    if response.status_code != 200:
        logging.warning("Unable to get access token")
    response_data = response.json()
    access_token = response_data["access_token"]

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "topic": topic,
        "duration": duration,
        "start_time": f"{start_date}T{start_time}",
        "type": 2,
    }

    resp = requests.post(
        f"{api_base_url}/users/me/meetings", headers=headers, json=payload
    )

    if resp.status_code != 201:
        logging.warning("Unable to generate meeting link")
        return None
    response_data = resp.json()

    logging.warning(f"{response_data=}")

    content = {
        "id": response_data["uuid"],
        "meeting_url": response_data["join_url"],
        "password": response_data["password"],
        "meetingTime": response_data["start_time"],
        "purpose": response_data["topic"],
        "duration": response_data["duration"],
        "message": "Success",
        "status": 1,
    }

    return content


def delete_meeting(student: IndividualStudent, lesson: IndividualLesson):
    data = {
        "grant_type": "client_credentials",
        "account_id": student.teacher.zoom_key,
        "client_secret": student.teacher.zoom_sec,
    }
    response = requests.post(auth_token_url,
                             auth=(student.teacher.zoom_client, student.teacher.zoom_sec),
                             data=data)

    if response.status_code != 200:
        logging.warning("Unable to get access token")
        return False
    response_data = response.json()
    access_token = response_data["access_token"]

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    resp = requests.delete(f"{api_base_url}/meetings/{lesson.zoom_id}", headers=headers)

    if resp.status_code != 204:
        logging.warning(f'{resp.json()=}')
        return False

    return True
