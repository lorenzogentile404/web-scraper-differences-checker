# web-scraper-differences-checker

A web scraper to check web pages differences using different approaches.

## Define approach

```python
# Check number of objects
check_n_objects = True
...

# Check HTML
check_html = False
...

# Check screenshot
check_screenshot = False
```

### Check number of HTML objects

```console
user@host:~$ python web_scraper_differences_checker.py
Page downloaded!
Number of buy-btn: 3
Page refreshed (1)!
Sleep 16 s...

Number of buy-btn: 3
Page refreshed (2)!
Sleep 18 s...

Number of buy-btn: 4
Difference found!
```

## Check HTML

```console
user@host:~$ python web_scraper_differences_checker.py
Page downloaded!
Current HTML: <html><head></head><body>
    <h2>E-commerce test</h2>
    <p>Welcome!</p>
    <button name="buy-btn">Buy 1</button>
    <button name="buy-btn">Buy 2</button>
    <button name="buy-btn">Buy 3</button>
</body></html>
Page refreshed (1)!
Sleep 17 s...

Current HTML: <html><head></head><body>
    <h2>E-commerce test</h2>
    <p>Welcome!</p>
    <button name="buy-btn">Buy 1</button>
    <button name="buy-btn">Buy 2</button>
    <button name="buy-btn">Buy 3</button>
</body></html>
Page refreshed (2)!
Sleep 18 s...

Current HTML: <html><head></head><body>
    <h2>E-commerce test</h2>
    <p>Welcome!</p>
    <button name="buy-btn">Buy 1</button>
    <button name="buy-btn">Buy 2</button>
    <button name="buy-btn">Buy 3</button>
    <button name="buy-btn">Buy 4</button>
</body></html>
Difference found!
```

## Check screenshot

```console
user@host:~$ python web_scraper_differences_checker.py
Page downloaded!
Screenshot saved...
Page refreshed (1)!
Sleep 17 s...

Screenshot saved...
Page refreshed (2)!
Sleep 16 s...

Screenshot saved...
Difference found!
```
