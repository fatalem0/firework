import time
from src import create_app
import os


def main():
    time.sleep(20)
    app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")
    app.run(host="0.0.0.0", use_reloader=False)

if __name__ == "__main__":
    main()