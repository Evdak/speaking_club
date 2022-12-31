import decimal
import hashlib
from urllib import parse
from speaking_club.settings import ALLOWED_HOSTS, ROBOKASSA_PASSWORD1
from django import forms
from robokassa.forms import SuccessRedirectForm


MAX_SCORE = {
    "nav-Writing": 16,
    "nav-Listening": 15,
    "nav-Vocabulary": 20,
    "nav-Grammar": 34,
    "nav-Reading": 16
}


def define_levels(
    grammar: int,
    listening: int,
    writing: int,
    reading: int,
    vocabulary: int
):
    if 0 <= grammar <= 13:
        grammar = 'A1'
    elif 14 <= grammar <= 27:
        grammar = 'A2'
    elif 28 <= grammar:
        grammar = 'B1'

    if 0 <= listening <= 6:
        listening = 'A1'
    elif 7 <= listening <= 11:
        listening = 'A2'
    elif 12 <= listening:
        listening = 'B1'

    if 0 <= writing <= 6:
        writing = 'A1'
    elif 7 <= writing <= 12:
        writing = 'A2'
    elif 13 <= writing:
        writing = 'B1'

    if 0 <= reading <= 5:
        reading = 'A1'
    elif 6 <= reading <= 12:
        reading = 'A2'
    elif 13 <= reading:
        reading = 'B1'

    if 0 <= vocabulary <= 7:
        vocabulary = 'A1'
    elif 8 <= vocabulary <= 15:
        vocabulary = 'A2'
    elif 16 <= vocabulary:
        vocabulary = 'B1'

    return {
        "grammar": grammar,
        "listening": listening,
        "writing": writing,
        "reading": reading,
        "vocabulary": vocabulary,
    }


def define_total_level(grammar: str, listening: str, writing: str, reading: str, vocabulary: str):
    if (grammar == "A1") and (vocabulary == "A1"):
        return {
            "total": "A1"
        }

    if (grammar == "A1") and (vocabulary == "A2" or vocabulary == "B1") and listening == "A1":
        return {
            "total": "A1"
        }

    if (grammar == "A1") and (vocabulary == "A2" or vocabulary == "B1") and (listening == "A2" or listening == "B1"):
        return {
            "total": "A2"
        }

    if (grammar == "A2") and (vocabulary == "A2" or vocabulary == "B1"):
        return {
            "total": "A2"
        }

    if (grammar == "A2") and (vocabulary == "A1") and listening == "A1":
        return {
            "total": "A1"
        }

    if (grammar == "A2") and (vocabulary == "A1") and (listening == "A2" or listening == "B1"):
        return {
            "total": "A2"
        }

    if (grammar == "B1") and (vocabulary == "A2" or vocabulary == "B1"):
        return {
            "total": "B1"
        }

    if (grammar == "B1") and (vocabulary == "A1"):
        return {
            "total": "A2"
        }


def generate_success_form(
    cost: decimal,  # Cost of goods, RU
    number: int,  # Invoice number
    host_url=ALLOWED_HOSTS[0],
) -> str:
    """URL for redirection of the customer to the service.
    """
    signature = calculate_signature(
        cost,
        number,
        ROBOKASSA_PASSWORD1,
    )

    data = {
        'OutSum': cost,
        'InvId': number,
        'SignatureValue': signature,
        "Culture": "ru"
    }

    return SuccessRedirectForm(data).as_table()


def calculate_signature(*args) -> str:
    """Create signature MD5.
    """
    return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()
