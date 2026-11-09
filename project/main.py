"""Run the supplied demo or the Stage 9 interactive menu."""

#    python main.py --interactive
import argparse
import datetime

from smartcare.console import run_demo, run_menu, format_appointment, parse_date_time
from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import PatientService, PractitionerService, AppointmentService


def main() -> None:
    """Run the demo, or the interactive menu with --interactive."""
    parser = argparse.ArgumentParser(
        description='SmartCare teaching application',
    )
    parser.add_argument('--interactive', action='store_true')
    args = parser.parse_args()
    if args.interactive:
        run_menu()
    else:
        run_demo()
if __name__ == '__main__':
    main()

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
