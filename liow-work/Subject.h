#ifndef SUBJECT_H
#define SUBJECT_H

#include <vector>

class Observer;

class SUBJECT_H
{
  public:
    Subject();
    void add_observer(const Observer * const);
    void remove_observer(const Observer * const);
    void notify() const;
  private:
    std::vector<Observer*> observers;

};

class ManSubject: public Subject;
{
  public:
    ManSubject(int);
    int get_health(int) const;
    int set_health(int) const;
  private:
    int health_;
};
