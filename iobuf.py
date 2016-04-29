from spinnman.transceiver import create_transceiver_from_hostname
import sys

if len(sys.argv) < 3:
    print "iobuf.py <machine_name> <app_name>"
    sys.exit()

machine_name = sys.argv[1]
app_name = sys.argv[2]
if len(app_name) > 15:
    app_name = app_name[0:15]

found = False
transceiver = create_transceiver_from_hostname(
    machine_name, 0, auto_detect_bmp=False)
print "Getting CPU information ..."
cpu_information = transceiver.get_cpu_information()
print "Checking for instances of", app_name, "..."
for cpu_info in cpu_information:
    if cpu_info.application_name == app_name:
        iobuf = transceiver.get_iobuf_from_core(
            cpu_info.x, cpu_info.y, cpu_info.p)
        print iobuf
        found = True

if not found:
    print "No instances of", app_name, "found"
