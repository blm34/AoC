import browser_cookie3 as bc3


def get_cookies():
    cookies = bc3.firefox(domain_name=".adventofcode.com")
    if not (".adventofcode.com" in str(cookies)):
        input("Cookie not in Firefox. Temporarily Close chrome then press enter to continue")
        cookies = bc3.chrome(domain_name=".adventofcode.com")
        print("You may now reopen Chrome")
    return cookies
