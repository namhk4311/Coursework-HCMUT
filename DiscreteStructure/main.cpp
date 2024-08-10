#include "SubFunction.cpp"

int main(){
    string infixMath; //= "(987+(654*(321/123)))^2-(456+789)";
    string infixLogic; //= "~t->t&~w|(z&(p&(w&(p|p&q)|y&z&z)<->x&(~p|z)&~y))";
    string varlue; //= "t w z p q y x 1 1 1 1 1 1 1";
    cout << "input infixMath: ";
    getline(cin, infixMath);
    cout << "input infixLogic: ";
    getline(cin, infixLogic);
    cout << "input variable value: ";
    getline(cin, varlue);
    cout << "\nMath infix: " << infixMath
         << "\nPostfix: " << Infix2Postfix(infixMath)
         << "\nPrefix: " << Infix2Prefix(infixMath)
         << "\nCalculator: " << PostfixPrefixCalculator(Infix2Postfix(infixMath))
         << "\n"
         << "\nLogic infix: " << infixLogic << ", variable value: " << varlue
         << "\nPostfix: " << LogicInfix2Postfix(infixLogic)
         << "\nPrefix: " << LogicInfix2Prefix(infixLogic)
         << "\nCalculator: " << LogicPostfixPrefixCalculator(LogicInfix2Postfix(infixLogic),varlue);
    return 0;
}