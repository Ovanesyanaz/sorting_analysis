cmake_minimum_required(VERSION 3.20)

include(${CMAKE_CURRENT_LIST_DIR}/allocator/CMakeLists.txt)
include(${CMAKE_CURRENT_LIST_DIR}/error/CMakeLists.txt)
include(${CMAKE_CURRENT_LIST_DIR}/memory/CMakeLists.txt)
include(${CMAKE_CURRENT_LIST_DIR}/swap/CMakeLists.txt)
include(${CMAKE_CURRENT_LIST_DIR}/timer/CMakeLists.txt)

set(UTILS_SRC
    ${ALLOCATOR_SRC}
    ${ERROR_SRC}
    ${MEMORY_SRC}
    ${SWAP_SRC}
    ${TIMER_SRC}
)