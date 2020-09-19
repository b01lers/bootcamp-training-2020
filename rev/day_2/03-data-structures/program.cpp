#include <string>
#include <iostream>

enum class damage {
    OK,
    DAMAGED,
    CRITICAL,
    DESTROYED 
};

enum class shipclass {
    CARRIER,
    CRUISER,
    BATTLESHIP,
    FRIGATE,
    FIGHTER
};

class spaceship {
    public:
        spaceship(const char * name, const char * shipclass, int maxspeed) {
            this->name = std::string(name);
            this->cls = this->getclass(shipclass);
            this->maxspeed = maxspeed;
        }

        void hit(void) {
            switch(this->condition) {
                case damage::OK:
                    this->condition = damage::DAMAGED;
                case damage::DAMAGED:
                    this->condition = damage::CRITICAL;
                case damage::CRITICAL:
                    this->condition = damage::DESTROYED;
                    break;
                default:
                    return;
            }
        }

        void fly(int speed) {
            if (speed < this->maxspeed) {
                this->speed = speed;
            } else {
                this->speed = this->maxspeed;
            }
        }

        virtual void crash(void) {
            this->condition = damage::DESTROYED;
        }
    protected:
        shipclass getclass(const char * sclass) {
            if (std::string(sclass) == "CARRIER") {
                return shipclass::CARRIER;
            } else if (std::string(sclass) == "CRUISER") {
                return shipclass::CRUISER;
            } else if (std::string(sclass) == "BATTLESHIP") {
                return shipclass::BATTLESHIP;
            } else if (std::string(sclass) == "FRIGATE") {
                return shipclass::FRIGATE;
            } else if (std::string(sclass) == "FIGHTER") {
                return shipclass::FIGHTER;
            }
            throw std::exception();
        }
        std::string name;
        shipclass cls;
        int speed;
        damage condition;
        int maxspeed;

};

class spiritoffire : public spaceship {
    public:
        spiritoffire(const char * name) : spaceship(name, "CARRIER", 200) {
        }
        void crash(void) override {
            this->condition = damage::OK;
            std::cout << "YOU LOSE!" << std::endl;
        }
};

class forwarduntodawn : public spaceship {
    public:
        forwarduntodawn(const char * name) : spaceship(name, "CRUISER", 10000) {
        }
        void crash(void) override {
            this->condition = damage::OK;
            std::cout << "YOU WIN!" << std::endl;
        }
};

int main() {
    std::cout << "Which ship would you like to helm today, Chief?" << std::endl;
    std::cout << "Forward Unto Dawn or Spirit Of Fire?" << std::endl;
    std::string choice;
    std::getline(std::cin, choice);
    spaceship * s;
    if (choice == "Forward Unto Dawn") {
        std::cout << "So it is. Let us fly." << std::endl;
        s = new forwarduntodawn("Forward Unto Dawn");
    } else if (choice == "Spirit Of Fire") {
        std::cout << "Our hope goes with you." << std::endl;
        s = new spiritoffire("Spirit Of Fire");
    }
    std::cout << "Chief, we are crashing...please hold on." << std::endl;
    s->crash();

}
