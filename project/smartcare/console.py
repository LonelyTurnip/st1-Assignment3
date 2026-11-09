"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')


def run_menu() -> None:
    """Stage 9: implement the register/find/book/cancel/list/exit menu.

    Call services, recover from expected input errors, and keep this
    session's data until exit. main.py reports the incomplete menu
    without crashing.
    """

    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    appointment_service = AppointmentService(data_store)
    practitioner_service = PractitionerService(data_store)

    while True:
        print(f"=" * 60)
        print(f" " *22, f"SMARTCARE", f" " * 23)
        print(f" " * 17, f"Interactive Console", " " * 18)
        print(f"=" * 60)
        print("Session data is temporary and will be discarded when you exit.")
        print(" ")
        print(f"MAIN MENU")
        print(f"-" * 60)
        print(f"[1] Register patient")
        print(f"[2] Find patient")
        print(f"[3] Register practitioner")
        print(f"[4] Find practitioner")
        print(f"[5] Book Appointment")
        print(f"[6] Cancel appointment")
        print(f"[7] Find appointment")
        print(f"[8] List practitioner appointments")
        print(f"[0] Exit")

        response = input(str("Select an option:")).strip()

        try:
            if(response == "1"):
                patient_id = input(str("Patient ID: "))
                patient_name = input(str("Patient Name: "))
                patient_service.register_patient(patient_id, patient_name)
                print(f"Patient has been registered")
                print(f"Patient ID: {patient_id} \nName: {patient_name}")
            elif(response == "2"):
                patient_id = input(str("Patient ID: "))
                patient = patient_service.find_patient(patient_id)
                print(f"Patient found. {patient.patient_id}: {patient.name}")
            elif(response == "3"):
                practitioner_id = input(str("Practitioner ID: "))
                practitioner_name = input(str("Practitioner Name: "))
                practitioner_specialty = input(str("Practitioner Specialty: "))
                practitioner_service.register_practitioner(practitioner_id, practitioner_name, practitioner_specialty)
                print(f"Practitioner registered successfully")
                print(f"Practitioner ID: {practitioner_id} \n Practitioner name: {practitioner_name} \n Specialty: {practitioner_specialty}")
            elif(response == "4"):
                practitioner_id = input(str("Practitioner ID: "))
                practitioner = practitioner_service.find_practitioner(practitioner_id)
                print(f"Practitioner found. {practitioner.practitioner_id}: {practitioner.name}, {practitioner.specialty}")
            elif(response == "5"): 
                appointment_id = input(str("Appointment ID: "))
                patient_id = input(str("Patient ID:"))
                practitioner_id = input(str("Practitioner ID: "))
                date_time_input = input(str("Date/time [YYYY-MM-DD HH:MM]: "))
                date_time = parse_date_time(date_time_input)
                appointment = appointment_service.book_appointment(appointment_id, patient_id, practitioner_id, date_time)
                print(f"Appointment booked successfully.")
                print(format_appointment(appointment))
            elif(response == "6"):
                appointment_id = input(str("Appointment ID: "))
                appointment = appointment_service.find_appointment(appointment_id)
                appointment_service.cancel_appointment(appointment_id)
                print(f"Appointment cancelled successfully.")
                print(format_appointment(appointment))
            elif(response == "7"):
                appointment_id = input(str("Appointment ID: "))
                appointment = appointment_service.find_appointment(appointment_id)
                print(f"Appointment Found.")
                print(format_appointment(appointment))
            elif(response == "8"):
                practitioner_id = input(str("Practitioner ID: "))
                status_text = input(str("Status filter (blank for all): ")).strip()
                status = AppointmentStatus(status_text.lower()) if status_text else None
                results = appointment_service.list_practitioner_appointments(
                    practitioner_id, status,
                )
                if not results:
                    print(f"No appointments found for practitioner {practitioner_id}.")
                for appointment in results:
                    print(format_appointment(appointment))
            elif(response == "0"):
                print("Thank you for using SMARTCARE")
                break
            else:
                print("Invalid Response. Please Try Again")
        except (ValueError, LookupError) as error:
            print(f"Error: {error}")