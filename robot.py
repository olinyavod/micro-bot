import pyb
from lib.hcsr04 import HCSR04
import uasyncio as asyncio


class Robot:

    def __init__(self):
        trigger_pin = pyb.Pin.cpu.B3
        echo_pin = pyb.Pin.cpu.B4
        self._servo = pyb.Servo(1)
        self._dist_sensor = HCSR04(trigger_pin, echo_pin)
        self._dist = 0.0

    async def run(self) -> None:
        angle_offset = const(40)
        angle = angle_offset
        speed = 1
        max_angle = 0
        max_dist = 0
        while True:
            wait = asyncio.sleep_ms(50)
            # self._servo.angle(angle)

            # angle += speed

            # if angle >= 90 or angle <= -30:
            #  speed *= -1
            #  angle += speed
            #  print(f"Max {max_dist:.2f} cm on angle {max_angle-angle_offset}")
            #  max_dist = 0

            await wait
            has_error, dist = await self._dist_sensor.distance_cm()

            if has_error:
                continue

            self._dist = dist

            # print(f"Distance: {dist:.2f} cm")

            # if max_dist < self._dist:
            #   max_dist = self._dist
            #  max_angle = angle

    def distance(self) -> float:
        return self._dist
