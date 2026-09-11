
ALLOWED_FILES = {
    "VIDEO": {
        "extensions": {".mp4", ".mov", ".webm"},
        "mime_types": {"video/mp4", "video/quicktime", "video/webm"},
        "max_size": 500 * 1024 * 1024  # 500 MB
    },
    "DOCUMENT": {
        "extensions": {".pdf", ".docx", ".txt"},
        "mime_types": {"application/pdf", "application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/vnd.ms-powerpoint"},
        "max_size": 25 * 1024 * 1024  # 25 MB
    },
}

def validate_extension(filename, content_type):
    ("product", "mp4")
    extension = os.path.splitext(filename)[1].lower()

    allowed_extensions = ALLOWED_FILES[content_type]["extensions"]

    if extension not in allowed_extensions:
        return False, (
            f"unsupported file extension '{extension}',",
            f"Allowed extension '{allowed_extension}"
        )
        return True, None

def validate_file(file, content_type):
    if content_type not in ALLOWED_FILES:
        return False, "Unsupported content type."
    if not file.filename:
        return False, "Filename is required."

    valid, error = validate_extension(file.filename, content_type)
    if not valid:
        return False, error

    valid, error = validate_mimetype(file, content_type)
    if not valid:
        return False, error