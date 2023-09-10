#
# Copyright © 2023 Github Lzhiyong
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

cmake_minimum_required(VERSION 3.14.2)

project(tree-sitter-grammer)

include_directories(
    ${PROJECT_SOURCE_DIR}/src/tree-sitter/lib/include
    )

add_library(tree-sitter SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter/lib/src/lib.c
    )

add_library(tree-sitter-bash SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-bash/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-bash/src/scanner.c
    )
    
add_library(tree-sitter-c SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-c/src/parser.c
    )

add_library(tree-sitter-cpp SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-cpp/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-cpp/src/scanner.c
    )
    
add_library(tree-sitter-cmake SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-cmake/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-cmake/src/scanner.c
    )
    
add_library(tree-sitter-c-sharp SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-c-sharp/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-c-sharp/src/scanner.c
    )

add_library(tree-sitter-go SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-go/src/parser.c
    )

add_library(tree-sitter-html SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-html/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-html/src/scanner.c
    )
    
add_library(tree-sitter-java SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-java/src/parser.c
    )
    
add_library(tree-sitter-javascript SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-javascript/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-javascript/src/scanner.c
    )
    
add_library(tree-sitter-json SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-json/src/parser.c
    )

add_library(tree-sitter-kotlin SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-kotlin/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-kotlin/src/scanner.c
    )
    
add_library(tree-sitter-lua SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-lua/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-lua/src/scanner.c
    )

add_library(tree-sitter-make SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-make/src/parser.c
    )
    
add_library(tree-sitter-markdown SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-markdown/tree-sitter-markdown/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-markdown/tree-sitter-markdown/src/scanner.c
    )
    
add_library(tree-sitter-python SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-python/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-python/src/scanner.c
    )
    
add_library(tree-sitter-query SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-query/src/parser.c
    )
    
add_library(tree-sitter-rust SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-rust/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-rust/src/scanner.c
    )

add_library(tree-sitter-smali SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-smali/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-smali/src/scanner.c
    )

add_library(tree-sitter-swift SHARED
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-swift/src/parser.c
    ${PROJECT_SOURCE_DIR}/src/tree-sitter-swift/src/scanner.c
    )
    
