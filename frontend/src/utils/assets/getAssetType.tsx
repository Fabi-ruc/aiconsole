// The AIConsole Project
//
// Copyright 2023 10Clouds
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import { Asset, AssetType, AssetTypePlural } from '@/types/assets/assetTypes';

export function getAssetType(asset?: Asset | AssetTypePlural): AssetType | undefined {
  if (typeof asset === 'string') {
    switch (asset) {
      case 'agents':
        return 'agent';
      case 'materials':
        return 'material';
      case 'chats':
        return 'chat';
      default:
        return undefined;
    }
  }

  if (asset) {
    // A bit hacky but effective way to distinguish between agent, materials and chats without introducing a new field

    if ('system' in asset) {
      return 'agent';
    }

    if ('content_type' in asset) {
      return 'material';
    }

    if ('last_modified' in asset) {
      return 'chat';
    }
  }

  return undefined;
}
