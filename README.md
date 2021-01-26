# http_monitor
py3status module for monitoring http services

## Screenshot
![Status Bar with http_monitor](/images/status_bar.png)

## Prerequisites

This is an i3 / py3status module, so you'll need those first off.

## Installation

```bash
git clone git@github.com:mcgillij/http_monitor.git ~/.i3/py3status/
```

## Configuration

Next you will need to add the services you want to monitor, and optionally choose some appropriate emoji's.

**~/.config/i3/i3status.conf**

```bash
...
general {
        colors = true
        interval = 15
}

order += "http_monitor apache"
order += "http_monitor medusa"
order += "http_monitor pihole"
order += "http_monitor nextcloud"
order += "http_monitor plex"
order += "http_monitor virtualbox"
order += "http_monitor airsonic"
order += "clock"
order += "mail"
...

http_monitor  'nextcloud' {
   service_location = "http://yourserver:8181"
   service_name = '⛅'
}

http_monitor  'virtualbox' {
   service_location = "http://yourserver:81/vb/"
   service_name = '💻'
}

http_monitor  'plex' {
   service_location = "http://yourserver:32400/web/index.html#"
   service_name = '🎥'
}

http_monitor  'airsonic' {
   service_location = "http://yourserver:4040"
   service_name = '🍃'
}

http_monitor  'pihole' {
   service_location = "http://yourserver:80"
   service_name = '🕳️ '
}

http_monitor  'apache' {
   service_location = "http://yourserver:81"
   service_name = '🪶'
}

http_monitor  'medusa' {
   service_location = "http://yourserver:8081"
   service_name = '🐍'
}
``` 
## Configuration Options

You can pass in the following configuration options:

* service_location
* service_name
* timeout
* cache_timeout

