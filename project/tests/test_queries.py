from datetime import datetime
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.queries import appointment_sort_key
from smartcare.queries import select_appointments


def test_appointment_sort_key() -> None:
    patient = Patient("P1", "Alex")
    practitioner = Practitioner(
        "D1",
        "Taylor",
        "General",
    )

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 10, 1, 9),
        AppointmentStatus.SCHEDULED,
    )

    assert appointment_sort_key(appointment) == (
        datetime(2026, 10, 1, 9),
        "A1",
    )

def test_select_appointments_by_practitioner() -> None:
    patient = Patient("P1", "Alex")

    dr1 = Practitioner("D1", "Taylor", "General")
    dr2 = Practitioner("D2", "Morgan", "General")

    appointment1 = Appointment(
        "A1",
        patient,
        dr1,
        datetime(2026, 10, 1, 9),
    )

    appointment2 = Appointment(
        "A2",
        patient,
        dr2,
        datetime(2026, 10, 1, 10),
    )

    results = select_appointments(
        [appointment1, appointment2],
        "D1",
    )

    assert results == [appointment1]

def test_select_appointments_by_status() -> None:
    patient = Patient("P1", "Alex")
    practitioner = Practitioner(
        "D1",
        "Taylor",
        "General",
    )

    scheduled = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 10, 1, 9),
    )

    cancelled = Appointment(
        "A2",
        patient,
        practitioner,
        datetime(2026, 10, 1, 10),
    )

    cancelled.cancel()

    results = select_appointments(
        [scheduled, cancelled],
        "D1",
        AppointmentStatus.CANCELLED,
    )

    assert results == [cancelled]

def test_select_appointments_sorted_by_time_then_id() -> None:
    patient = Patient("P1", "Alex")

    practitioner = Practitioner(
        "D1",
        "Taylor",
        "General",
    )

    a2 = Appointment(
        "A2",
        patient,
        practitioner,
        datetime(2026, 10, 1, 9),
    )

    a1 = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 10, 1, 9),
    )

    a3 = Appointment(
        "A3",
        patient,
        practitioner,
        datetime(2026, 10, 1, 10),
    )

    results = select_appointments(
        [a3, a2, a1],
        "D1",
    )

    assert results == [a1, a2, a3]

def test_select_appointments_does_not_modify_source() -> None:
    patient = Patient("P1", "Alex")

    practitioner = Practitioner(
        "D1",
        "Taylor",
        "General",
    )

    appointment1 = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 10, 1, 10),
    )

    appointment2 = Appointment(
        "A2",
        patient,
        practitioner,
        datetime(2026, 10, 1, 9),
    )

    appointments = [appointment1, appointment2]

    before = list(appointments)

    select_appointments(
        appointments,
        "D1",
    )

    assert appointments == before

def test_select_appointments_empty_result() -> None:
    patient = Patient("P1", "Alex")

    practitioner = Practitioner(
        "D1",
        "Taylor",
        "General",
    )

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 10, 1, 9),
    )

    results = select_appointments(
        [appointment],
        "D2",
    )

    assert results == []