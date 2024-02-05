from glob import glob
from pathlib import Path
import sys
import os  
from prog_prompts import Messages
import json 

@staticmethod
class UtilsIO:
    def files_with_ext(path: str, ext: str) -> list:
        return glob(f"{path}/*.{ext}")
    
    def _json_to_file(dst_path: Path, data: dict) -> None:
        with open(dst_path, mode = "w") as f:
            json.dump(data, f)

    def check_file_exists(file_path: Path) -> bool:
        if not Path.exists(file_path):
            Messages.format_msg(f"The file path provided does not exist! {file_path}", type="error")
            return False
        
        return True
    

    def json_to_file(dst_path: Path, file_name: str, data: dict ) -> None:
        file_path = Path(dst_path, file_name)
        if not UtilsIO.check_file_exists(file_path):
            return False
        try:
            UtilsIO._json_to_file(file_path, data)
        except PermissionError:
           Messages.format_msg(f"Permission error: orccured Cannot write to {file_path}", type="error")
           return False

        except FileNotFoundError:
           Messages.format_msg(f"File not found: {file_path}", type="error")
           return False

        except json.JSONDecodeError:
            Messages.format_msg(f"JSON decode error: {file_path}", type="error")
            return False

        except OSError as os_error:
            Messages.format_msg(f"OS error: {os_error}", type="error")
            return False

        except Exception as e:
            Messages.format_msg(f"An error occurred: {e}", type="error")
            return False
        
        return True

    def update_json(json_name:str, data: dict):
        if not UtilsIO.check_file_exists(json_name):
            return False
        
        try:
            orig_data = {}
            with open(json_name, "r") as f:
                orig_data = json.load(f)

        except Exception as e:
            Messages.format_msg(f"An error occurred: {e}", type="error")
            return False
        
        orig_data.update(data)
        UtilsIO.json_to_file(json_name, orig_data)
        
        

    
@staticmethod
class StartUp:
    def start_script():
        prog_dir = Path(sys.argv[0]).parent.absolute()
        config = Path(prog_dir, "config")
        # prog_dir [0], config [1]
        return (prog_dir, config)
    
    def config_check(config: Path):
        if not Path.exists(config):
            Messages.handle_no_config()
            os.makedirs(config)
            return False
        
        if not Path.exists(config, "app_data"):
            os.mkdir(Path(config, "app_data"))

        return True
    
    def get_configs(config: Path):
        return UtilsIO.files_with_ext(config, "json")
    

    def _make_app_data(app_data: Path):
        UtilsIO.json_to_file(app_data, "user_paths.json", {})

        
