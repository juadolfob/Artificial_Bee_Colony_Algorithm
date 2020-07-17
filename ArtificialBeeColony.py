# Artificial Bee Colony Algorithm

# Author:
# juadolfob

# Based on paper:
# Artificial Bee Colony (ABC) Optimization Algorithm for Solving Constrained Optimization Problems
# Dervis Karaboga, Erciyes Üniversitesi


import random
from collections import Iterable


class ABC:
    def __init__(self, objective_function, sn, bound, trial_limit, maximum_cycle_number):
        self.objective_function = objective_function
        self.bound = bound
        self.maximum_cycle_number = maximum_cycle_number
        self.trial_limit = trial_limit
        self.trial = [0] * sn

        self.solutions = \
            [
                [random.uniform(-bound, bound) for arg in range(self.objective_function.__code__.co_argcount)]
                for f in range(sn)
            ]
        self._eval_solutions()
        # main loop
        for c in range(self.maximum_cycle_number):
            # employed
            self._employed_phase()
            self._eval_prob()
            # onlookers
            self._onlookers_phase()
            # scouts

    @staticmethod
    def _fitness_function(function_f):
        if function_f >= 0:
            return 1 / (1 + function_f)
        else:
            return 1 + function_f

    def _eval_prob(self):
        sum_fit = sum(self.fit)
        self.prob = [self.fit[i] / sum_fit for i in range(len(self.solutions))]

    def eval_solution(self, solution):
        """
        Calculates objective_function and fitness_function values

        :return: (obj_fun_val, fit_fun_val)
        """
        if isinstance(solution, int):
            obj_val = self.objective_function(self.solutions[solution])
        elif isinstance(solution, Iterable):
            obj_val = self.objective_function(*solution)
        else:
            raise Exception("Expected solution to be int or Iterable, instead found ", type(solution))
        fit_val = ABC._fitness_function(obj_val)
        return obj_val, fit_val

    def _eval_solutions(self):
        self.function = list(map(lambda args: self.objective_function(*args), self.solutions))
        self.fit = list(map(ABC._fitness_function, self.function))

    def best_solution(self):
        i = self.fit.index(max(self.fit))
        return self.solution_detail(i)

    def worst_solution(self):
        i = self.fit.index(min(self.fit))
        return self.solution_detail(i)

    def solution_detail(self, i):
        # todo
        # remame function
        return {"solution": self.solutions[i], "function": self.function[i], "fitness": self.fit[i],
                "trial": self.trial[i]}

    # Produce new solution υi,j
    def _new_v_solution(self, i):
        # Randomly select a partner k (mutator) such that i != p
        k = random.choice([k for k in range(len(self.solutions)) if k != i])
        # Randomly select a variable j
        j = random.randrange(self.objective_function.__code__.co_argcount)
        # Generate new solution new_x and bound it
        xkj = self.solutions[k][j]
        xij = self.solutions[i][j]
        phi = random.uniform(-1, 1)
        new_xj = xij + phi * (xij - xkj)
        new_xj = self._bound(new_xj)
        new_solution = self.solutions[i][:]
        new_solution[j] = new_xj
        return new_solution

    def _new_x_solution(self, i):
        # Randomly select a variable j
        j = random.randrange(self.objective_function.__code__.co_argcount)
        # Generate new solution new_x and bound it
        xij = self.solutions[i][j]
        r = random.uniform(0, 1)
        new_xj = -self.bound + r * (self.bound - (-self.bound))
        new_xj = self._bound(new_xj)
        new_solution = self.solutions[i][:]
        new_solution[j] = new_xj
        return new_solution

    # todo implement for upper and lower bound
    def _bound(self, value):
        if value >= self.bound:
            return self.bound
        elif value <= -self.bound:
            return -self.bound
        return value

    def _accept_solution(self, i, new_solution, new_obj_val=None, new_fit_val=None):
        if not new_obj_val:
            new_fit_val = ABC._fitness_function(new_obj_val)
            if not new_fit_val:
                new_obj_val, new_fit_val = self.eval_solution(new_solution)
        self.solutions[i] = new_solution
        self.fit[i] = new_fit_val
        self.function[i] = new_obj_val
        self.trial[i] = 0

    # Phases
    def _employed_phase(self):
        for i in range(len(self.solutions)):
            new_solution = self._new_v_solution(i)
            self._general_phase(new_solution, i)

    def _onlookers_phase(self):
        for n in range(len(self.solutions)):
            i = random.choices(range(len(self.solutions)), weights=self.prob)[0]
            new_solution = self._new_v_solution(i)
            self._general_phase(new_solution, i)

    def _scout_phase(self, i):
        new_solution = self._new_x_solution(i)
        self._general_phase(new_solution, i)

    def _general_phase(self, new_solution, i=None):
        new_obj_val, new_fit_val = self.eval_solution(new_solution)

        if new_fit_val > self.fit[i]:
            self._accept_solution(i, new_solution, new_obj_val, new_fit_val)
        else:
            self.trial[i] += 1
            if self.trial[i] >= self.trial_limit:
                self.trial[i] = 0
                self._scout_phase(i)