from datetime import datetime
import re


def get_non_empty_input(prompt):
    user_response = input(prompt).strip()
    if user_response:
        return user_response
    print("Ce champ ne peut être vide.")
    return get_non_empty_input(prompt)


def get_valid_date_format(prompt):
    date_str = get_non_empty_input(prompt)
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print("Format date invalide. Entrez une date valide (01-01-2021).")
        return get_valid_date_format(prompt)


def get_valid_float(prompt):
    while True:
        float_str = get_non_empty_input(prompt)
        try:
            value = float(float_str)
            if value >= 0:
                return value
            print("Le nombre doit être suppèrieur ou égale à zéro.")
        except ValueError:
            print("Invalide: Veuillez entrer un nombre valide.")


def get_valid_national_id_format(prompt):
    pattern = re.compile(r"[A-Z]{2}\d{5}$")
    national_id = get_non_empty_input(prompt)
    if pattern.match(national_id):
        return national_id
    print("Invalide format nationnal ID. Veuillez entrer un ID valide (AB12345).")
    return get_valid_national_id_format(prompt)
