from lib.hcsr04 import HCSR04
import uasyncio as asyncio
from lib.line_sensor import LineSensor
from micropython import const

class Robot:

    def __init__(self):
        self._line_sensor = LineSensor(const("B5"), self._line_on_changed)
        self._dist_sensor = HCSR04(const("B3"), const("B4"))
        self._dist = 0.0

    def _line_on_changed(self, value:int):
        print(f"Line: {value}")

    async def run(self) -> None:
        while True:
            await asyncio.sleep_ms(50)
            has_error, dist = await self._dist_sensor.distance_cm()

            if has_error:
                continue
            self._dist = dist

    def distance(self) -> float:
        return self._dist

    def close(self):
        self._line_sensor.close()
        self._dist_sensor.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


