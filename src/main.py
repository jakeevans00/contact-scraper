from inputs import parse_args
from fetcher import get_data_from_local, get_data_from_api
from parser import convert_txt_to_html
from bs import BSParser
import pandas as pd

def main():
    use_local = False # Use this boolean in development to save on API requests if you need to customize the script
    args = parse_args()
    results_raw = None

    if not use_local:
        get_data_from_api(args.query, args.num_results)

    results_raw = get_data_from_local() # get_data_from_api() also loads the raw file into local
    results_html = convert_txt_to_html(results_raw)

    bs = BSParser(results_html) 
    results = bs.run()

    df = pd.DataFrame(results)
    df.to_csv('locations_data.csv', index=False)
    df.to_excel('locations_data.xlsx', index=False)

if __name__ == "__main__":
    main()

