cmake_minimum_required(VERSION 3.20)

include(${CMAKE_CURRENT_LIST_DIR}/sorts/CMakeLists.txt)
include(${CMAKE_CURRENT_LIST_DIR}/utils/CMakeLists.txt)
include(${CMAKE_CURRENT_LIST_DIR}/data_structures/CMakeLists.txt)

set(SOURCES
    ${UTILS_SRC}
    ${DATA_STURCTURES_SRC}
    ${SORTS_SRC}
)