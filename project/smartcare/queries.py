"""Stage 9 contracts for pure collection processing."""


from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus


def appointment_sort_key(appointment: Appointment) -> tuple[datetime, str]:
    """Return the date/time and appointment ID ordering key without side
    effects.
    """
    return (appointment.date_time,
            appointment.appointment_id,)
    # raise NotImplementedError('Stage 9: named sorting key')


def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
)-> list[Appointment]:
    """Return a new list for this practitioner, optionally filtered by
    status.

    Order by date/time then appointment ID using appointment_sort_key.
    Do not mutate the source list/objects or perform input/output.
    """

    filtered = []

    for appointment in appointments:
        if appointment.practitioner.practitioner_id != practitioner_id:
            continue

        if status is not None and appointment.status is not status:
            continue

        filtered.append(appointment)

    return sorted(filtered, key=appointment_sort_key)

    # raise NotImplementedError('Stage 9: pure query')
