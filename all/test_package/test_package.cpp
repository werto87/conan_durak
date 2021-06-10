#include "durak/game.hxx"
#include "durak/print.hxx"
#include <iostream>


int main() {
	auto game =	durak::Game{{"player1","player2"}};
	std::cout << durak::attackingPlayerWithNameAndCardIndexValueAndType (game);
}
