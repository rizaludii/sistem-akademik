def to_minutes(time_str: str) -> int:
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


def is_overlap(a_start, a_end, b_start, b_end) -> bool:
    return a_start < b_end and b_start < a_end


def detect_schedule_conflict(jadwals: list):
    """
    Input  : list of Jadwal objects
    Output : list of conflict dict
    """
    conflicts = []

    for i in range(len(jadwals)):
        for j in range(i + 1, len(jadwals)):
            a = jadwals[i]
            b = jadwals[j]

            # Hari harus sama
            if a.hari != b.hari:
                continue

            a_start = to_minutes(a.jam_mulai)
            a_end   = to_minutes(a.jam_selesai)
            b_start = to_minutes(b.jam_mulai)
            b_end   = to_minutes(b.jam_selesai)

            # Tidak overlap waktu
            if not is_overlap(a_start, a_end, b_start, b_end):
                continue

            # Konflik ruangan
            if a.ruangan_id == b.ruangan_id:
                conflicts.append({
                    "type": "room_conflict",
                    "affected_schedules": [a.id, b.id]
                })

            # Konflik dosen
            if a.dosen == b.dosen:
                conflicts.append({
                    "type": "lecturer_conflict",
                    "affected_schedules": [a.id, b.id]
                })

            # Overlap waktu umum
            conflicts.append({
                "type": "time_overlap",
                "affected_schedules": [a.id, b.id]
            })

    return conflicts
