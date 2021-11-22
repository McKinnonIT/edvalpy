import edvalpy

edval = edvalpy.Edval("TOKEN_HERE")

edval.configs
edval.ischolaris.files()

csv_file = edval.ischolaris.get_file("classlists.csv")
edval.ischolaris.save_file("classlists.csv", r"C:\Users\Sam\Downloads\classes.csv")
