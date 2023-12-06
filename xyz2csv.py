import csv

def xyz_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    data = []
    for line in lines:
        coordinates = [float(coord) for coord in line.split()]
        data.append(coordinates)

    # Write the data to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

# Replace 'your_xyz_file.xyz' with the path to your XYZ file
# Replace 'output_file.csv' with the desired output CSV file path
xyz_file_path = 'escanor_axe.xyz'
csv_output_path = 'escanor_axe.csv'
xyz_to_csv(xyz_file_path, csv_output_path)

print(f"Conversion complete. Data has been written to {csv_output_path}.")
