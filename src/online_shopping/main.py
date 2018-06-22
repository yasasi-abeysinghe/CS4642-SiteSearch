import os


def write_initial_file():
    file = open('../../links/links.txt', 'w')
    file.write('https://www.kapruka.com/shops/deliveryCatalogCompact_wide.jsp')


def crawl_link_extractor():
    # execute 6 times to extract all the links in the botanicgardens.gov.lk
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
    os.system("python scrapy_command_executor.py crawl kaprukacom -o ../../data/items_details_2.json")


def extract_data():
    os.system("python scrapy_command_executor.py crawl kaprukacomextractor -o ../../data/items_details_1.json")


if __name__ == "__main__":
    write_initial_file()
    crawl_link_extractor()
    remove_duplicate_links()
    crawl_pages()
    extract_data()