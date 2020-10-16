# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import get_entry


def test_get_entry(client, random_entry_name):
    # break entry name into parts
    name = client.parse_entry_path(random_entry_name)
    entry = get_entry.sample_get_entry(
        name["project"], name["location"], name["entry_group"], name["entry"]
    )
    assert entry.name == name
