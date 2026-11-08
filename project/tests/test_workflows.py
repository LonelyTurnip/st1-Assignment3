from datetime import datetime
import pytest
from smartcare.data_store import SmartCareDataStore
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)
from smartcare.domain import AppointmentStatus


def test_list_practitioner_appointments() -> None:
    data_store = SmartCareDataStore()

    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    patient_service.register_patient("P1", "Alex")

    practitioner_service.register_practitioner(
        "D1",
        "Taylor",
        "General",
    )

    appointment1 = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 10, 1, 9),
    )

    appointment2 = appointment_service.book_appointment(
        "A2",
        "P1",
        "D1",
        datetime(2026, 10, 1, 10),
    )

    results = appointment_service.list_practitioner_appointments(
        "D1",
    )

    assert results == [appointment1, appointment2]

def test_list_practitioner_unknown() -> None:
    data_store = SmartCareDataStore()

    appointment_service = AppointmentService(data_store)

    with pytest.raises(LookupError):
        appointment_service.list_practitioner_appointments(
            "UNKNOWN",
        )

def test_list_practitioner_no_matches() -> None:
    data_store = SmartCareDataStore()

    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    practitioner_service.register_practitioner(
        "D1",
        "Taylor",
        "General",
    )

    results = appointment_service.list_practitioner_appointments(
        "D1",
    )

    assert results == []

def test_list_practitioner_appointments_by_status() -> None:
    data_store = SmartCareDataStore()

    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    patient_service.register_patient("P1", "Alex")

    practitioner_service.register_practitioner(
        "D1",
        "Taylor",
        "General",
    )

    scheduled = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 10, 1, 9),
    )

    cancelled = appointment_service.book_appointment(
        "A2",
        "P1",
        "D1",
        datetime(2026, 10, 1, 10),
    )

    appointment_service.cancel_appointment("A2")

    results = appointment_service.list_practitioner_appointments(
        "D1",
        AppointmentStatus.CANCELLED,
    )

    assert results == [cancelled]

def test_cancelled_appointments_remain_listable() -> None:
    data_store = SmartCareDataStore()

    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    patient_service.register_patient(
        "P1",
        "Alex",
    )

    practitioner_service.register_practitioner(
        "D1",
        "Taylor",
        "General",
    )

    appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 10, 1, 9),
    )

    appointment_service.cancel_appointment("A1")

    results = appointment_service.list_practitioner_appointments(
        "D1",
    )

    assert len(results) == 1
    assert results[0].appointment_id == "A1"
    assert results[0].status == AppointmentStatus.CANCELLED

def test_list_practitioner_invalid_status() -> None:
    data_store = SmartCareDataStore()

    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    practitioner_service.register_practitioner(
        "D1",
        "Taylor",
        "General",
    )

    with pytest.raises(ValueError):
        appointment_service.list_practitioner_appointments(
            "D1",
            "INVALID",
        )

