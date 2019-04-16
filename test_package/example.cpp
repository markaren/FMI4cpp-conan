
#include <fmi4cpp/fmi4cpp.hpp>

using namespace std;
using namespace fmi4cpp::fmi2;

int main() {

    auto fmuFile = "ControlledTemperature.fmu";
    auto fmu = fmu(fmuFile).as_cs_fmu();

    auto slave = fmu->new_instance();
    slave->setup_experiment();
    slave->enter_initialization_mode();
    slave->exit_initialization_mode();
    slave->step(1e-3);
    slave->terminate();

    return 0;

}
