from voluptuous import PREVENT_EXTRA, Schema

output = Schema({"id": int, "token": str}, extra=PREVENT_EXTRA, required=True)
