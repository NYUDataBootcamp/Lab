import pandas as pd

from bs4 import BeautifulSoup

# from http://stackoverflow.com/questions/259091/how-can-i-scrape-an-html-table-to-csv/259100
def table2csv(html_txt):
   csvs = []
   soup = BeautifulSoup(html_txt, "lxml")
   tables = soup.findAll('table')

   for table in tables:
       csv = ''
       rows = table.findAll('tr')
       row_spans = []
       do_ident = False

       for tr in rows:
           cols = tr.findAll(['th','td'])

           for cell in cols:
               colspan = int(cell.get('colspan',1))
               rowspan = int(cell.get('rowspan',1))

               if do_ident:
                   do_ident = False
                   csv += ','*(len(row_spans))

               if rowspan > 1: row_spans.append(rowspan)

               csv += '"{text}"'.format(text=cell.text) + ','*(colspan)

           if row_spans:
               for i in range(len(row_spans)-1,-1,-1):
                   row_spans[i] -= 1
                   if row_spans[i] < 1: row_spans.pop()

           do_ident = True if row_spans else False

           csv += '\n'

       csvs.append(csv)
       #print csv

   return '\n\n'.join(csvs)

def create_zipcode_file():

    # from https://www.health.ny.gov/statistics/cancer/registry/appendix/neighborhoods.htm
    body = """\
    <table summary=" ">
    <tbody><tr>
        <th id="header1" abbr="Borough">Borough</th>
        <th id="header2" abbr="Neighborhood">Neighborhood</th>
        <th id="header3" abbr="ZIP Codes">ZIP Codes</th>
    </tr><tr>
        <td headers="header1" rowspan="7">Bronx</td>
        <td headers="header2"> Central Bronx</td>
        <td headers="header3"> 10453, 10457, 10460</td>
    </tr><tr>
        <td headers="header2"> Bronx Park and Fordham</td>
        <td headers="header3"> 10458, 10467, 10468</td>
    </tr><tr>
        <td headers="header2"> High Bridge and Morrisania</td>
        <td headers="header3"> 10451, 10452, 10456</td>
    </tr><tr>
        <td headers="header2"> Hunts Point and Mott Haven</td>
        <td headers="header3"> 10454, 10455, 10459, 10474</td>
    </tr><tr>
        <td headers="header2"> Kingsbridge and Riverdale</td>
        <td headers="header3"> 10463, 10471</td>
    </tr><tr>
        <td headers="header2"> Northeast Bronx</td>
        <td headers="header3"> 10466, 10469, 10470, 10475</td>
    </tr><tr>
        <td headers="header2"> Southeast Bronx</td>
        <td headers="header3"> 10461, 10462,10464, 10465, 10472, 10473</td>
    </tr><tr>
        <td headers="header1" rowspan="11">Brooklyn</td>
        <td headers="header2"> Central Brooklyn</td>
        <td headers="header3"> 11212, 11213, 11216, 11233, 11238</td>
    </tr><tr>
        <td headers="header2"> Southwest Brooklyn</td>
        <td headers="header3"> 11209, 11214, 11228</td>
    </tr><tr>
        <td headers="header2"> Borough Park</td>
        <td headers="header3"> 11204, 11218, 11219, 11230</td>
    </tr><tr>
        <td headers="header2"> Canarsie and Flatlands</td>
        <td headers="header3"> 11234, 11236, 11239</td>
    </tr><tr>
        <td headers="header2"> Southern Brooklyn</td>
        <td headers="header3"> 11223, 11224, 11229, 11235</td>
    </tr><tr>
        <td headers="header2"> Northwest Brooklyn</td>
        <td headers="header3"> 11201, 11205, 11215, 11217, 11231</td>
    </tr><tr>
        <td headers="header2"> Flatbush</td>
        <td headers="header3"> 11203, 11210, 11225, 11226</td>
    </tr><tr>
        <td headers="header2"> East New York and New Lots</td>
        <td headers="header3"> 11207, 11208</td>
    </tr><tr>
        <td headers="header2"> Greenpoint</td>
        <td headers="header3"> 11211, 11222</td>
    </tr><tr>
        <td headers="header2"> Sunset Park</td>
        <td headers="header3"> 11220, 11232</td>
    </tr><tr>
        <td headers="header2"> Bushwick and Williamsburg</td>
        <td headers="header3"> 11206, 11221, 11237</td>
    </tr><tr>
        <td headers="header1" rowspan="10">Manhattan</td>
        <td headers="header2"> Central Harlem</td>
        <td headers="header3"> 10026, 10027, 10030, 10037, 10039</td>
    </tr><tr>
        <td headers="header2"> Chelsea and Clinton</td>
        <td headers="header3"> 10001, 10011, 10018, 10019, 10020, 10036</td>
    </tr><tr>
        <td headers="header2"> East Harlem</td>
        <td headers="header3"> 10029, 10035</td>
    </tr><tr>
        <td headers="header2"> Gramercy Park and Murray Hill</td>
        <td headers="header3"> 10010, 10016, 10017, 10022</td>
    </tr><tr>
        <td headers="header2"> Greenwich Village and Soho</td>
        <td headers="header3"> 10012, 10013, 10014</td>
    </tr><tr>
        <td headers="header2"> Lower Manhattan</td>
        <td headers="header3"> 10004, 10005, 10006, 10007, 10038, 10280</td>
    </tr><tr>
        <td headers="header2"> Lower East Side</td>
        <td headers="header3"> 10002, 10003, 10009</td>
    </tr><tr>
        <td headers="header2"> Upper East Side</td>
        <td headers="header3"> 10021, 10028, 10044, 10065, 10075, 10128</td>
    </tr><tr>
        <td headers="header2"> Upper West Side</td>
        <td headers="header3"> 10023, 10024, 10025</td>
    </tr><tr>
        <td headers="header2"> Inwood and Washington Heights</td>
        <td headers="header3"> 10031, 10032, 10033, 10034, 10040</td>
    </tr><tr>
        <td headers="header1" rowspan="10">Queens</td>
        <td headers="header2"> Northeast Queens</td>
        <td headers="header3"> 11361, 11362, 11363, 11364</td>
    </tr><tr>
        <td headers="header2"> North Queens</td>
        <td headers="header3"> 11354, 11355, 11356, 11357, 11358, 11359, 11360</td>
    </tr><tr>
        <td headers="header2"> Central Queens</td>
        <td headers="header3"> 11365, 11366, 11367</td>
    </tr><tr>
        <td headers="header2"> Jamaica</td>
        <td headers="header3"> 11412, 11423, 11432, 11433, 11434, 11435, 11436</td>
    </tr><tr>
        <td headers="header2"> Northwest Queens</td>
        <td headers="header3"> 11101, 11102, 11103, 11104, 11105, 11106</td>
    </tr><tr>
        <td headers="header2"> West Central Queens</td>
        <td headers="header3"> 11374, 11375, 11379, 11385</td>
    </tr><tr>
        <td headers="header2"> Rockaways</td>
        <td headers="header3"> 11691, 11692, 11693, 11694, 11695, 11697</td>
    </tr><tr>
        <td headers="header2"> Southeast Queens</td>
        <td headers="header3"> 11004, 11005, 11411, 11413, 11422, 11426, 11427, 11428, 11429</td>
    </tr><tr>
        <td headers="header2"> Southwest Queens</td>
        <td headers="header3"> 11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421</td>
    </tr><tr>
        <td headers="header2"> West Queens</td>
        <td headers="header3"> 11368, 11369, 11370, 11372, 11373, 11377, 11378</td>
    </tr><tr>
        <td headers="header1" rowspan="4">Staten Island</td>
        <td headers="header2"> Port Richmond</td>
        <td headers="header3"> 10302, 10303, 10310</td>
    </tr><tr>
        <td headers="header2"> South Shore</td>
        <td headers="header3"> 10306, 10307, 10308, 10309, 10312</td>
    </tr><tr>
        <td headers="header2"> Stapleton and St. George</td>
        <td headers="header3"> 10301, 10304, 10305</td>
    </tr><tr>
        <td headers="header2"> Mid-Island</td>
        <td headers="header3"> 10314</td>
            </tr>
    </tbody></table>
    """

    from io import StringIO
    df = pd.read_csv(StringIO(table2csv(body)))
    df.fillna(method="ffill", inplace=True)
    df.drop("Unnamed: 3", axis=1, inplace=True)
    df.rename(columns={"ZIP Codes": "ZIP"}, inplace=True)
    df.set_index(["Borough", "Neighborhood"], inplace=True)
    zips = df.ZIP.str.split(", ?", expand=True)
    zips.reset_index(inplace=True)
    zips1 = pd.melt(zips, ["Borough", "Neighborhood"])
    zips1.drop("variable", axis=1, inplace=True)
    zips1.dropna(inplace=True)
    zips1["Neighborhood"] = zips1["Neighborhood"].str.strip()
    zips1.set_index(["Borough", "Neighborhood"], inplace=True)
    final = zips1.astype(int)
    final.sort_index(inplace=True)
    final.to_csv("nyc_zipcodes.csv")


if __name__ == '__main__':
    import os
    if not os.path.isfile("nyc_zipcodes.csv"):
        create_zipcode_file()

    df = pd.read_csv("nyc_zipcodes.csv", index_col=[0, 1])
