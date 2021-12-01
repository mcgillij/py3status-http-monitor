# py3status-http-monitor
Python module for monitoring **http** services in your py3status bar.

[![Downloads](https://static.pepy.tech/personalized-badge/py3status-http-monitor?period=total&units=international_system&left_color=blue&right_color=green&left_text=Downloads)](https://pepy.tech/project/py3status-http-monitor)

## Screenshot
![Status Bar with py3status_http_monitor](https://raw.githubusercontent.com/mcgillij/py3status-http-monitor/main/images/status_bar.png)

## Prerequisites

This is an i3 / py3status module, so you'll need those first off.

## Installation

### From Git

``` bash
git clone https://github.com/mcgillij/py3status-http-monitor.git
mkdir -p ~/.i3/py3status && cd ~/.i3/py3status
ln -s <PATH_TO_CLONED_REPO>/src/py3status-http-monitor/http_monitor.py ./
```

### With Pip, Pipenv or Poetry

``` bash
pip install py3status-http-monitor
pipenv install py3status-http-monitor
poetry add py3status-http-monitor && poetry install
```

### With `yay`

``` bash
yay -S py3status-http-monitor
```

### Building Arch package w/PKGBUILD

``` bash
git clone https://aur.archlinux.org/py3status-http-monitor.git
cd py3status-http-monitor.git
makechrootpkg -c -r $HOME/$CHROOT
```

### Installing built Arch package

``` bash
sudo pacman -U --asdeps py3status-http-monitor-*-any.pkg.tar.zst
```

## Configuration

Next you will need to add the services you want to monitor, and optionally choose some appropriate emoji's.
You can also configure actions to open up your browser when you click on the icon, which I find pretty handy.

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
   on_click 1 = "exec xdg-open http://yourserver:8181"
}

http_monitor  'virtualbox' {
   service_location = "http://yourserver:81/vb/"
   service_name = '💻'
   on_click 1 = "exec xdg-open http://yourserver:81/vb/"
}

http_monitor  'plex' {
   service_location = "http://yourserver:32400/web/index.html#"
   service_name = '🎥'
   on_click 1 = "exec xdg-open http://yourserver:32400/web/index.html#"
}

http_monitor  'airsonic' {
   service_location = "http://yourserver:4040"
   service_name = '🍃'
}

http_monitor  'pihole' {
   service_location = "http://yourserver:80"
   service_name = '🕳️ '
   on_click 1 = "exec xdg-open http://yourserver:80"
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

## Restart i3

Once the package is installed and configured you just need to restart i3.
