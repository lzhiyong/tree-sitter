#!/usr/bin/env python
#
# Copyright © 2023 Github Lzhiyong
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# pylint: disable=not-callable, line-too-long, no-else-return

import os
import shutil
import argparse
import subprocess
from pathlib import Path
import zipfile

# package a directory as zip file
def package(srcPathName, destPathName):
    zip = zipfile.ZipFile(destPathName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirs, names in os.walk(srcPathName):
        fpath = path.replace(srcPathName, '')
 
        for filename in names:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))            
    zip.close()

def callback(args):
    arch = {'arm64-v8a' : 'aarch64', 'armeabi-v7a' : 'arm', 'x86_64' : 'x86_64', 'x86' : 'i686'}
        
    strip = Path(args.ndk) / 'toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-strip'
    workdir = Path.cwd() / args.build / 'lib'
    
    for library in workdir.glob('*.so'):
        subprocess.run('{} --strip-debug {}'.format(strip, library), shell=True)
    
    grammer = Path.cwd() / 'src/nvim-treesitter/queries'
    
    # package libtree-sitter-arch.zip file
    package(str(workdir), str(workdir.parent / 'libtree-sitter-{}.zip'.format(arch[args.abi])))
    # package tree-sitter-grammer.zip file
    package(str(grammer), str(workdir.parent / 'tree-sitter-{}.zip'.format('queries')))
    
def build(args):
    ndk = Path(args.ndk)
    cmake_toolchain_file = ndk / 'build/cmake/android.toolchain.cmake'
    if not cmake_toolchain_file.exists():
        raise ValueError('no such file or directory: {}'.format(cmake_toolchain_file))
        
    command = ['cmake', '-GNinja', 
        '-B {}'.format(args.build),
        '-DANDROID_NDK={}'.format(args.ndk),
        '-DCMAKE_TOOLCHAIN_FILE={}'.format(cmake_toolchain_file),
        '-DANDROID_PLATFORM=android-{}'.format(args.api),
        '-DCMAKE_ANDROID_ARCH_ABI={}'.format(args.abi),
        '-DANDROID_ABI={}'.format(args.abi),
        '-DCMAKE_SYSTEM_NAME=Android',
        '-DLIBRARY_OUTPUT_PATH=lib',
        '-DANDROID_ARM_NEON=ON',
        '-DCMAKE_BUILD_TYPE=Release']
    result = subprocess.run(command)
    result = subprocess.run(['ninja', '-C', args.build, '-j {}'.format(args.jobs)])
    
    # success
    if result.returncode == 0:
        callback(args)

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--ndk', required=True, help='set the ndk toolchain path')
    
    parser.add_argument('--abi', choices=['armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64'], 
      required=True, help='build for the specified architecture')
    
    parser.add_argument('--api', default=24, help='set android platform level, min api is 24')

    parser.add_argument('--build', default='build', help='the build directory')

    parser.add_argument('--jobs', default=16, help='run N jobs in parallel, default is 16')
    
    args = parser.parse_args()
    
    build(args)
    
if __name__ == "__main__":
    main()
    
