from pathlib import Path
import yaml


def get_yaml_dir() -> Path:
    return Path(__file__).parent / 'yaml_test_case'


def load_yaml(yaml_file: Path) -> dict:
    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)
