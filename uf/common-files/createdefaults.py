#! /usr/bin/python
# Copyright 2018 Splunk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys
import uuid
import random
import base64

splunk_ansible_home = os.environ.get('SPLUNK_ANSIBLE_HOME')
splunk_ansible_inventory = os.path.join(splunk_ansible_home, "inventory")
sys.path.append(os.path.abspath(splunk_ansible_inventory))

splunk_hec_token = os.environ.get("SPLUNK_HEC_TOKEN", None)
splunk_password = os.environ.get("SPLUNK_PASSWORD", None)
splunk_idxc_secret = os.environ.get("SPLUNK_IDXC_SECRET", None)
splunk_shc_secret = os.environ.get("SPLUNK_SHC_SECRET", None)

def random_generator(size=24):
    # Use System Random for
    rng = random.SystemRandom()
    bytes = [chr(rng.randrange(256)) for i in range(size)]
    s = ''.join(bytes)

    return base64.b64encode(s)

# if there are no environment vars set, lets make some safe defaults
if not splunk_hec_token:
    tempuuid=uuid.uuid4()
    os.environ["SPLUNK_HEC_TOKEN"] = str(tempuuid)
if not splunk_password:
    os.environ["SPLUNK_PASSWORD"] = random_generator()
if not splunk_idxc_secret:
    os.environ["SPLUNK_IDXC_SECRET"] = random_generator()
if not splunk_shc_secret:
    os.environ["SPLUNK_SHC_SECRET"] = random_generator()
sys.argv.append("--write-to-stdout")
import environ
environ.main()

