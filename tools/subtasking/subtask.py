#!/usr/bin/env python

from argparse import ArgumentParser
import random
import string
import json
import os


parser = ArgumentParser()
parser.add_argument("bids_app", action="store",
                    description="The CBRAIN `tool_class' for the BIDS app to run")
parser.add_argument("bids_dataset", action="store",
                    description="The BIDS dataset to process")
parser.add_argument("output_dir", action="store",
                    description="The directory for storing outputs")
bids_app, bids_dataset, output_dir = parser.parse_args()

subtask_obj = {
                "tool-class": bids_app,
                "description": "A {} BIDS app submission".format(bids_app),
                "share-wd-tid": "",
                "parameters": {
                    "bids_dir": bids_dataset,
                    "output_dir": output_dir,
                    "analysis_level": "",
                    "participant_label": ""
                },
                "required-to-post-process": True
              }


alvl = "participant"
for sub in [fl for fl in os.listdir(bids_dataset) if "sub-" in fl]:
    prefix = ".new-task-{}_{}".format(sub, random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=4))
    # modify the subtask obj
    # write file prefix.json out
    # wait for file prefix.cbid
    # submit task
    # record id from cbrain
    # add to list

alvl = "group"
# modify the subtask obj
# add all previous ids as dependencies
# generate and write new prefix.json out
# wait for prefix.cbid
# submit task
# record id from cbrain
