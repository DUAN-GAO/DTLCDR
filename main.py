# main.py
import subprocess

def run_cmd(cmd):
    print(f"\n>>> Running: {cmd}\n")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}")

if __name__ == "__main__":
    run_cmd("python run_GCADTI.py --task training")
    run_cmd("python run_GCADTI.py --task predict")
