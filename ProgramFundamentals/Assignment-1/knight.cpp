#include "knight.h"

const int inf = 2e9 +7;
int event[1000]; int MaxHP = 999, MaxLevel = 10, MaxRemedy = 99, MaxMaidenkiss = 99, MaxPhoenixdown = 99; 
string file_pack[3];

void Lowercase(string &pack)
{
    for (int i = 0; i < pack.length(); i++)
    {
        if (65 <= pack[i] && pack[i] <= 90) pack[i] = pack[i] - 65 + 97;
    }
}

void display(int HP, int level, int remedy, int maidenkiss, int phoenixdown, int rescue) 
{
    cout << "HP=" << HP
        << ", level=" << level
        << ", remedy=" << remedy
        << ", maidenkiss=" << maidenkiss
        << ", phoenixdown=" << phoenixdown
        << ", rescue=" << rescue << endl;
}

void knightcheck(string s, int &HP,int &level,int &remedy,int &maidenkiss, int &phoenixdown)
{    
    stringstream ss(s);
    ss >> HP >> level >> remedy >> maidenkiss >> phoenixdown;
    MaxHP = HP;
}

int event1_5damage(int event, int levelIO)
{
    int k; int res;
    int event1 = 10, event2 = 15, event3 = 45, event4 = 75, event5 = 95;
    switch (event)
    {
        case 1:
        {
            res = event1*levelIO;
            break; 
        } 
        case 2:
        {
            res = event2*levelIO;
            break;
        }
        case 3:
        {
            res = event3*levelIO;
            break;
        }
        case 4:
        {
            res = event4*levelIO;
            break;
        }
        case 5:
        {
            res = event5*levelIO;
            break;
        }
    }
    return res;
}

bool checkHPisprime(int HP) //Lancelot
{
    if (HP == 1) return false;
    else if (HP == 2) return true;
    else {
        for (int i = 2; i <= HP/2 + 1; i++)
        {
            if (HP % i == 0) return false;
        }
    }
    return true;
}

int fibonacci(int n)
{
    if (n < 2 && n > 0) return 1;
    if (n == 0) return 0;
    else return fibonacci(n - 1) + fibonacci(n - 2); 
}

int Fibocheck(int HP)
{
    int n = 0, res = 0;
    while (fibonacci(n) < HP && HP > 1)
    {
        res = fibonacci(n++);
    }
    if (HP == 1) res = 1;
    return res; 
}

bool checkmountUPshape(int a[], int initial, int end)
{
    int cntup = 1;
    for (int i = initial; i < end; i++)
    {
        if (a[i] < a[i + 1] && i + 1 != end) cntup++;
    }
    if (cntup == end - initial) {return true;}
    return false;
}

bool checkmountDOWNshape(int a[], int initial, int end)
{
    int cntdown = 1;
     for (int i = initial; i < end; i++)
    {
        if (a[i] > a[i + 1] && i + 1 != end) cntdown++;
    }
    if (cntdown == end - initial) {return true;}
    return false;
}

void check_Mush_Ghost(int event13, int &HP, int &phoenixdown)
{
    int lengthofindex13 = log10(event13) + 1;
    int arr[100];
    for (int i = lengthofindex13 - 1; i >= 0; i--){
        arr[i] = event13 % 10;
        event13 = event13/10;
    }
    int tmp = arr[0]*10 + arr[1];
    if (tmp == 13)
    {
        int n2 = -1, numn2[100]; 
        ifstream docfilemush;
        docfilemush.open(file_pack[0]); int cnt = 0, cnt_of_numn2 = 0;
            int TransArr[250], cnt_of_TransArr = 0;
            string numstring[250], stringn2;  
            docfilemush >> n2;
            docfilemush >> stringn2;
            for (int i = 0; i < stringn2.length(); i++)
            {
                if (stringn2[i] != ',') numstring[cnt] += stringn2[i];
                else if (stringn2[i] == ',') cnt++;                 
            }
            for (int i = 0; i <= cnt; i++)
            {
                stringstream(numstring[i]) >> numn2[cnt_of_numn2++];
            }
            for (int i = 0; i < cnt_of_numn2; i++) 
            {
                TransArr[cnt_of_TransArr++] = numn2[i];
            }
            for (int t = 0; t < cnt_of_TransArr; t++) //trans array
            {
                if (numn2[t] < 0) {TransArr[t] = -TransArr[t];}
                TransArr[t] = (17 * TransArr[t] + 9) % 257; 
            }
            
            for (int i = 2; i < lengthofindex13; i++) //bat dau check chuoi theo su kien arr[i] 
            {   
                if (arr[i] == 1)
                {
                    int maxi = -1, mini = -1, maxValue = -inf, minValue = inf;
                    for (int t = 0; t < cnt_of_numn2; t++)
                    {
                        if (numn2[t] > maxValue)
                        {
                            maxValue = numn2[t];
                            maxi = t; 
                        }
                        if (numn2[t] == maxValue && t > maxi)
                        {
                            maxi = t;
                        }
                        if (numn2[t] < minValue)
                        {
                            minValue = numn2[t];
                            mini = t; 
                        }
                        if (numn2[t] == minValue && t > mini)
                        {
                            mini = t;
                        }
                    }
                    HP = HP - (maxi + mini);
                }

                if (arr[i] == 2)
                {
                    int mtx, mti, maxValue_2 = -inf, maxi_2 = -1;
                    for (int t = 0; t < cnt_of_numn2; t++)
                    {
                        if (numn2[t] > maxValue_2)
                        {
                            maxValue_2 = numn2[t];
                            maxi_2 = t;
                        }
                    }
                    
                    if (checkmountUPshape(numn2, 0, maxi_2 + 1) && checkmountDOWNshape(numn2, maxi_2, cnt_of_numn2))
                    {
                        mtx = maxValue_2; mti = maxi_2;
                    }
                    else if (checkmountUPshape(numn2, 0, cnt_of_numn2))
                    {
                        mtx = numn2[cnt_of_numn2 - 1];
                        mti = cnt_of_numn2 - 1;
                    }
                    else if (checkmountDOWNshape(numn2, 0, cnt_of_numn2))
                    {
                        mtx = numn2[0];
                        mti = 0;
                    }
                    else 
                    {
                        mtx = -2;
                        mti = -3;
                    }
                  
                    HP = HP - (mtx + mti); 
                }

                if (arr[i] == 3)
                {
                    int maxValue2 = -inf, minValue2 = inf, maxi2 = inf, mini2 = inf;
                    for (int t = 0; t < cnt_of_TransArr; t++)
                    {
                        if (TransArr[t] > maxValue2) 
                        {
                            maxValue2 = TransArr[t];
                            maxi2 = t;
                        }
                        if (TransArr[t] == maxValue2 && t < maxi2)
                        {
                            maxi2 = t;
                        }
                        if (TransArr[t] < minValue2) 
                        {
                            minValue2 = TransArr[t];
                            mini2 = t;
                        }
                        if (TransArr[t] == minValue2 && t < mini2)
                        {
                            mini2 = t;
                        }
                    }
                    HP = HP - (maxi2 + mini2);
                }

                if (arr[i] == 4)
                {
                    int maxValue2 = -inf, minValue2 = inf, max2_3x = -inf, max2_3i = -1, flagsuccess = 0;
                    int indexrun;
                    if (cnt_of_TransArr >= 3) indexrun = 3;
                    else indexrun = cnt_of_TransArr;
                    for (int t = 0; t < indexrun; t++)
                    {
                        if (TransArr[t] >= maxValue2) 
                        {
                            maxValue2 = TransArr[t];
                        }
                    }
                    for (int t = 0; t < indexrun; t++)
                    {
                        if (TransArr[t] != maxValue2 && TransArr[t] > max2_3x)
                        {
                            max2_3x = TransArr[t]; 
                            max2_3i = t;
                        }
                       
                        if (TransArr[t] == max2_3x && t < max2_3i) 
                        {
                            max2_3i = t;
                        }
                    }
                    if (max2_3i == -1) {max2_3x = -5; max2_3i = -7;} 
                    HP = HP - (max2_3x + max2_3i);
                }
                if (HP > MaxHP) HP = MaxHP;
                if (HP <= 0 && phoenixdown > 0) 
                {
                    phoenixdown--;
                    HP = MaxHP;
                }
                else if (HP <= 0 && phoenixdown == 0) break; //check again
            }
        docfilemush.close();
    }
}

bool findMerlin(string s, string s1)
{
    for (int i = 0; i < s.length(); i++)
    {
        int j = 0; string tmp;
        while (j < s1.length())
        {
            tmp += s[i+j];
            j++;
        }
        if (tmp == s1) 
        {
            return true;
        }
    }
    return false;
}

void check_Merlin(int &HP)
{
    ifstream fileMerlin;
            fileMerlin.open(file_pack[2]);
                int n9, t = 1; 
                fileMerlin >> n9;
                while (t <= n9)
                {
                    string packstring;
                    fileMerlin >> packstring;
                    if (findMerlin(packstring,"Merlin") || findMerlin(packstring,"merlin")) HP += 3;
                    else {
                        Lowercase(packstring); 
                        string check6words; bool flag_m = false, flag_e = false, flag_r = false, flag_l = false, flag_i = false, flag_n = false;
                        for (int j = 0; j < packstring.length(); j++)
                        {                        
                            if (packstring[j] == 'm' && !flag_m)
                            {
                                check6words += packstring[j];
                                flag_m = true;
                            }
                            if (packstring[j] == 'e' && !flag_e)
                            {
                                check6words += packstring[j];
                                flag_e = true;
                            }
                            if (packstring[j] == 'r' && !flag_r)
                            {
                                check6words += packstring[j];
                                flag_r = true;
                            }
                            if (packstring[j] == 'l' && !flag_l)
                            {
                                check6words += packstring[j];
                                flag_l = true;
                            }
                            if (packstring[j] == 'i' && !flag_i)
                            {
                                check6words += packstring[j];
                                flag_i = true;
                            }
                            if (packstring[j] == 'n' && !flag_n)
                            {
                                check6words += packstring[j];
                                flag_n = true;
                            }
                        }
                        if (check6words.length() == 6)
                        {
                            HP += 2;
                        }
                    }
                    t++;
                }    
                if (HP > MaxHP) HP = MaxHP;
            fileMerlin.close();
}

void eventcheck(string s, int &HP, int &level, int &remedy, int &maidenkiss, int &phoenixdown, int &rescue, string file_pack[])
{
    int eventindex = -1, k = 0, currentLevel = -1, currentHP = -1; bool flagencounterevent19 = false, flagencounterevent18 = false, flagintial = false, flag999 = false;
    int flagevent6 = -1, flagevent7 = -1;
    bool Lancelot = false; 
    stringstream ss(s);
    while(ss >> eventindex) event[k++] = eventindex;
    if (checkHPisprime(HP)) {Lancelot = true;}
    for (int i = 0; i < k; i++)
    {
        bool skipflagevent6_7 = false;       
        if (i <= flagevent6 || i <= flagevent7) skipflagevent6_7 = true;
        if (HP == 999 && !flagintial)
        {
            flagintial = true;
            flag999 = true;
        }

        if (event[i] == 0) 
        {
            rescue = 1; 
            display(HP, level, remedy, maidenkiss, phoenixdown, rescue);
            break;
        } 

        // events from 1 to 5
        if (1 <= event[i] && event[i] <= 5)  
        {
            if (flag999 || Lancelot) 
            {
                level++; 
            }
            else {
                int b = (i + 1) % 10; 
                int levelIO = i + 1; // level of opponent
                (levelIO > 6) ? ((b > 5) ? levelIO = b : levelIO = 5) : levelIO = b;  
                if (level > levelIO) // win
                {
                    level++; 
                    if (level > 10) level = 10;
                }
                else if (level < levelIO)  // lose
                {
                    int tmp; tmp = event[i]; 
                    HP = HP - event1_5damage(tmp,levelIO);
                }
                if (HP <= 0 && phoenixdown == 0) 
                {
                    rescue = 0; 
                    display(HP, level, remedy, maidenkiss, phoenixdown, rescue);
                    break;
                }
                else if (HP <=0 && phoenixdown > 0)
                {
                    HP = MaxHP;
                    phoenixdown--;
                }
            }
        } 
        // event 6
        else if (event[i] == 6 && !skipflagevent6_7)  
        { 
            if (flag999 || Lancelot) 
            {
                level += 2;
            }
            else {
                int b = (i + 1) % 10; 
                int levelIO = i + 1; // level of opponent
                (levelIO > 6) ? ((b > 5) ? levelIO = b : levelIO = 5) : levelIO = b; 

                if (level > levelIO) // win
                {
                    level = level + 2; 
                    if (level > 10) level = 10;
                }
                else if (level < levelIO) // lose and tiny 
                {
                    flagevent6 = i + 3;
                    currentHP = HP;
                    if (HP >= 5) HP = HP/5;
                    else HP = 1;
                    if (remedy >= 1)
                    { 
                        flagevent6 = -1;
                        remedy--;
                        HP = currentHP;
                    }
                    if (HP <= 0 && phoenixdown > 0) 
                    {
                        flagevent6 = -1;
                        HP = MaxHP;
                        phoenixdown--;
                    }
                }   
            }   
        }

        // event 7 (Vajsh)
        else if (event[i] == 7 && !skipflagevent6_7)
        {
            if (flag999 || Lancelot) 
            {
                level = level + 2; 
            }
            else {
                int b = (i + 1) % 10; 
                int levelIO = i + 1; // level of opponent
                (levelIO > 6) ? ((b > 5) ? levelIO = b : levelIO = 5) : levelIO = b; 

                if (level > levelIO) 
                {
                    level = level + 2;
                    if (level > 10) level = 10;
                }
                else if (level < levelIO) 
                {
                    currentLevel = level;
                    flagevent7 = i + 3;
                    level = 1;
                    if (maidenkiss > 0)
                    {
                        flagevent7 = -1;
                        maidenkiss--;
                        level = currentLevel;
                    }
                }
            }
        }
        else if (event[i] == 11) // MushMario 
        {            
            int n1 = ((level + phoenixdown) % 5 + 1) * 3, intial = 99, s1 = 0;
            for (int i = 1; i <= n1; i++)
            {
                s1 += intial;
                intial -= 2;
            }
            HP = HP + (s1 % 100); 
            int checkPrimeHP = HP; bool HPprimeinitial = false; 
            while (checkPrimeHP <= MaxHP)
            {
                if (checkHPisprime(checkPrimeHP) != 1) ++checkPrimeHP;
                else if (checkHPisprime(HP) == 1 && !HPprimeinitial) // if HP itself is a prime number then add to the nearest primenumber 
                {
                    ++checkPrimeHP; 
                    HPprimeinitial = true;
                }    
                else {
                    HP = checkPrimeHP;
                    break;
                }
            }
            if (HP > MaxHP) HP = MaxHP;
        }
        else if (event[i] == 12) 
        {
            HP = Fibocheck(HP);
        }
        
        check_Mush_Ghost(event[i],HP,phoenixdown);
        if (event[i] == 15 && remedy < MaxRemedy)
        {
            remedy++;
            if (i < flagevent6)
            {
                remedy--; flagevent6 = -1; HP = currentHP; 
            }
        }
        else if (event[i] == 16 && maidenkiss < MaxMaidenkiss)
        {
            maidenkiss++;
            if (i < flagevent7) 
            {
                maidenkiss--; flagevent7 = -1; level = currentLevel;
            }
        }
        else if (event[i] == 17 && phoenixdown < MaxPhoenixdown)
        {
            phoenixdown++;
        }
        else if (event[i] == 18 && !flagencounterevent18)
        {
            flagencounterevent18 = true;
            check_Merlin(HP);
        }    
        else if (event[i] == 19 && !flagencounterevent19)
        {   
            flagencounterevent19 = true; bool lootRemedy = false, lootMaidenkiss = false;
            int r1, c1, pack1[100][100]; 
            ifstream fileap;
            fileap.open(file_pack[1]);
                fileap >> r1;
                fileap >> c1;
                for (int r = 0; r < r1; r++)
                {
                    for (int c = 0; c < c1; c++)
                    {
                        fileap >> pack1[r][c];
                    }
                }

                for (int r = 0; r < r1; r++) //check loot
                {
                    int loot = 0;
                    for (int c = 0; c < c1; c++)
                    {
                        if (pack1[r][c] == 16 && loot < 3) //remedy
                        { 
                            ++remedy; ++loot;
                            lootRemedy = true;
                        }
                        else if (pack1[r][c] == 17 && loot  < 3) //maidenkiss
                        {
                            ++maidenkiss; ++loot;
                            lootMaidenkiss = true;
                        }
                        else if (pack1[r][c] == 18 && loot < 3) //phoenixdown
                        {
                            ++phoenixdown; ++loot;
                        }
                    }
                }
                
                if (remedy > MaxRemedy) remedy = MaxRemedy;
                if (phoenixdown > MaxPhoenixdown) phoenixdown = MaxPhoenixdown;
                if (maidenkiss > MaxMaidenkiss) maidenkiss = MaxMaidenkiss;
                
                if (i < flagevent6 && lootRemedy)
                {
                    remedy--; flagevent6 = -1; HP = currentHP; 
                }
                if (i < flagevent7 && lootMaidenkiss) 
                {
                    maidenkiss--; flagevent7 = -1; level = currentLevel;
                }
        }
        else if (event[i] == 99)
        {
            if (flag999 || (Lancelot && level >= 8) || level == 10)
            {
                level = 10;
            }
            else {
                rescue = 0;
                display(HP, level, remedy, maidenkiss, phoenixdown, rescue);
                break;
            }
        }   
         //after pass 3 events and get back to normal
        if (i == flagevent6) 
        {
            HP *= 5; 
            if (HP > MaxHP) HP = MaxHP;
        }

        else if (i == flagevent7)
        {
            level = currentLevel;
        }

        if (HP <= 0) 
        {
            rescue = 0; 
            display(HP, level, remedy, maidenkiss, phoenixdown, rescue);
            break;
        }
        if (rescue == -1 && i == k - 1) rescue = 1;  
        if (level > 10) level = 10;
        display(HP, level, remedy, maidenkiss, phoenixdown, rescue);
    }
}

void filecheck(string s)
{
    int cnt = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] != ',') file_pack[cnt] += s[i]; 
        else cnt++;
    }
    cnt++;
}

void inputData(string file_input, int &HP, int &level, int &remedy, int &maidenkiss, int &phoenixdown, int &rescue)
{
    rescue = -1;
    ifstream ipp;
    ipp.open(file_input);
        string info, events, nfile;
        getline(ipp,info);
        getline(ipp,events);
        getline(ipp,nfile);
        knightcheck(info, HP, level, remedy, maidenkiss, phoenixdown);
        filecheck(nfile);
        eventcheck(events, HP, level, remedy, maidenkiss, phoenixdown, rescue, file_pack);
    ipp.close();
}

void adventureToKoopa(string file_input, int & HP, int & level, int & remedy, int & maidenkiss, int & phoenixdown, int & rescue) 
{
        inputData(file_input, HP, level, remedy,maidenkiss, phoenixdown, rescue);
}