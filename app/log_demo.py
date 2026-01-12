import logging

from logger import setup_logger


def main() -> None:
    logger = setup_logger(level=logging.DEBUG)

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")

    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Something went wrong")


if __name__ == "__main__":
    main()
