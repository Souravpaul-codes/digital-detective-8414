# Mission 7 — How computers communicate

## 1. Task / objective
Explain basic network types and concepts, observe network lookup and connectivity information, and describe what happens when a website opens.

## 2. Work completed
- Explained network concepts (LAN, MAN, WAN, DNS, router, protocol, etc.)
- Ran connectivity and DNS lookup tests from Terminal
- Wrote a step-by-step explanation of what happens when opening a website

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `ping -c 3 example.com` | Tests if my computer can reach a website by sending small packets |
| `nslookup example.com` | Looks up the IP address associated with a domain name using DNS |

## 4. My understanding

### Task 7.1 — Network concepts

| Concept | Explanation in my own words | Example |
|---------|---------------------------|---------|
| LAN | A network that covers a small area like one room or building. All devices are close together. | The Wi-Fi network in my home connecting my laptop, phone and printer. |
| MAN | A network that covers a larger area like a city or a big university campus. | A university network connecting multiple buildings across campus. |
| WAN | A network that covers very large areas — across countries or the whole world. | The internet is the biggest example of a WAN. |
| DNS | A system that translates human-readable domain names into IP addresses that computers understand. | When I type `google.com`, DNS finds the IP address like `142.250.195.14` so my computer can connect. |
| Router | A device that connects different networks and decides where to send data packets. | My home router connects my local Wi-Fi network to the internet. |
| Protocol | A set of rules that devices follow to communicate with each other properly. | HTTP is the protocol used by web browsers to request and receive web pages. |
| Packet switching | Data is broken into small packets that travel independently across the network and are reassembled at the destination. | When I download a file, it arrives in many small packets that get put back together. |
| Client-server | A model where one device (client) requests a service and another device (server) provides it. | My browser (client) requests a web page from Google's server, and the server sends it back. |

### Task 7.2 — Network observations

**Connectivity test (`ping`):**
I ran `ping -c 3 example.com` and got replies with round-trip times. This tells me my computer can reach the website and how fast the connection is. 0% packet loss means all packets arrived successfully.

**DNS lookup (`nslookup`):**
I ran `nslookup example.com` and it showed IP addresses like `104.20.23.154`. This tells me the DNS server translated the domain name into a numerical IP address.

**Role of DNS when browsing:** When I type a website name in my browser, DNS acts like a phone book — it looks up the name and returns the actual IP address of the server. Without DNS, I would have to type numbers like `104.20.23.154` instead of `example.com`.

> Note: Private IP addresses and Wi-Fi details have been redacted.

### Task 7.3 — What happens when you open a website?

1. **I type the URL** (like `www.example.com`) in my browser and press Enter. My browser is the **client**.

2. **DNS lookup** — My browser asks the DNS server to translate `www.example.com` into an IP address. The DNS server responds with something like `104.20.23.154`.

3. **Connection request** — My browser uses the IP address to send a request to the web **server** through my **router** and the internet. It uses the **HTTP/HTTPS protocol**.

4. **Router forwards the request** — My home router sends the request through my internet provider's network to the destination server, which could be anywhere in the world.

5. **Server processes the request** — The web server receives the request, finds the requested page, and prepares a response.

6. **Server sends the response** — The server sends the web page data back as small **packets** that travel through the internet, through routers, back to my computer.

7. **Browser displays the page** — My browser receives all the packets, reassembles them, and renders the HTML, CSS and images on my screen. I see the website.

## 5. Difficulties faced
I got confused between DNS and the router — they both seem to help with connecting.

## 6. How I resolved them
I understood that DNS only translates names to IP addresses (like a phone book). The router actually forwards the data to the right destination. They do different jobs.

## 7. Evidence / files
- This README with network concepts table, observations and website steps

## 8. Commit details
- Commit message: **"Explain networking concepts and website communication"**
- Pushed to GitHub and verified.
