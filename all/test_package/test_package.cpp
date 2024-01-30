#include "durak/game.hxx"
#include "durak/print.hxx"
#include <iostream>


int main() {
  auto game =durak::Game{{"player1","player2"}};
  if(game.getPlayers().size()!=2){
    std::terminate();
  }else{
    std::cout<<"works"<<std::endl;
  }
  return 0;
}
