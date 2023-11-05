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
    
from fastapi import APIRouter
from starlette.responses import JSONResponse

from aiconsole.project_settings.project_settings import PartialSettingsAndToGlobal, get_aiconsole_settings

router = APIRouter()

@router.patch("")
async def patch(patch_data: PartialSettingsAndToGlobal):
    get_aiconsole_settings().save(settings_data=patch_data, to_global=patch_data.to_global)
    return JSONResponse({"status": "ok"})


@router.get("")
async def get():
    return JSONResponse(get_aiconsole_settings().model_dump())
