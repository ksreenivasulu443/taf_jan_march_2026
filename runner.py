import pytest
import sys

import sys
sys.dont_write_bytecode = True

def main():
    # Customize the arguments for pytest run
    pytest_args = [
        "tests/table1/",                      # Folder containing your test cases
        "-v",                          # Verbose output
        "--tb=short",                  # Short traceback format
        "--capture=tee-sys",          # Capture and also print stdout/stderr
        "--html=reports/report.html", # HTML report generation
        "--self-contained-html",      # Standalone HTML with styles/scripts
        "-m", "regression",
        "-k"# Run all tests except those marked with @pytest.mark.ignore
    ]

    # Exit with pytest's exit code
    sys.exit(pytest.main(pytest_args))
#hsjfhsd
#updated in local

if __name__ == "__main__":
    main()
