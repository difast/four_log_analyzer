from core.parser import LogParser
from core.plugins import RustParser
import time

def benchmark():
    parser = LogParser()
    rust_parser = RustParser()
    
    # Python
    start = time.time()
    for entry in parser.parse_file("access.log", "nginx"):
        pass
    print(f"Python: {time.time() - start:.4f}s")
    
    # Rust
    start = time.time()
    with open("access.log") as f:
        for line in f:
            rust_parser.parse_nginx(line)
    print(f"Rust: {time.time() - start:.4f}s")

if __name__ == "__main__":
    benchmark()