# Web Server Log Attack Detector - Developed by Umutcan Korkmaz

def analyze_web_logs(log_data):
    # Yaygın web saldırı vektörleri
    attack_vectors = {
        "SQL Injection": ["'", "--", "UNION", "SELECT"],
        "Path Traversal": ["../", "..%2f", "etc/passwd"],
        "XSS": ["<script>", "alert(", "onload="]
    }
    
    for attack_type, signatures in attack_vectors.items():
        for sig in signatures:
            if sig in log_data:
                print(f"[DETECTED] {attack_type} attempt found! Signature: {sig}")

# Örnek kirli log satırı
sample_log = "GET /products.php?id=10' OR '1'='1' HTTP/1.1"
analyze_web_logs(sample_log)
