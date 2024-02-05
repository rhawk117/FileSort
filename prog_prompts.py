

@staticmethod
class Messages:
    def format_msg(msg: str, type: str) -> None:
        prefix = "[i]"
        if type == "error":
          prefix = "[!]"
        elif type == "warning":
          prefix = "[*]"
        elif type == "success":
          prefix = "[+]"
        elif type == "info":
          prefix = "[i]"
        else:
            prefix = ""

        print(f"{prefix} {msg} {prefix}".center(60, "-"))

    def no_config():
       Messages.format_msg("No config directory found", type="warning")
      
    def no_app_data():
       Messages.format_msg("""
        The app data directory was not found upon program start up 
        it has been created along with some configuration .json files
        to improve user experience
      """, type="warning")
    