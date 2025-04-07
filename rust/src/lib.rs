use pyo3::prelude::*;
use regex::Regex;
use serde_json::{Value, Map};

#[pyfunction]
fn parse_nginx_log(line: &str) -> PyResult<Map<String, Value>> {
    let re = Regex::new(r#"(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>.+?)\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d+) \S+ "(?P<response_time>[\d.]+)""#)?;
    
    let caps = re.captures(line).ok_or("Invalid log format")?;
    let mut result = Map::new();
    
    result.insert("ip".to_string(), Value::String(caps["ip"].to_string()));
    result.insert("method".to_string(), Value::String(caps["method"].to_string()));
    // ... остальные поля
    
    Ok(result)
}

#[pymodule]
fn log_parser_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_nginx_log, m)?)?;
    Ok(())
}