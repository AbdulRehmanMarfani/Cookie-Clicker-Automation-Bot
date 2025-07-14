---

# Cookie Clicker Automation Bot 🍪🤖

A Python script that uses **Selenium WebDriver** to automate gameplay on the [Cookie Clicker](https://ozh.github.io/cookieclicker/) website. The bot clicks cookies rapidly, buys the most expensive affordable buildings every 15 seconds, and calculates cookies per second over a 5-minute session.

---

## Features 📋

* **Auto Clicking**: Continuously clicks the big cookie every 0.1 seconds.
* **Smart Purchasing**: Buys the **most expensive** affordable building every 15 seconds.
* **Timed Execution**: Runs for exactly **5 minutes** and then stops.
* **Performance Stats**: Calculates and displays **Cookies Per Second (CPS)** manually and compares it with the in-game CPS.
* **Cookie Consent Handling**: Automatically accepts cookie banners and selects language.
* **Clean Exit**: Gracefully closes the browser after completion.

---

## Libraries Used 🔌

* [`selenium`](https://pypi.org/project/selenium/)
* [`schedule`](https://pypi.org/project/schedule/)
* `time` (built-in)

---

## How It Works ⚙️

1. Opens the Cookie Clicker game in Microsoft Edge.
2. Accepts cookie banner and sets language to English.
3. Repeatedly clicks the big cookie to generate cookies.
4. Every 15 seconds:

   * Scans store for unlocked, enabled items.
   * Buys the **most expensive affordable** item.
5. After 5 minutes:

   * Stops execution.
   * Calculates CPS = (cookies earned) / (elapsed time).
   * Reads the in-game CPS for comparison.
   * Exits.

---

## Setup 🛠️

### 1. Clone the Repo

```bash
git clone https://github.com/AbdulRehmanMarfani/cookie-clicker-bot.git
cd cookie-clicker-bot
```

### 2. Install Required Packages

```bash
pip install selenium schedule
```

### 3. Install Edge WebDriver

Download [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and make sure it's added to your system PATH.

> Make sure the WebDriver version matches your installed Edge browser version.

---

## Running the Script ▶️

```bash
python cookie_clicker_bot.py
```

The bot will:

* Start clicking cookies
* Purchase upgrades intelligently
* Run for 5 minutes
* Print cookie stats and exit

---

## Sample Output 🖨️

```
Cookie consent accepted.
Prices: [15, 100, 500]
Store items found: 3
Current Cookies: 245
Trying to click store_items[2]
Affordable item indices: [0, 1, 2]
Cookies per second (calculated): 73.42
Cookies per second (game): 75.6
```

---

## Security 🔐

No credentials are required for this script.
If you plan to extend this bot with logging, analytics, or cloud integrations, use environment variables for sensitive keys and tokens.

---

## Ideas for Extensions 🚀

* Automate **upgrades** (the top row).
* Track cookies per second over time in a CSV.
* Graph performance using `matplotlib` or `pandas`.
* Add a GUI dashboard using `Tkinter`.
* Save game state using local storage with browser automation.

---
