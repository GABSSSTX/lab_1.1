from persistence.hash_table import HashTable
from persistence.record_store import append_record, read_all


class ProfileRepository:

    def __init__(self):
        self.index = HashTable()
        self._rebuild_index()

    
    def _rebuild_index(self):
        records = read_all()

        offset = 0
        for r in records:
            key = r["key"]
            self.index.put(key, offset)
            offset += 1

    def save_profile(self, player_id, profile):

        record = {
            "type": "profile",
            "key": f"player:{player_id}",
            "data": profile
        }

        offset = append_record(record)
        self.index.put(record["key"], offset)

    def get_profile(self, player_id):
        key = f"player:{player_id}"
        offset = self.index.get(key)

        if offset is None:
            return None

        records = read_all()
        return records[offset]["data"]