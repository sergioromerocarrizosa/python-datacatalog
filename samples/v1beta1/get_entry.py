# -*- coding: utf-8 -*-
#
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

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-datacatalog

# sample-metadata
#   title:
#   description: Get Entry
#   usage: python3 samples/v1beta1/datacatalog_get_entry.py [--project_id "[Google Cloud Project ID]"] [--location_id "[Google Cloud Location ID]"] [--entry_group_id "[Entry Group ID]"] [--entry_id "[Entry ID]"]

# [START data_catalog_get_entry]
from google.cloud import datacatalog_v1beta1


def sample_get_entry(
    project_id: str, location_id: str, entry_group_id: str, entry_id: str
):
    """
    Get Entry

    Args:
      project_id (str): Your Google Cloud project ID
      location_id (str): Google Cloud region, e.g. us-central1
      entry_group_id (str): ID of the Entry Group, e.g. @bigquery, @pubsub, my_entry_group
      entry_id (str): ID of the Entry
    """

    client = datacatalog_v1beta1.DataCatalogClient()

    # project_id = '[Google Cloud Project ID]'
    # location_id = '[Google Cloud Location ID]'
    # entry_group_id = '[Entry Group ID]'
    # entry_id = '[Entry ID]'
    name = client.entry_path(project_id, location_id, entry_group_id, entry_id)

    entry = client.get_entry(request={"name": name})
    print(f"Entry name: {entry.name}")
    print(f"Entry type: {datacatalog_v1beta1.EntryType(entry.type).name}")
    print(f"Linked resource: {entry.linked_resource}")
    # [END data_catalog_get_entry]
    return entry


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--project_id", type=str, default="[Google Cloud Project ID]")
    parser.add_argument("--location_id", type=str, default="[Google Cloud Location ID]")
    parser.add_argument("--entry_group_id", type=str, default="[Entry Group ID]")
    parser.add_argument("--entry_id", type=str, default="[Entry ID]")
    args = parser.parse_args()

    sample_get_entry(
        args.project_id, args.location_id, args.entry_group_id, args.entry_id
    )


if __name__ == "__main__":
    main()