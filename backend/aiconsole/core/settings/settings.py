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
import logging
from functools import lru_cache

from aiconsole.core.settings.fs.settings_file_storage import SettingsUpdatedEvent
from aiconsole.core.settings.settings_notifications import SettingsNotifications
from aiconsole.core.settings.settings_storage import SettingsStorage
from aiconsole.core.settings.utils.merge_settings_data import merge_settings_data
from aiconsole.utils.events import internal_events
from aiconsole_toolkit.settings.partial_settings_data import PartialSettingsData
from aiconsole_toolkit.settings.settings_data import SettingsData

_log = logging.getLogger(__name__)


class Settings:
    def configure(self, storage: SettingsStorage):
        from aiconsole.core.users.user import user_profile_service

        self.destroy()

        self._storage: SettingsStorage = storage
        self._settings_notifications: SettingsNotifications = SettingsNotifications()

        internal_events().subscribe(
            SettingsUpdatedEvent,
            self._when_reloaded,
        )

        user_profile_service().configure_user()

        _log.info("Settings configured")

    def destroy(self):
        if hasattr(self, "_storage"):
            self._storage.destroy()
            del self._storage
        if hasattr(self, "_settings_notifications"):
            del self._settings_notifications

        internal_events().unsubscribe(
            SettingsUpdatedEvent,
            self._when_reloaded,
        )

    async def _when_reloaded(self, SettingsUpdatedEvent):
        if not self._storage or not self._settings_notifications:
            raise ValueError("Settings not configured")

        await self._settings_notifications.notify()

    @property
    def unified_settings(self) -> SettingsData:
        if not self._storage or not self._settings_notifications:
            raise ValueError("Settings not configured")

        return merge_settings_data(self._storage.global_settings, self._storage.project_settings)

    def save(self, settings_data: PartialSettingsData, to_global: bool):
        if not self._storage or not self._settings_notifications:
            raise ValueError("Settings not configured")

        self._settings_notifications.suppress_next_notification()
        self._storage.save(settings_data, to_global=to_global)


@lru_cache
def settings() -> Settings:
    return Settings()
