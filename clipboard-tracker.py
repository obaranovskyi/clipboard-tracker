import asyncio
import sys

from clipboard_tracker.__main__ import main, read_args
from clipboard_tracker.text import create_file_if_not_exists, set_filename

if __name__ == "__main__":
    set_filename(read_args())
    create_file_if_not_exists()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(0)
