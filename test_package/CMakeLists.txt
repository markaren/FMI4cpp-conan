cmake_minimum_required(VERSION 3.10)
project(FMI4cppTest)
set(CMAKE_CXX_STANDARD 17)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    message(FATAL_ERROR "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first!")
endif()

find_package(FMI4cpp CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example fmi4cpp::fmi4cpp)

file(COPY ControlledTemperature.fmu DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/bin)

enable_testing()
add_test(NAME example
      WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
      COMMAND example)
