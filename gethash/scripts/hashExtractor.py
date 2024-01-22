import requests
from bs4 import BeautifulSoup
import csv

def scape_website(url,output_csv):
    try: 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        target = soup.find('pre',class_="code")

        if target: 
            content = target.get_text()

            words = content.split()

            # print(content.index("- [ Hash modes ] -"))

            start = content.index("- [ Hash modes ] -")
            end = content.index("- [ Brain Client Features ] -")

            selected = content[start:end]

            lines = selected.split('\n ')

            csv_data = [['#', 'Name', 'Category']]

            for line in lines: 

                fields = [field.strip() for field in line.split(' | ')]
        
                if len(fields) == 3: 
                    csv_data.append(fields)     

            with open(output_csv, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(csv_data)    
            print(f"Data saved to {output_csv}")

        else: 
            print("Target element not found.")
    
    except requests.exceptions.RequestException as e: 
        print(f"Error: {e}")





output = "hashcat_data.csv"
scape_website("https://hashcat.net/wiki/doku.php?id=hashcat",output)