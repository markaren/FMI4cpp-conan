cmake_minimum_required(VERSION 3.10)
project(FMI4cppTest)
set(CMAKE_CXX_STANDARD 17)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    message(FATAL_ERROR "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first!")
endif()

if (MSVC)
    add_definitions("-DNOMINMAX" "-D_CRT_SECURE_NO_WARNINGS")
    add_compile_options(/wd4996) # suppress warning appearing in boost headers under MSVC.
    #https://docs.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-3-c4996?view=vs-2017
endif ()

find_package(fmi4cpp CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example fmi4cpp::fmi4cpp)

file(COPY ControlledTemperature.fmu DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY ControlledTemperature.fmu DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/bin)

enable_testing()
add_test(NAME example COMMAND example)
