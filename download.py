import sys
from icrawler.builtin import GoogleImageCrawler


def main():
    if len(sys.argv) != 4:
        print("Usage: python download.py <no_of_images> <keyword> <output_folder_path>")
        return
    no_of_images = int(sys.argv[1])
    keyword = sys.argv[2]
    output_folder_path = sys.argv[3]
    google_Crawler = GoogleImageCrawler(storage={'root_dir': output_folder_path})
    google_Crawler.crawl(keyword=keyword, max_num=no_of_images)

if __name__ == "__main__":
    main()
