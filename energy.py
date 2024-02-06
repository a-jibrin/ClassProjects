from argparse import ArgumentParser
import sqlite3
import sys

class EnergyDB:
     """
    A class for managing a in-memory SQLite database of energy production data.

    Attributes:
        conn (sqlite3.Connection): The SQLite database connection.

    Methods:
        __init__(self, filename: str):
            Initializes the database and creates the production table.

        __del__(self):
            Cleans up the database connection when the object is destroyed.

        read(self, filename: str):
            Reads data from a CSV file and inserts it into the database.

        production_by_source(self, source: str, year: int) -> float:
            Calculates the total energy production by source and year.
      """
     def __init__(self, filename):
        """ Initialize the database and create production table.
         Args:
            filename (str): Path to a CSV file containing energy production data.
        """

        self.conn = sqlite3.connect(":memory:")
        self.read(filename)
     
     def __del__(self):
        """ Clean up the database connection. """
        try:
            self.conn.close()
        except:
            pass

     def read(self, filename):
        """ Read data from a CSV file and insert it into the database.
         Args:
            filename (str): Path to a CSV file containing energy production data. """
        
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE production
            (year integer, state text, source text, mwh real)
        """)
        
        with open(filename, "r") as file:
            file.readline()  # Skip the header
            for line in file:
                year, state, source, mwh = line.strip().split(',')
                cursor.execute("INSERT INTO production VALUES (?,?,?,?)",
                               (int(year), state, source, float(mwh)))

        self.conn.commit()

     def production_by_source(self, source, year):
        """ Calculate the total energy production by source and year.
         
        Args:
            source (str): The energy source name.
            year (int): The year for which to calculate the total production.

        Returns:
            float: The total energy production in megawatt hours (MWh). """
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(mwh) FROM production WHERE source=? AND year=?",
                       (source, year))
        total_mwh = cursor.fetchone()[0]
        return total_mwh

def main(filename):
    """ Build a database of energy sources and calculate the total production
    of solar and wind energy.

    Args:
    filename (str): path to a CSV file containing four columns:
    Year, State, Energy Source, Megawatthours.

    Side effects:
    Writes to stdout.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"),
               ("wind", "Wind")]
    for source_lbl, source_str in sources:
        print(f"Total {source_lbl} production in 2017: ",
              e.production_by_source(source_str, 2017))

def parse_args(arglist):
    """ Parse command-line arguments. """

    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
