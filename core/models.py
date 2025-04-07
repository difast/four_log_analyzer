from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional, Union

class LogEntry(BaseModel):
    timestamp: datetime
    message: str
    metadata: Dict[str, Union[str, int, float]]
    source: str  # "nginx", "syslog", "json"

class NginxLog(LogEntry):
    method: str
    path: str
    status_code: int
    response_time: float

class AnalysisResult(BaseModel):
    total_entries: int
    errors_count: int
    avg_processing_time: float
    sources_distribution: Dict[str, int]