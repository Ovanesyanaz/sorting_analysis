cmake_minimum_required(VERSION 3.20)
project(sorts VERSION 0.1.0 LANGUAGES C DESCRIPTION "famous sorts for use from python")

include(GNUInstallDirs)

# include(CTest)
# enable_testing()

set(TARGET "sorts")

set(PUBLIC_HEADERS
    sorts_python.h
)

set(INCLUDE_DIRECTORIES
    ${CMAKE_SOURCE_DIR}/include
    ${CMAKE_SOURCE_DIR}/source
)

include(${CMAKE_SOURCE_DIR}/source/CMakeLists.txt)

add_library(${TARGET} SHARED ${SOURCES})

set_target_properties(${TARGET} PROPERTIES
                      VERSION ${PROJECT_VERSION}
                      PUBLIC_HEADER ${PUBLIC_HEADERS})

target_include_directories(${TARGET} PRIVATE ${INCLUDE_DIRECTORIES})

install(TARGETS ${TARGET}
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
