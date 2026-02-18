def individual_data(log):
    return {
        "id": str(log["_id"]),
        "title": log["status"],
        "created_at": log["created_at"],
    }

def all_logs(logs):
    return [individual_data(log) for log in logs]
