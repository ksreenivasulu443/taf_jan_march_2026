import datetime
import os
project_path =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
report_dir = os.path.join(project_path,'report')

os.makedirs(report_dir, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%d%m%Y%H%M%S")

report_filename = os.path.join(report_dir, f"report_{timestamp}.txt")
print("report_filename", report_filename)

def write_output(validation_type, status, details):
    with open(report_filename, "a") as report:
        report.write(f"{validation_type}: {status} Details: {details}\n ")


# write_output(validation_type='dummy', status='dummy status', details = "count failed missing record [1,2,2]")

#
#
# import csv
# import os
# from datetime import datetime
#
#
# # Create report folder dynamically
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#
# project_path = os.path.dirname(
#     os.path.dirname(
#         os.path.dirname(os.path.abspath(__file__))
#     )
# )
#
# report_dir = os.path.join(
#     project_path,
#     "reports",
#     f"run_{timestamp}"
# )
#
# os.makedirs(report_dir, exist_ok=True)
#
#
# # Report files
# report_file = os.path.join(
#     report_dir,
#     "validation_report.csv"
# )
#
# summary_file = os.path.join(
#     report_dir,
#     "summary.txt"
# )
#
#
# # Initialize report
# def initialize_report():
#
#     with open(report_file, "w", newline="") as file:
#
#         writer = csv.writer(file)
#
#         writer.writerow([
#             "Execution Time",
#             "Validation Type",
#             "Status",
#             "Details"
#         ])
#
#
# # Write validation result
# def write_output(validation_type, status, details):
#
#     with open(report_file, "a", newline="") as file:
#
#         writer = csv.writer(file)
#
#         writer.writerow([
#             datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             validation_type,
#             status,
#             details
#         ])
#
#
# # Generate execution summary
# def generate_summary():
#
#     total = 0
#     passed = 0
#     failed = 0
#
#     with open(report_file, "r") as file:
#
#         rows = file.readlines()[1:]
#
#         total = len(rows)
#
#         for row in rows:
#
#             if "PASS" in row:
#                 passed += 1
#
#             elif "FAIL" in row:
#                 failed += 1
#
#     with open(summary_file, "w") as file:
#
#         file.write("=" * 50 + "\n")
#         file.write("ETL AUTOMATION EXECUTION SUMMARY\n")
#         file.write("=" * 50 + "\n\n")
#
#         file.write(f"Total Validations : {total}\n")
#         file.write(f"PASS              : {passed}\n")
#         file.write(f"FAIL              : {failed}\n")