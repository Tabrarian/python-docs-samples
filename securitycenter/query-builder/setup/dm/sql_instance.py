# Copyright 2017 Google Inc. All rights reserved.
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
"""Creates a sql instance."""


def GenerateConfig(context):
    """Generate Deployment Manager configuration.

    Args:
      context: The context object provided by Deployment Manager.

    Returns:
      A config object for Deployment Manager (basically a dict with resources).
    """
    # Basic instance
    resources = [{
        'name': context.properties['name'],
        'type': 'sqladmin.v1beta4.instance',
        'properties': {
            'region': context.properties['region'],
            'settings': {
                'tier': context.properties['tier']
            }
        }
    }]

    return {
        'resources': resources
    }
