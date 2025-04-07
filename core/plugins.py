from pyo3 import PyO3, Python
from .models import LogEntry

class RustParser:
    def __init__(self):
        self.rust_module = PyO3::import("log_parser_rs")?  # Импорт Rust-модуля

    def parse_nginx(self, line: str) -> Optional[LogEntry]:
        with Python::acquire_gil() as py:
            try:
                result = self.rust_module.parse_nginx_log(line)
                return LogEntry(**result)
            except Exception:
                return None