RESISTOR = 10       # Ohm
COIL = 1 * 10e-3    # Henry
VOLTAGE_START = 300 # Volt
CURRENT_START = 10  # A
DUTY_CYCLE = 20 * 10e-3    # /100 %
PULSE_WIDTH = 5 * 10e-3 # seconds
SCANS = 12

VOLTAGE = [0, VOLTAGE_START, 0, 0]

# divide the voltage in 2 parts: down time: V=0. up time: V>0.
SCANS_DOWN = round((1-DUTY_CYCLE) * (SCANS - 1))
SCANS_UP = SCANS - SCANS_DOWN

TIME_UP = PULSE_WIDTH * DUTY_CYCLE
TIME_DOWN = PULSE_WIDTH - TIME_UP

time_per_scan_down = TIME_DOWN / SCANS_DOWN
time_per_scan_up = TIME_UP / SCANS_UP

scan_down_time_firstpart = [x * time_per_scan_down for x in range(round(SCANS_DOWN / 2))]
scan_up_time = [max(scan_down_time_firstpart) + x * time_per_scan_up for x in range(SCANS_UP)]
# scan_down_time_secondpart = [max(scan_up_time) + x * time_per_scan_down for x in range(round(SCANS_DOWN / 2))]