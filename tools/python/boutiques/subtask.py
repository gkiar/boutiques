#!/usr/bin/env python

# Copyright 2015 - 2017:
#   The Royal Institution for the Advancement of Learning McGill University,
#   Centre National de la Recherche Scientifique,
#   University of Southern California,
#   Concordia University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import threading
import os.path as op
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Credit to:
# https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory
class subtaskWatcher:

    def __init__(self, watchdir):
        self.watchdir = watchdir
        self.observer = Observer()

    def run(self):
        event_handler = subtaskHandler()
        self.observer.schedule(event_handler, self.watchdir, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class subtaskHandler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            from boutiques import bosh

            fpath, fname = event.src_path, op.basename(event.src_path)
            print("Received created event - {}.".format(fname))

            ext = op.splitext(fname)[-1].upper()
            if ext == ".JSON":
                print("JSON Created - check compliance to subtask schema")
            elif ext == ".CBID":
                print("CBID Created - check record ID of subtask")

            # thing = threading.Thread(target=bosh, args=["--help"])
            # thing.start()

        elif event.event_type == 'modified':
            print("Received modified event - {}.".format(event.src_path))

