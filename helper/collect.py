#!/usr/bin/env python3
'''!
Skript used to record the video frames. Trigger spurecorders to recording *.jpg images
'''

import socket
import json
import time
from random import randint

SPUREC_PORT = 4967
OUTPUT_PATH = "/tmp/"

def trigger_recording(SrcPort):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    recorder_id = "%d_" % SrcPort
    recCfg = {"RecorderId": recorder_id,
              "SrcUrl": "tcp://127.0.0.1:%d/VidSize=720x576" % SrcPort,
              "SubConfigEntries": [
                  {"SubTrigger": "Trigger", "Type": "Startup"}],
              "OutputPath": OUTPUT_PATH,
              "OutputType": "JPEG",
              "PrebufferTime": 0,
              "RundownTime": 3000}

    sock.connect(('localhost', SPUREC_PORT))

    print("Recording %d" % SrcPort)
    cmd_str = "addRecorderJson %s\n" % json.dumps(recCfg)
    sock.sendall(cmd_str.encode())
    time.sleep(recCfg["RundownTime"] * 1.05 / 1000)
    cmd_str = "delRecorder %s\n" % recorder_id
    sock.sendall(cmd_str.encode())
    sock.close()

if __name__ == "__main__":
    # list of vidoedecoder ports
    sources = [10106, 10206, 10306, 10406]

    while(True):
        for src in sources:
            try:
                trigger_recording(src)
            except Exception as inst:
                print(inst)
        delay = 5 * 60
        print("sleep for %d sec" % delay)
        time.sleep(delay)
