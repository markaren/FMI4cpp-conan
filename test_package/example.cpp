
#include <fmi4cpp/fmi4cpp.hpp>

using namespace fmi4cpp::fmi2;

int main() {
    auto fmuFile = "ControlledTemperature.fmu";
    auto fmu = fmi2Fmu(fmuFile).asCoSimulationFmu();

    auto slave = fmu->newInstance();
    slave->setupExperiment();
    slave->enterInitializationMode();
    slave->exitInitializationMode();
    while (slave->getSimulationTime() <= 1.0) {
        slave->doStep(1e-3);
    }
    slave->terminate();
}
