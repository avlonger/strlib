cmake_minimum_required(VERSION 2.8.4)
project(strlib)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")

add_executable(kmp src/kmp.c)
add_executable(duval src/duval.c)