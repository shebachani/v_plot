import sys
from collections import defaultdict

def parse_bed_file(input_file):
    data = defaultdict(int)  # Dictionary to store counts (key: (distance, length), value: count)

    with open(input_file, 'r') as f:
        for line in f:
            cols = line.strip().split('\t')

            # Extract required fields
            start_pos = int(cols[2])
            end_pos = int(cols[3])
            frag_start = int(cols[8])
            frag_end = int(cols[9])
            fragment_length = int(cols[11])

            # Calculate the center of the interval
            interval_center = (start_pos + end_pos) / 2

            # Calculate the relative distance from the center
            fragment_center = (frag_start + frag_end) / 2
            relative_distance = round(fragment_center - interval_center)

            # Store the count of (relative_distance, fragment_length)
            data[(relative_distance, fragment_length)] += 1

    return data

def write_matrix_file(data, output_file):
    with open(output_file, 'w') as f:
        for (distance, length), count in data.items():
            f.write(f"{distance} {length} {count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_matrix.py <input.bed> <output_matrix.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = parse_bed_file(input_file)
    write_matrix_file(data, output_file)

    print(f"Matrix file generated: {output_file}")

