import os
import json

data_1 = []


def write_initial_file():
    file = open('../../links/links.txt', 'w')
    file.write('https://www.kapruka.com/shops/deliveryCatalogCompact_wide.jsp')


def crawl_link_extractor():
    # execute 2 times to extract all the links in the kapruka.com
    for i in range(2):
        os.system("python scrapy_command_executor.py crawl kaprukacomlinks")


def remove_duplicate_links():
    file = open('../../links/links.txt', 'r')
    urls = file.read().split('\n')
    url_set = set(urls)
    links = list(url_set)

    file = open('../../links/final_links.txt', 'w')
    for link in links[:-1]:
        file.write(link + '\n')
    file.write(links[-1])


def crawl_pages():
    os.system("python scrapy_command_executor.py crawl kaprukacom -o ../../data/items_details_1.json")


def extract_data():
    os.system("python scrapy_command_executor.py crawl kaprukacomextractor -o ../../data/items_details_2.json")


def remove_NA_values():
    global data_1
    with open('../../data/items_details_1.json') as json_file:
        data_1 = json.load(json_file)
    for i in data_1:
        for key in i.keys():
            if i[key] == "N/A":
                i[key] = None


def merge_files():
    global data_1
    data = []
    with open('../../data/items_details_2.json') as json_file_2:
        data_2 = json.load(json_file_2)

    for i in data_1:
        for j in data_2:
            if "name" in i and "name" in j:
                if i["name"] == j["name"]:
                    data.append(
                        {
                            "name": i["name"],
                            "payment_method": i["payment_method"] if "payment_method" in i else None,
                            "vendor": i["vendor"] if "vendor" in i else None,
                            "availability": i["availability"] if "availability" in i else None,
                            "delivery_areas_src": i["delivery_areas_src"] if "delivery_areas_src" in i else None,
                            "similar_items": i["similar_items"] if "similar_items" in i else None,
                            "max_qty": i["max_qty"] if "max_qty" in i else None,
                            "category": j["category"],
                            "price": j["offers"]["price"],
                            "brand": j["brand"]
                        }
                    )

    with open('../../data/items_details.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    # write_initial_file()
    # crawl_link_extractor()
    # remove_duplicate_links()
    # crawl_pages()
    # extract_data()
    remove_NA_values()
    merge_files()