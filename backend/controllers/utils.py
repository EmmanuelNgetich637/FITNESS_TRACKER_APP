# Example utility function for validation or common helpers

def validate_required_fields(data, fields):
    missing = [field for field in fields if field not in data]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    return True, ""
