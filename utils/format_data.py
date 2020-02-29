def get_bytes_size(bytes):
    """
        Returns size of bytes in a nice format
    """
    byte_format_list = ["", "K", "M", "G", "T", "P"]
    for unit in byte_format_list:
        if bytes < 1024:
            return "{bytes:.2f}{unit}B".format(bytes=bytes, unit=unit)
        bytes = bytes / 1024

