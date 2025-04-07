import re
from datetime import datetime
from ..models import NginxLog

NGINX_REGEX = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>.+?)\] '
    r'"(?P<method>\S+) (?P<path>\S+) \S+" '
    r'(?P<status>\d+) \S+ "(?P<response_time>[\d.]+)"'
)

def parse(line: str) -> NginxLog:
    match = NGINX_REGEX.match(line)
    if not match:
        raise ValueError("Invalid Nginx log format")
    
    return NginxLog(
        timestamp=datetime.strptime(match.group("timestamp"), "%d/%b/%Y:%H:%M:%S %z"),
        message=line.strip(),
        metadata={},
        source="nginx",
        method=match.group("method"),
        path=match.group("path"),
        status_code=int(match.group("status")),
        response_time=float(match.group("response_time"))
    )