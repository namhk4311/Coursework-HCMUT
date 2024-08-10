#include <iostream>
#include <string>
#include <stack>
#include <iomanip>
#include <cmath>
#include <sstream>
using namespace std;
int precedence(char c);
int precedence_logical(char c);
string Infix2Postfix(string infix);
string Infix2Prefix(string infix);
string PostfixPrefixCalculator(string input);
   
string LogicInfix2Postfix(string infix);
string LogicInfix2Prefix(string infix);
string LogicPostfixPrefixCalculator(string input,string varlue);