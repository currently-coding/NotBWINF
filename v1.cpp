#include <fstream>
#include <iostream>
#include <string>

std::string solve(std::string path) {
  std::ifstream file(path); // Open the file for reading
  if (file) {
    char ch;
    int score_a(0);
    int score_b(1);
    int index(0);
    while (file.get(ch)) { // Read each character one by one
      // Process the character
      //
      // test for non letter

      // test for uppercase
      //
      //
      // change score

      index++;
    }
    file.close(); // Close the file
  }
  return "a won - test text";
}
