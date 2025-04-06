import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", "-q", type=str, required=True)
    parser.add_argument("--location", "-l", type=str)
    parser.add_argument("--num_results", "-n", type=int, default=1)
    parser.add_argument("--output", "-o", type=str, default="output.csv")
    parser.add_argument("--headless", "-H", action="store_true")
    return parser.parse_args()


def load_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Results file '{file_path}' not found")
        return None
    except Exception as e:
        print(f"Error loading results: {e}")
        return None