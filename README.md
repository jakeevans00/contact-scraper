# contact-scraper

Get the contacts from Google's map search result page 

## Getting started
Make sure python in installed on your machine. Use `python3 --version` to check this. I am using version `3.13.1`

1. Clone this repository onto your computer 
```
git clone && cd contact-scraper
```
2. Run my setup script (this will create a virtual environment, activate it, and install dependencies). This might require you to make it executable. If the command below fails, try running this `chmod +x setup.sh` and then running it again.
```
./setup.sh
```
3. This application runs off of the Oxylabs local search scaper service. You'll need to create an account (even just a free trial) and provide your credentials for the scraper to work properly
If the setup script ran correctly, we should have generated a `.env` file for you. Fill in your username and password so the file looks like... (no need for quotes)
```
USERNAME=testuser
PASSWORD=testpassword
```
4. Run the program
```
python3 src/main.py -q "Query" -n 1
```

## Options
- `-q` query: The search term you want used. I suggest you format like this <keywords, location>. As an example "Beauty Salons, Sonora CA"
- `-n` num_pages: The number of pages you want scraped. Doesn't work yet, so it will just get you the first 20 results

By default the both `.csv` and `.excel` files will be created in the root project directory