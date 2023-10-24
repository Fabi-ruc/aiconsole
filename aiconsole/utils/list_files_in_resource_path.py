# The AIConsole Project
# 
# Copyright 2023 10Clouds
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
    
from aiconsole.utils.resource_to_path import resource_to_path


def list_files_in_resource_path(resource: str):
    """
    Recursively list all paths to files in path
    """

    abs_path = resource_to_path(resource)


    if not abs_path.exists():
        return

    for entry in abs_path.iterdir():
        if entry.is_file():
            yield entry
        else:
            yield from list_files_in_resource_path(str(entry).replace('/', '.'))
