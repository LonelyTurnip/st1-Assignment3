"""Adding in the TODOs that are not called in the test_starter.py file."""

# imports
from datetime import datetime
import pytest
from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

# Lookup Tests

# Patient tests
def test_find_patient_unknown_id() -> None:
    """Verifying that a LookupError is raised for an unknown patient ID."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    with pytest.raises(LookupError):
        patient_service.find_patient('unknown_id')

def test_find_patient_blank_id() -> None:
    """Verifying that a ValueError is raised for a blank patient ID."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    with pytest.raises(ValueError):
        patient_service.find_patient('')

def test_find_patient_invalid_id() -> None:
    """Verifying that a ValueError is raised for a invalid patient ID."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    with pytest.raises(ValueError):
        patient_service.find_patient(5)

def test_find_patient_valid_id() -> None:
    """Verifying that a valid patient ID returns the correct patient."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    patient = patient_service.register_patient('P1', 'Alex Example')
    found_patient = patient_service.find_patient('P1')
    assert found_patient is patient
    assert found_patient.patient_id == 'P1'
    assert found_patient.name == 'Alex Example'

# Practitioner Tests

def test_find_practitioner_unknown_id() -> None:
    """Verifying that a LookupError is raised for an unknown practitioner ID."""
    data_store = SmartCareDataStore()
    practitioner_service = PractitionerService(data_store)
    with pytest.raises(LookupError):
        practitioner_service.find_practitioner('unknown_id')

def test_find_practitioner_blank_id() -> None:
    """Verifying that a ValueError is raised for a blank practitioner ID."""
    data_store = SmartCareDataStore()
    practitioner_service = PractitionerService(data_store)
    with pytest.raises(ValueError):
        practitioner_service.find_practitioner('')

def test_find_practitioner_invalid_id() -> None:
    """Verifying that a ValueError is raised for a invalid practitioner ID."""
    data_store = SmartCareDataStore()
    practitioner_service = PractitionerService(data_store)
    with pytest.raises(ValueError):
        practitioner_service.find_practitioner(5)

def test_find_practitioner_valid_id() -> None:
    """Verifying that a valid practitioner ID returns the correct practitioner."""
    data_store = SmartCareDataStore()
    practitioner_service = PractitionerService(data_store)
    practitioner = practitioner_service.register_practitioner('P1', 'Alex Example', 'General')
    found_practitioner = practitioner_service.find_practitioner('P1')
    assert found_practitioner is practitioner
    assert found_practitioner.practitioner_id == 'P1'
    assert found_practitioner.name == 'Alex Example'

# Cancel appointment tests

def test_cancel_appointment() -> None:
    """Verifying that an appointment can be cancelled."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    patient_service.register_patient('p1', 'Alex Example')
    practitioner_service.register_practitioner('d1', 'Taylor Example', 'General')
    appointment = appointment_service.book_appointment(
        'a1',
        'p1',
        'd1',
        datetime(2026, 10, 1, 9),
    )
    result = appointment_service.cancel_appointment('a1')
    assert result is appointment
    assert appointment_service.find_appointment('a1') is appointment
    assert appointment.status == AppointmentStatus.CANCELLED

def test_cancel_appointment_unknown_id() -> None:
    """Verifying that a LookupError is raised for an unknown appointment ID."""
    data_store = SmartCareDataStore()
    appointment_service = AppointmentService(data_store)
    with pytest.raises(LookupError):
        appointment_service.cancel_appointment('unknown_id')

def test_repeat_cancel_appointment() -> None:
    """Verifying that canceling an already cancelled appointment raises a ValueError."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)
    patient_service.register_patient('p1', 'Alex Example')
    practitioner_service.register_practitioner('d1', 'Taylor Example', 'General')
    appointment = appointment_service.book_appointment(
        'a1',
        'p1',
        'd1',
        datetime(2026, 10, 1, 9),
    )
    appointment_service.cancel_appointment('a1')
    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('a1')
    assert appointment.status == AppointmentStatus.CANCELLED