from django.core.exceptions import ValidationError


def validate_image(file_obj):
    """
    Validate the image.
    Args:
        file_obj(dict): the file data
    Returns
        (error): error if not valid image
    """
    filesize = file_obj.size
    megabyte_limit = 2.0
    extensions = {".jpg", ".png", ".gif", ".jpeg"}
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    if not any(file_obj.name.lower().endswith(key) for key in extensions):
        raise ValidationError("You can only upload image files")
