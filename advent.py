#!/usr/bin/python3
# coding: utf-8

import requests
import bs4

ADVENTOFCODE = 'http://adventofcode.com/2016/leaderboard/private/view/YOUR_PRIVATE_LEADERBOARD_NR.json'
ADVENT_COOKIE = {'session': 'PUT_COOKIE_HERE'}
DJUL = 'https://djul.datasektionen.se/toplist'
DJUL_COOKIES = {'connect.sid': 'PUT_COOKIE_HERE',
           '__cfduid': 'PUT_COOKIE_HERE'}
usernames = {"USERNAMES", "TO", "LIST", "HERE"}


def get_name(elem):
    try:
        name = elem.contents[0].text.strip()
        return name
    except:
        return elem.text.strip()


def aoc():
    r = requests.get(ADVENTOFCODE, cookies=ADVENT_COOKIE)
    if r.status_code == requests.codes.ok:
        members = r.json()["members"]
        output_string = "adventofcode\n\n"
        # Get all members
        users = [(m["name"], m["stars"]) for m in members.values()]
        # Sort members by stars decending
        users.sort(key=lambda s: -s[1])
        # Add each user to outputString
        top10 = 10
        for username, stars in users:
            if top10 > 0:
                output_string += "{0:<5} {1:<20}\n".format(str(stars), str(username))
                top10 -= 1
        print(output_string)
    else:
        print("Advent of Code not working: " + str(r.status_code) + "\ncheck your cookies/leaderboard #")


def djul():
    r = requests.get(DJUL, cookies=DJUL_COOKIES)
    if r.status_code == requests.codes.ok:
        c = r.content
        soup = bs4.BeautifulSoup(c, "html5lib")
        table = soup.find('table', attrs={'class': 'toplist'})
        rows = table.find_all("tr")
        djul_string = 'KTH dJul:\n\n{0:<5} {1:<15} {2:<6} {3:<5}\n'.format("Plats", "Namn", "Lösta", "Tid")
        for row in rows:
            cols = row.find_all("td")
            values = set(map(get_name, cols))
            if len(usernames.intersection(values)) > 0:
                djul_string += '{0:<5} {1:<15} {2:<6} {3:<5}\n'.format(cols[0].text.strip(),
                                                                        cols[1].a.text.strip(),
                                                                        cols[2].text.strip(),
                                                                        cols[3].text.strip())
        print(djul_string)
    else:
        print("dJulkalender not working: " + str(r.status_code) + "\ncheck your cookies")

aoc()
djul()
