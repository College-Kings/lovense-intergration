init python:
    class Lovense():
        @staticmethod
        def vibrate(strength: int, time: float, stop_previous: bool = True):
            data = {
                "command": "Function",
                "action": f"Vibrate:{strength}",
                "timeSec": time,
                "stopPrevious": int(stop_previous),
                "apiVer": 1
            }

            response = requests.post(f"https://{domain}:{httpsPort}/command", json=data)

        @staticmethod
        def rotate(strength: int, time: int, stop_previous: bool = True):
            data = {
                "command": "Function",
                "action": f"Rotate:{strength}",
                "timeSec": time,
                "stopPrevious": int(stop_previous),
                "apiVer": 1
            }

            response = requests.post(f"https://{domain}:{httpsPort}/command", json=data)

        @staticmethod
        def pump(strength: int, time: int, stop_previous: bool = True):
            data = {
                "command": "Function",
                "action": f"Pump:{strength}",
                "timeSec": time,
                "stopPrevious": int(stop_previous),
                "apiVer": 1
            }

            response = requests.post(f"https://{domain}:{httpsPort}/command", json=data)

        @staticmethod
        def stop():
            data = {
                "command": "Function",
                "action": "Stop",
                "timeSec": 0,
                "apiVer": 1
            }

            response = requests.post(f"https://{domain}:{httpsPort}/command", json=data)
