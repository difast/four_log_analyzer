from .models import LogEntry, NginxLog
from .analyzers import nginx, json_log
import json
from typing import Iterator

class LogParser:
    def __init__(self):
        self.parsers = {
            "nginx": nginx.parse,
            "json": json_log.parse
        }

    def parse_line(self, line: str, format: str) -> Optional[LogEntry]:
        try:
            return self.parsers[format](line)
        except (KeyError, json.JSONDecodeError):
            return None

    def parse_file(self, path: str, format: str) -> Iterator[LogEntry]:
        with open(path) as f:
            for line in f:
                if entry := self.parse_line(line, format):
                    yield entry