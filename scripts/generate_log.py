import os
from datetime import datetime

def create_daily_log():
    # Define log directory and file
    log_dir = "daily_logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # File format: YYYY-MM-DD.txt
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(log_dir, f"{today}.txt")
    
    # Check if log already exists
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write(f"# Daily Activity Log for {today}\n\n")
            f.write("## Activities:\n- [ ] Task 1\n- [ ] Task 2\n\n")
        print(f"Log created: {log_file}")
    else:
        print(f"Log already exists: {log_file}")

if __name__ == "__main__":
    create_daily_log()
