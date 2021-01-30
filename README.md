# web-scraper-differences-checker

A web scraper to check web pages differences using different approaches.

# Examples of usage

## Check number of HTML objects

```console
user@host:~$ python web_scraper_differences_checker.py file:///home/user/e_commerce_test.html check_n_objects buy-btn
Sleep 5 s to let the page load...

Number of buy-btn: 3
Random sleep 15 s...
Page refreshed (1)!

Number of buy-btn: 3
Random sleep 20 s...
Page refreshed (2)!

Number of buy-btn: 4
Difference found!
```

## Check HTML

```console
user@host:~$ python web_scraper_differences_checker.py file:///home/user/e_commerce_test.html check_html
Sleep 5 s to let the page load...

Current HTML: <html><head></head><body onload="generateButtons()">
    <h2>E-commerce test</h2>
    <p>Welcome!</p>
    <!--<button name="buy-btn">Buy 4</button>-->
    <script>
      function generateButtons() {
        for (var i = 1; i<=3; i++){
          var btn = document.createElement("button");
          btn.innerHTML = "Buy " + i.toString();
          btn.name = "buy-btn";
          document.body.appendChild(btn);
        }
      }
    </script> 
<button name="buy-btn">Buy 1</button><button name="buy-btn">Buy 2</button><button name="buy-btn">Buy 3</button></body></html>
Random sleep 10 s...
Page refreshed (1)!

Current HTML: <html><head></head><body onload="generateButtons()">
    <h2>E-commerce test</h2>
    <p>Welcome!</p>
    <!--<button name="buy-btn">Buy 4</button>-->
    <script>
      function generateButtons() {
        for (var i = 1; i<=3; i++){
          var btn = document.createElement("button");
          btn.innerHTML = "Buy " + i.toString();
          btn.name = "buy-btn";
          document.body.appendChild(btn);
        }
      }
    </script>
<button name="buy-btn">Buy 1</button><button name="buy-btn">Buy 2</button><button name="buy-btn">Buy 3</button></body></html>
Random sleep 20 s...
Page refreshed (2)!

Current HTML: <html><head></head><body onload="generateButtons()">
    <h2>E-commerce test</h2>
    <p>Welcome!</p>
    <!--<button name="buy-btn">Buy 4</button>-->
    <button name="buy-btn">Buy 4</button>
    <script>
      function generateButtons() {
        for (var i = 1; i<=3; i++){
          var btn = document.createElement("button");
          btn.innerHTML = "Buy " + i.toString();
          btn.name = "buy-btn";
          document.body.appendChild(btn);
        }
      }
    </script>
<button name="buy-btn">Buy 1</button><button name="buy-btn">Buy 2</button><button name="buy-btn">Buy 3</button></body></html>
Difference found!
```

## Check screenshot

```console
user@host:~$ python web_scraper_differences_checker.py file:///home/user/e_commerce_test.html check_screenshot
Sleep 5 s to let the page load...

Screenshot saved...
Random sleep 14 s...
Page refreshed (1)!

Screenshot saved...
Random sleep 18 s...
Page refreshed (2)!

Screenshot saved...
Difference found!
```
