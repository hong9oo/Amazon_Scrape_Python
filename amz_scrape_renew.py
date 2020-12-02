from requests_html import HTMLSession

def get_url(search_text):
    session = HTMLSession()
    products = []

    # Operate through each page
    for x in range(1, 7):
        # Need a separate iteration for product page 1
        if x == 1:
            url = 'https://www.amazon.com/s?k={}&qid=1606853501&ref=sr_pg_{}'

            # Format a url with specific product names
            search_term = search_text.replace(' ', '+')
            url_inc = url.format(search_term, x)

            print(f"**********Current Page is**********" + f"[{x}]")

            # Navigate through html and find wanted info
            r = session.get(url_inc)
            r.html.render(sleep=1)
            items = r.html.find('h2')

            for item in items:
                product = item.text
                # Scrape only those from Apple
                if product.startswith("Apple"):
                    print(f"{product}")
                    products.append(product)
        else:
            url = 'https://www.amazon.com/s?k={}&page={}&qid=1606853501&ref=sr_pg_{}'

            search_term = search_text.replace(' ', '+')
            url_inc = url.format(search_term, x, x)
    
            print(f"**********Current Page is**********" + f"[{x}]")

            r = session.get(url_inc)
            r.html.render(sleep=1)
            items = r.html.find('h2')

            for item in items:
                product = item.text

                if product.startswith("Apple"):
                    print(f"{product}")
                    products.append(product)
            
    return set(products)

# Example with AirPods Pro
product_titles = get_url('airpods pro')