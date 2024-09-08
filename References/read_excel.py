import openpyxl


def read_excel(file_path):
    # Load the workbook and select the active worksheet
    workbook = openpyxl.load_workbook("users.xlsx")
    sheet = workbook.active

    # Read the header (first row)
    headers = [cell.value for cell in sheet[1]]

    # Print the header
    print("Headers:", headers)

    # Read and print each row of data
    for row in sheet.iter_rows(min_row=2, values_only=True):
        print(row)


# Path to your Excel file
file_path = 'C:\\Users\\DELL\\PycharmProjects\\pythonProject\\PytestFrameworkDemo\\References\\users.xlsx'


# Call the function to read and print the data
read_excel(file_path)
