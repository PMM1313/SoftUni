from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def __add_object(object, col):
        if object not in col:
            col.append(object)

    def add_customer(self, customer: Customer):
        self.__add_object(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_object(trainer, self.trainers)

    def add_equipment(self, eq: Equipment):
        self.__add_object(eq, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_object(plan, self.plans)
        
    def add_subscription(self, sub: Subscription):
        self.__add_object(sub, self.subscriptions)
        
    def subscription_info(self, sub_id: int):
        subscription = next((s for s in self.subscriptions if s.id == sub_id), None)
        customer = next((c for c in self.customers if c.id == subscription.id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)

        plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)

        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)
        return "\n".join([repr(subscription),
                    repr(customer),
                    repr(trainer),
                    repr(equipment),
                    repr(plan)])



