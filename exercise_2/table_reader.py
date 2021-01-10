class TableReader(object):

    def __init__(self, path_to_file, delimiter):

        self.table_file_object = open(path_to_file, 'r')

        self.delimiter = delimiter

        self.rows = []

    def read(self):

        # First row contains headers, so skip it
        first_line = self.table_file_object.readline()

        for line in self.table_file_object.readlines():

            this_row = TableRow(row_text = line, delimiter = self.delimiter)

            self.rows.append(this_row)

    def sum_second_and_third_columns(self):

        print ("Sample_Id_1\tSum_col2_col3")
        for row in self.rows:
            
            this_sample = row.values[0]
            this_sum = row.values[1] + row.values[2]

            print(f"{this_sample}\t{this_sum}")

    def close_file_object(self):
        self.table_file_object.close()

class TableRow(object):

    def __init__(self, row_text, delimiter):
        
        self.row_text = row_text

        self.delimiter = delimiter

        self.values = self.parse_row_into_columns(self.row_text)

    def parse_row_into_columns(self, row_text):

        stripped = row_text.strip()

        spl = stripped.split(self.delimiter)

        return spl


if __name__ == "__main__":

    my_table_path = "exercise2_table.tsv"

    my_table_reader = TableReader(my_table_path, delimiter = ",")

    my_table_reader.sum_second_and_third_columns()

    my_table_reader.close_file_object()

    



