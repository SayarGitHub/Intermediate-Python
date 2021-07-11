# Creates a spider to to benchmark single-process vs multi-process

from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
import time


def random_starting_url():
    starting = "".join(
        random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3)
    )
    url = "".join(["http://", starting, ".com"])
    return url


def handle_local_links(url, link):
    if link.startswith("/"):
        return "".join([url, link])
    else:
        return link


def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, "lxml")
        body = soup.body
        links = [link.get("href") for link in body.find_all("a")]
        links = [handle_local_links(url, link) for link in links]
        links = [str(link.encode("ascii")) for link in links]
        return links

    except TypeError as e:
        print(e)
        print("Got a TypeError, probably because we tried to iterate over None.")
        return []

    except IndexError as e:
        print(e)
        print(
            "We probably got no useful links so iterating over empty list gives IndexError."
        )
        return []

    except AttributeError as e:
        print(e)
        print("Likely got None for links, so we are throwing this.")
        return []

    except Exception as e:
        print(str(e))
        return []


def main():
    start = time.time()
    how_many = 10
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(50)]
    data = p.map(get_links, parse_us)
    data = [url for url_list in data for url in url_list]
    p.close()
    print(time.time() - start)
    with open("urls.txt", "w") as f:
        f.write(str(data))


if __name__ == "__main__":
    main()


# In this example 2 processes took 95s on my pc. Wheareas for 10
# processes it took 29s.

