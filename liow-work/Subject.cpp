#include <algorithm>
#include "Subject.h"

Subject::Subject()
  : observes(0)
{}

void Subject::notify() const
{
  for (auto && e: observers)
  {
    e->update(this);
  }
}

ManSubject::ManSubject()
  : health_(health)
{}

void add_observer(const Observer* p const)
{
  observers.pushback(p);
}

void remove_observer(const Observer* p const)
{
  std::erase(observers, p);
}

int ManSubject::get_health() const
{
  return health_;
}

int ManSubject::set_health(int health)
{
  health_ = health;
}
