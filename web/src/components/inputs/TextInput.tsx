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
    
import { ChangeEvent } from 'react';

import { cn } from '@/utils/styles';

interface SimpleInputProps {
  label: string;
  value: string;
  className?: string;
  onChange: (value: string) => void;
  placeholder?: string;
  disabled?: boolean;
}

export function SimpleInput({
  label,
  value,
  className,
  onChange,
  placeholder,
  disabled = false,
}: SimpleInputProps) {
  return (
    <>
      <label htmlFor={label} className="font-bold">
        {label}:
      </label>
      <textarea
        disabled={disabled}
        placeholder={placeholder}
        id={label}
        value={value}
        onChange={(e: ChangeEvent<HTMLTextAreaElement>) => {
          onChange(e.target.value);
        }}
        className={cn(
          className,
          'resize-none flex-none h-10 bg-black/20 appearance-none border border-transparent rounded w-full py-2 px-3 leading-tight placeholder-gray-400 focus:outline-none focus:border-primary/50 focus:shadow-outline',
        )}
      ></textarea>
    </>
  );
}
