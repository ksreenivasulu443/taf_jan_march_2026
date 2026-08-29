import pytest
import sys

sys.dont_write_bytecode = True


def main():
    pytest_args = [
        "-v",
        "-s",
        # "-m", "customer",
        "tests/pipeline_apr_customer_load/adls_customerLanding"
    ]

    # Exit with pytest's exit code
    sys.exit(pytest.main(pytest_args))


if __name__ == "__main__":
    main()