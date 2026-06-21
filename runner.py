import pytest
import sys

import sys
sys.dont_write_bytecode = True

def main():
    # Customize the arguments for pytest run
    pytest_args = [
        "tests/pl_customer/adls_bronzecustomer/test_customer_bronze.py"
    ]

    # Exit with pytest's exit code
    sys.exit(pytest.main(pytest_args))
#hsjfhsd
#updated in local

if __name__ == "__main__":
    main()
