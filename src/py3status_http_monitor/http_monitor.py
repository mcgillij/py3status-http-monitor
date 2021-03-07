# -*- coding: utf-8 -*-
"""
Module to display the status of a remote web service
"""


class Py3status:
    cache_timeout = 600
    service_name = "test"
    service_location = "http://example.com"
    timeout = 3
    status_good = "🟢"
    status_bad = "🔴"
    format = "{service_name}: {status}"

    def _get_status(self):
        try:
            status = self.py3.request(
                self.service_location, timeout=self.timeout)
            if status.status_code != 200:
                return self.status_bad
            return self.status_good

        except self.py3.RequestException:
            return self.status_bad

    def http_monitor(self):
        status = self._get_status()
        full_text = self.py3.safe_format(
            self.format, {"service_name": self.service_name, "status": status}
        )
        return {
            "full_text": full_text,
            "cached_until": self.py3.time_in(self.cache_timeout),
        }


if __name__ == "__main__":
    from py3status.module_test import module_test
    module_test(Py3status)
