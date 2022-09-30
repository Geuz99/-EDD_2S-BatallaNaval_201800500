cmake_minimum_required(VERSION 3.0.0)
set(CMAKE_TOOLCHAIN_FILE "C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake")
project(Fase2 VERSION 0.1.0)

include(CTest)
enable_testing()

INCLUDE_DIRECTORIES(
   C:/dev/vcpkg/installed/x86-windows/include
)
LINK_DIRECTORIES(
   C:/dev/vcpkg/installed/x86-windows/lib
)

add_executable(Fase2 main.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
