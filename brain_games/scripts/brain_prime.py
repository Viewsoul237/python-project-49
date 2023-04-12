#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.prime_game import TASK_DESCRIPTION
from brain_games.games.prime_game import create_question_and_answer


def main():
    run_game(TASK_DESCRIPTION, create_question_and_answer)


if __name__ == "__main__":
    main()
