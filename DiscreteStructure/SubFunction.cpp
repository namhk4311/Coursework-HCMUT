#include "Declaration.h"

int precedence(char c){
    if (c == '^') return 3;
    if (c == '*' || c == '/') return 2;
    if (c == '+' || c == '-') return 1;
    return 0;
}
int precedence_logical(char c){
    if (c == '~') return 4;
    if (c == '&' || c == '|') return 3;
    if (c == '-') return 2;
    if (c == '<') return 1; 
    return 0;
}
string Infix2Postfix(string infix){
    stack<char> s;
    string postfix,copy_infix;
    bool flag_sign = false;
    int length = infix.size(), cnt = 0, opening_parenthesis = 0, closing_parenthesis = 0; 
    for (int i = 0; i < length; i++){
        if (infix[i] != ' ') {
            copy_infix += infix[i];
            if (precedence(infix[i]) > 0) flag_sign = true;
        }
        if (infix[i] == ' ' && '0' <= infix[i + 1] && infix[i + 1] <= '9') {
            if (flag_sign == false) copy_infix += ' ';
            flag_sign = false;
        }
    }
    infix = copy_infix;
    length = infix.size();
    for (int i = 0; i < length; i++){
        if (infix[i] == '0' && infix[i + 1] == '^' && infix[i + 2] == '0') return "undefined error";
        if (precedence(infix[i]) > 1 && precedence(infix[i + 1]) > 1) return "undefined error"; //consecutive operator
        if (infix[i] == '.' && (infix[i + 1] < '0' || infix[i + 1] > '9')) return "syntax error"; // floating point
        if (precedence(infix[i]) > 0 && infix[i + 1] == ')') return "syntax error"; 
        if (infix[i] == ' ') return "syntax error"; //Blank
        if (infix[i] == '/' && infix[i + 1] == '0') return "divided-by-0 error";
        if ((infix[i] == '+' && infix[i + 1] == '+') || (infix[i] == '-' && infix[i + 1] == '-')) infix.replace(i, 2, "+");
        else if ((infix[i] == '-' && infix[i + 1] == '+') || (infix[i] == '+' && infix[i + 1] == '-')) infix.replace(i, 2, "-");
        if (infix[i] == '(') ++opening_parenthesis;
        else if (infix[i] == ')') ++closing_parenthesis;
    }
    if (opening_parenthesis != closing_parenthesis) return "syntax error";
    //length = infix.size();
    for (int i = 0; i < length; i++){
        if (('0' <= infix[i] && infix[i] <= '9') || infix[i] == '.'){
            postfix += infix[i]; ++cnt;
            if (cnt < length && (infix[i + 1] < '0' || infix[i + 1] > '9') && infix[i + 1] != '.') postfix += " "; 
        }
        else if (infix[i] == '('){
            s.push(infix[i]);
            ++cnt;
        }
        else if (infix[i] == ')'){
            ++cnt;
            while (!s.empty() && s.top() != '('){
                postfix += s.top();
                if (cnt <= length) postfix += " "; 
                s.pop();
            }
            if (!s.empty()) {
                s.pop();
                continue;
            }
            while (!s.empty()){ 
                postfix += s.top();
                if (cnt <= length) postfix += " "; 
                s.pop();
            }
        }
        else {
            ++cnt;
            while (!s.empty() && precedence(s.top()) >= precedence(infix[i])) { 
                postfix += s.top();
                if (cnt < length) postfix += " "; 
                s.pop();
            }
            s.push(infix[i]);
        }
    }
    while (!s.empty()) {
        if (cnt != length || infix[length - 1] != ')') postfix += " ";
        postfix += s.top();
        s.pop();
        ++cnt;
    }
    return postfix;
}
string Infix2Prefix(string infix){
    stack<char> s;
    string prefix, postfix, copy_infix = "";
    bool flag_sign = false;
    int length = infix.size(), cnt = 0, cnt_rev = 0, cnt_string = 0, opening_parenthesis = 0, closing_parenthesis = 0; 
    for (int i = 0; i < length; i++){
        if (infix[i] != ' ') {
            copy_infix += infix[i];
            if (precedence(infix[i]) > 0) flag_sign = true;
        }
        if (infix[i] == ' ' && '0' <= infix[i + 1] && infix[i + 1] <= '9') {
            if (flag_sign == false) copy_infix += ' ';
            flag_sign = false;
        }
    }
    infix = copy_infix;
    length = infix.size();
    for (int i = 0; i < length; i++){
        if (infix[i] == '0' && infix[i + 1] == '^' && infix[i + 2] == '0') return "undefined error";
        if (precedence(infix[i]) > 1 && precedence(infix[i + 1]) > 1) return "undefined error"; //consecutive operator
        if (infix[i] == '.' && (infix[i + 1] < '0' || infix[i + 1] > '9')) return "syntax error"; // floating point
        if (precedence(infix[i]) > 0 && infix[i + 1] == ')') return "syntax error"; //Parenthesis
        if (infix[i] == ' ') return "syntax error"; //Blank
        if (infix[i] == '/' && infix[i + 1] == '0') return "divided-by-0 error";
        if ((infix[i] == '+' && infix[i + 1] == '+') || (infix[i] == '-' && infix[i + 1] == '-')) infix.replace(i, 2, "+");
        else if ((infix[i] == '-' && infix[i + 1] == '+') || (infix[i] == '+' && infix[i + 1] == '-')) infix.replace(i, 2, "-");
        if (infix[i] == '(') ++opening_parenthesis;
        else if (infix[i] == ')') ++closing_parenthesis;
    }
    if (opening_parenthesis != closing_parenthesis) return "syntax error";

    char *infixreverse = new char[length + 1];
    for (int i = length - 1; i >= 0; i--){
        if (infix[i] == '(') infixreverse[cnt_rev++] = ')';
        else if (infix[i] == ')') infixreverse[cnt_rev++] = '(';
        else {
            infixreverse[cnt_rev++] = infix[i];
            ++cnt_string;
        } 
    }
    infixreverse[cnt_rev] = '\0';
     for (int i = 0; i < length; i++){
        if (('0' <= infixreverse[i] && infixreverse[i] <= '9') || infixreverse[i] == '.'){
            postfix += infixreverse[i]; ++cnt;
            if (infixreverse[i] == '.' && infixreverse[i + 1] == '.') return "syntax error";
            if ((infixreverse[i + 1] < '0' || infixreverse[i + 1] > '9') && cnt < cnt_string && infixreverse[i + 1] != '.') postfix += " "; 
        }
        else if (infixreverse[i] == '('){
            s.push(infixreverse[i]);
        }
        else if (infixreverse[i] == ')'){

            while (!s.empty() && s.top() != '('){
                postfix += s.top();
                ++cnt;
                if (cnt < cnt_string) postfix += " "; 
                s.pop();
            }
            if (!s.empty()) {
                s.pop();
                continue;
            }
            while (!s.empty()){
                postfix += s.top();
                ++cnt;
                if (cnt < cnt_string) postfix += " "; 
                s.pop();
            }
        }
        else { 
            while (!s.empty() && precedence(s.top()) > precedence(infixreverse[i])) {
                postfix += s.top();
                ++cnt;
                if (cnt < cnt_string) postfix += " "; 
                s.pop();
            }
            s.push(infixreverse[i]);
        }
    }
    while (!s.empty()) {
        postfix += s.top();
        s.pop();
        ++cnt;
        if (cnt < cnt_string) postfix += " ";
    }
    int length2 = postfix.size();
    for (int i = length2 - 1; i >= 0; i--){
        prefix += postfix[i];       
    }
    return prefix;
}
string PostfixPrefixCalculator(string input){
    stack<double> st;
    if (input == "syntax error") return "syntax error";
    else if (input == "undefined error") return "undefined error";
    else if (input == "divided-by-0 error") return "divided-by-0 error";
    string digit_string = "", output = "";
    int n = input.size();
    if (precedence(input[0]) == 0){
        for (int i = 0; i < n; i++){
            if (('0' <= input[i] && input[i] <= '9') || input[i] == '.'){
                    digit_string += input[i];
            } 
            else if (input[i] == ' ' && '0' <= input[i - 1] && input[i - 1] <= '9'){
                double num_digit = stod(digit_string);
                digit_string = "";
                st.push(num_digit);
            }
            else if (precedence(input[i]) > 0) {
                double op2 = st.top();
                st.pop();
                //if (op2 == 0.0 && input[i] == '/') return "divided-by-0 error";
                double op1 = st.top();
                st.pop();
                //if (op1 == 0.0 && op2 == 0.0 && input[i] == '^') return "undefined error";
                switch (input[i]){
                    case '+':
                        st.push(op1 + op2);
                        break;
                    case '-':
                        st.push(op1 - op2);
                        break;
                    case '*':
                        st.push(op1 * op2);
                        break;
                    case '/':
                        st.push(op1 / op2);
                        break;
                    case '^':
                        st.push(pow(op1,op2));
                        break;
                }
            } 
        }
    }
    else {
        for (int i = n - 1; i >= 0; i--){
            if (('0' <= input[i] && input[i] <= '9') || input[i] == '.'){
                digit_string += input[i];
            }
            else if (input[i] == ' ' && '0' <= input[i + 1] && input[i + 1] <= '9'){
                int k_pre = digit_string.size();
                string digit_string_rev = "";
                for (int j = k_pre - 1; j >= 0; j--){
                    digit_string_rev += digit_string[j];
                }
                double digit = stod(digit_string_rev);
                digit_string = "";
                st.push(digit);
                digit = 0.0;
            } 
            else if (precedence(input[i]) > 0) {
                double op1 = st.top();
                st.pop();
                double op2 = st.top();
                st.pop();
                //if (op2 == 0.0 && input[i] == '/') return "divided-by-0 error";
                //if (op1 == 0.0 && op2 == 0.0 && input[i] == '^') return "undefined error";
                switch (input[i]){
                    case '+':
                        st.push(op1 + op2);
                        break;
                    case '-':
                        st.push(op1 - op2);
                        break;
                    case '*':
                        st.push(op1 * op2);
                        break;
                    case '/':
                        st.push(op1 / op2);
                        break;
                    case '^':
                        st.push(pow(op1,op2));
                        break;
                }
            } 
        }
    }
    if (st.empty()) return digit_string;
    int digit_count, check = st.top();
    if (check == 0) digit_count = 0;
    else digit_count = log10(abs(st.top())) + 1;
    ostringstream k;
    k << setprecision(digit_count + 4) << st.top() << fixed;
    output = k.str();
    return output;
}

string LogicInfix2Postfix(string infix){
    stack<char> s;
    string postfix = "", op = "", infix_new = ""; 
    bool flag_implication = false, flag_equivalent = false;
    int implication_index = -1, equivalent_index = -1;
    int length = infix.size();

    for (int i = 0; i < length; i++){ 
        if (i == implication_index) flag_implication = false;
        if (i == equivalent_index) flag_equivalent = false;
        if ((!flag_equivalent || !flag_implication) && (infix[i] != '<' && infix[i] != '-' && infix[i] != '>')) {
            infix_new += infix[i];
            // cout << infix_new << " " << implication_index << endl;
        }
        else if (infix[i] == '<' && infix[i + 1] == '-' && infix[i + 2] == '>' && !flag_equivalent){
            
            infix_new += '<';
            flag_implication = true;
            implication_index = i + 3;
        }
        else if (infix[i] == '-' && infix[i + 1] == '>' && !flag_implication){
            infix_new += '-';
            flag_equivalent = true;
            equivalent_index = i + 2;
        }
    }
    //cout << infix_new << endl;
    int length2 = infix_new.size();
    for (int i = 0; i < length2; i++){
        if ('a' <= infix_new[i] && infix_new[i] <= 'z'){
            postfix += infix_new[i];
        }
        else if (infix_new[i] == '('){
            s.push(infix_new[i]);
        }
        else if (infix_new[i] == ' ') continue;
        else if (infix_new[i] == ')'){
            while (!s.empty() && s.top() != '('){
                if (s.top() == '-') postfix += "->";
                else if (s.top() == '<') postfix += "<->";
                else postfix += s.top();
                s.pop();
            }
            if (!s.empty()){
                s.pop();
            }
        }
        else{
            while(!s.empty() && precedence_logical(s.top()) >= precedence_logical(infix_new[i])){
                if (s.top() == '-') postfix += "->";
                else if (s.top() == '<') postfix += "<->";
                else postfix += s.top();
                s.pop();
            }
            s.push(infix_new[i]);
        }
    }
    while (!s.empty()){
        if (s.top() == '-') postfix += "->";
        else if (s.top() == '<') postfix += "<->";
        else postfix += s.top();
        s.pop();
    }
    return postfix;
}
string LogicInfix2Prefix(string infix){
    stack<char> s;
    string prefix = "", op = "", infix_new = "", postfix = ""; 
    bool flag_implication = false, flag_equivalent = false;
    int implication_index = -1, equivalent_index = -1;
    int length = infix.size();

    for (int i = 0; i < length; i++){ 
        if (i == implication_index) flag_implication = false;
        if (i == equivalent_index) flag_equivalent = false;
        if ((!flag_equivalent || !flag_implication) && (infix[i] != '<' && infix[i] != '-' && infix[i] != '>')) {
            infix_new += infix[i];
           
        }
        else if (infix[i] == '<' && infix[i + 1] == '-' && infix[i + 2] == '>' && !flag_equivalent){
             
            infix_new += '<';
            flag_implication = true;
            implication_index = i + 3;
        }
        else if (infix[i] == '-' && infix[i + 1] == '>' && !flag_implication){
            // cout << infix_new << " " << i << endl;
            infix_new += '-';
            flag_equivalent = true;
            equivalent_index = i + 2;
        }
    }    
    int infixnewlength = infix_new.size();
    string infixreverse = "";
    for (int i = infixnewlength - 1; i >= 0; i--){
        if (infix_new[i] == '(') infixreverse += ')';
        else if (infix_new[i] == ')') infixreverse += '(';
        else {
            infixreverse += infix_new[i];
        } 
    }
    //infixreverse[cnt_rev] = '\0';
    int newlength = infixreverse.size();
    // for (int i = 0; i < cnt_rev; i++) cout << infixreverse[i];
    // cout << endl;
    //cout << infixreverse << endl;
    for (int i = 0; i < newlength; i++){
        if ('a' <= infixreverse[i] && infixreverse[i] <= 'z'){
            postfix += infixreverse[i];
        }
        else if (infixreverse[i] == ' ') continue;
        else if (infixreverse[i] == '('){
            s.push(infixreverse[i]);
        }
        else if (infixreverse[i] == ')'){
            while (!s.empty() && s.top() != '('){
                if (s.top() == '-') postfix += ">-";
                else if (s.top() == '<') postfix += ">-<";
                else postfix += s.top();
                s.pop();
            }
            if (!s.empty()){
                s.pop();
            }
        }
        else{
            while(!s.empty() && precedence_logical(s.top()) > precedence_logical(infixreverse[i])){
                if (s.top() == '-') postfix += ">-";
                else if (s.top() == '<') postfix += ">-<";
                else postfix += s.top();
                s.pop();
            }
            s.push(infixreverse[i]);
        }
    }
     while (!s.empty()){
        if (s.top() == '-') postfix += ">-";
        else if (s.top() == '<') postfix += ">-<";
        else postfix += s.top();
        s.pop();
    }
    //cout << postfix << endl;
    int length2 = postfix.size();
    for (int i = length2 - 1; i >= 0; i--){
        prefix += postfix[i];
    }
    return prefix;
}
string LogicPostfixPrefixCalculator(string input,string varlue){
    stringstream ss(varlue);
    stack<bool> st;
    string infix_new = "";
    bool flag_equivalent = false, flag_implication = false;
    int lengthvarlue = varlue.size();
    char op[lengthvarlue];
    int num[lengthvarlue], cnt_num = 0, cnt_op = 0, implication_index = -1, equivalent_index = -1;
    char ans;
    while (ss >> ans){
        if ('a' <= ans && ans <= 'z') op[cnt_op++] = ans;
        else if ('0' <= ans && ans <= '9') num[cnt_num++] = ans - '0';
        // cout << ans << endl;
    }
    
    
    int length = input.size();
    for (int i = 0; i < length; i++){ 
        if (i == implication_index) flag_implication = false;
        if (i == equivalent_index) flag_equivalent = false;
        if ((!flag_equivalent || !flag_implication) && (input[i] != '<' && input[i] != '-' && input[i] != '>')) {
            infix_new += input[i];
        }
        else if (input[i] == '<' && input[i + 1] == '-' && input[i + 2] == '>' && !flag_equivalent){
            
            infix_new += '<';
            flag_implication = true;
            implication_index = i + 3;
        }
        else if (input[i] == '-' && input[i + 1] == '>' && !flag_implication){
            infix_new += '-';
            flag_equivalent = true;
            equivalent_index = i + 2;
        }
    }
    //cout << infix_new << " " << cnt_op << endl;
    int infixnewlength = infix_new.size();
    if (precedence_logical(input[0]) == 0){
        for (int i = 0; i < infixnewlength; i++){
            if ('a' <= infix_new[i] && infix_new[i] <= 'z'){
                for (int j = 0; j < cnt_op; j++){
                    if (op[j] == infix_new[i]){
                        (num[j] == 1) ? st.push(true) : st.push(false); 
                        break;
                    }
                }
            }
            else{
                bool num2 = st.top();
                st.pop();
                bool num1 = 0;
                if (!st.empty() && infix_new[i] != '~'){
                    num1 = st.top();
                    st.pop();
                }
                //cout << num1 << endl;
                switch(infix_new[i]){
                    case '~':
                        st.push(!num2);
                        break;
                    case '&':
                        st.push(num1 && num2);
                        //cout << "result:" <<  st.top() << endl;
                        break;
                    case '|':
                        st.push(num1 || num2);
                        break;
                    case '<':
                        st.push((num1 && num2) || (!num1 && !num2));
                        break;
                    case '-':
                        st.push(!num1 || num2);
                        break;
                }

            }
        }
    }
    else {
        for (int i = infixnewlength - 1; i >= 0; i--){
            if ('a' <= infix_new[i] && infix_new[i] <= 'z'){
                for (int j = 0; j < cnt_op; j++){
                    if (op[j] == infix_new[i]){
                        (num[j] == 1) ? st.push(true) : st.push(false); 
                        //st.push(num[j]);
                        break;
                    }
                }
            }
            else{
                bool num1 = st.top();
                st.pop();
                bool num2 = 0;
                if (!st.empty() && infix_new[i] != '~'){
                    num2 = st.top();
                    st.pop();
                }
                switch(infix_new[i]){
                    case '~':
                        st.push(!num1);
                        break;
                    case '&': 
                        st.push(num1 && num2);
                        break;
                    case '|':
                        st.push(num1 || num2);
                        break;
                    case '<':
                        st.push((num1 && num2) || (!num1 && !num2));
                        break;
                    case '-':
                        st.push(!num1 || num2);
                        break;
                }
            }
        }
    }
    if (st.empty()) return "error";
    if (st.top() == true) return "TRUE";
    return "FALSE";
} 
