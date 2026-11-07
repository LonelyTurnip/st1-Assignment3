"""Adding in the tests to check the broken functionality of the find_appointment method 
and the has_practitioner_conflict method in the data_store.py file."""

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

# Cancelled Appointment Tests
def test_cancelled_appointment_remains_findable() -> None:
    data_store = SmartCareDataStore()
    PatientService(data_store).register_patient('P1', 'Alex Example')
    PractitionerService(data_store).register_practitioner(
        'D1', 'Taylor Example', 'General',
    )
    appointment_service = AppointmentService(data_store)
    appointment = appointment_service.book_appointment(
        'A1', 'P1', 'D1', datetime(2026, 10, 1, 9),
    )

    appointment_service.cancel_appointment('A1')

    assert data_store.find_appointment('A1') is appointment
    assert appointment.status == AppointmentStatus.CANCELLED
    assert appointment in data_store.list_appointments()


# Practitoner Conflict Tests
def test_same_practitioner_same_time_conflicts_but_other_does_not() -> None:
    data_store = SmartCareDataStore()
    PatientService(data_store).register_patient('P1', 'Alex Example')
    practitioners = PractitionerService(data_store)
    practitioners.register_practitioner('D1', 'Taylor Example', 'General')
    practitioners.register_practitioner('D2', 'Morgan Example', 'General')
    appointment_service = AppointmentService(data_store)
    when = datetime(2026, 10, 1, 9)
    original = appointment_service.book_appointment('A1', 'P1', 'D1', when)

    # Store level: conflict only for the same practitioner at the same time.
    assert data_store.has_practitioner_conflict('D1', when) is True
    assert data_store.has_practitioner_conflict('D2', when) is False
    assert data_store.has_practitioner_conflict(
        'D1', datetime(2026, 10, 1, 10),
    ) is False

    # Service level: the conflicting booking is rejected, state unchanged.
    with pytest.raises(ValueError, match='already has a SCHEDULED'):
        appointment_service.book_appointment('A2', 'P1', 'D1', when)
    assert data_store.list_appointments() == [original]

    # A different practitioner at the same time is allowed.
    other = appointment_service.book_appointment('A3', 'P1', 'D2', when)
    assert other.practitioner.practitioner_id == 'D2'

# Failed Test evidence
"""
FAILED tests/test_regression.py::test_cancelled_appointment_remains_findable - AssertionError: assert None is <smartcare.domain.Appointment object at 0x00000175803D9A90>
 +  where None = find_appointment('A1')
 +    where find_appointment = <smartcare.data_store.SmartCareDataStore object at 0x00000175803D8EC0>.find_appointment
FAILED tests/test_regression.py::test_same_practitioner_same_time_conflicts_but_other_does_not - AssertionError: assert False is True
 +  where False = has_practitioner_conflict('D1', datetime.datetime(2026, 10, 1, 9, 0))
 +    where has_practitioner_conflict = <smartcare.data_store.SmartCareDataStore object at 0x00000175802C91D0>.has_practitioner_conflict
 """