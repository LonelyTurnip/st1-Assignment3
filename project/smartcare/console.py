"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare import data_store
from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment
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
    data_store = SmartCareDataStore()

    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)

    while True:
        print("\nSmartCare Menu")
        print("1. Register patient")
        print("2. Find patient")
        print("3. Register practitioner")
        print("4. Book appointment")
        print("5. Cancel appointment")
        print("6. List practitioner appointments")
        print("7. Exit")
        choice = input("Choose option: ").strip()

    #Register Patient
        if choice == "1":
            patient_id = input("Patient ID: ")
            patient_name = input("Patient Name: ")

            try:
                patients.register_patient(
                    patient_id,
                    patient_name,
                )
                print("Patient registered")

            except (ValueError, LookupError) as error:
                print(error)

    #Find Patient
        elif choice == "2":
            patient_id = input("Patient ID: ")

            try:
                patient = patients.find_patient(patient_id)

                print(f"ID: {patient.patient_id}")
                print(f"Name: {patient.name}")

            except (ValueError, LookupError) as error:
                print(error)

    #Register Practitioner
        elif choice == "3":
            practitioner_id = input("Practitioner ID: ")
            prac_name = input ("Practitioner Name: ")
            speciality = input ("Practitioner Speciality: ")
            try:
                practitioners.register_practitioner(
                    practitioner_id,
                    prac_name,
                    speciality,
                )
                print("Practitioner registered")
            except (ValueError, LookupError) as error:
                print(error)

    #Book Appointment
        elif choice == "4":
            appointment_id = input("Appointment ID: ")
            patient_id = input("Patient ID: ")
            practitioner_id = input("Practitioner ID: ")
            date_text = input("Date (YYYY-MM-DD HH:MM): ")

            try:
                appointment = appointments.book_appointment(
                    appointment_id,
                    patient_id,
                    practitioner_id,
                    parse_date_time(date_text),
                )

                print(format_appointment(appointment))

            except (ValueError, LookupError) as error:
                print(error)

    #Cancel Appointment
        elif choice == "5":
            appointment_id = input("Appointment ID: ")

            try:
                appointments.cancel_appointment(appointment_id)
                print("Appointment cancelled")

            except (ValueError, LookupError) as error:
                print(f"Error: {error}")


    #List Practitioners
        elif choice == "6":
            practitioner_id = input("Practitioner ID: ")

            try:
                results = appointments.list_practitioner_appointments(
                    practitioner_id
                )

                for appointment in results:
                    print(format_appointment(appointment))

            except (ValueError, LookupError) as error:
                print(f"Error: {error}")

    #Exit
        elif choice == "7":
            print("Exit")
            break

        else:
            print("Invalid Choice")