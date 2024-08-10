#include "main.h"


//===================== START =========================

typedef unsigned long long ull;
int MAXSIZE = 0;
//==================== Object: Char_Frequency ===========
struct CharFreq {
    char character;
    int frequency;
};

//================== Huffman coding tree =================

class Huffnod{
	public:
		char letter;
		int val;
		int appearance;
		Huffnod *l;
		Huffnod *r;
	public:
		Huffnod(char c, int val, int appearance = 0, Huffnod *left = nullptr, Huffnod *right = nullptr) : letter(c), val(val), appearance(appearance), l(left), r(right) {}
		int root_val() const {
			return val;
		}
		char root_char() const {
			return letter;
		}
		bool isLeaf() {
			return (!this->l) && (!this->r);
		}
		~Huffnod() {}
};
// =================== helper Huffnod function ===========
class My_compare{
	public:
		bool operator() (Huffnod *a, Huffnod *b) {
			if (a->val == b->val) return a->appearance > b->appearance;
			return a->val > b->val;
		}
};

void deletenodeHufftree(Huffnod *&root) {
	if (!root) {
		return;
	}
	deletenodeHufftree(root->l);
	deletenodeHufftree(root->r);
	delete root;
}


//================== AVL tree ===========================
Huffnod* rotateLeft(Huffnod* root) {
	Huffnod *tmp = root;
	root = root->r;
	Huffnod* tmp2 = root->l;
	tmp->r = tmp2;
	root->l = tmp;
	return root;
}
Huffnod *rotateRight(Huffnod* root) {
	Huffnod *tmp = root;
	root = root->l;
	Huffnod *tmp2 = root->r;
	tmp->l = tmp2;
	root->r = tmp;
    return root;
}


int height(Huffnod *r) {
	if (r == nullptr) return 0;
	else {
		int lheight = height(r->l);
		int rheight = height(r->r);

		if (lheight > rheight) return lheight + 1;
		else return rheight + 1;
	}
}

int getBalance(Huffnod *root) {
	if (!root) return 0;
	return height(root->l) - height(root->r);
}

Huffnod *balanceLeft(Huffnod *root, int&count) {
	if (!root || count >= 3) return root;
	int b = getBalance(root);
	if (b <= -1) return rotateLeft(root);
	return root;
}

Huffnod *balanceRight(Huffnod *root, int&count) {
	if (!root || count >= 3) return root;
	int b = getBalance(root);
	if (b >= 1) return rotateRight(root);

	return root;
}

void balancetree(Huffnod *&root, int &count) {
	if (!root || count == 3) return;
	int b = getBalance(root);
    //cout << "balance: " << b << endl;
	if (b > 1) {
		root->l = balanceLeft(root->l, count);
		root = rotateRight(root);
		++count;
	}
	else if (b < -1) {
		root->r = balanceRight(root->r, count);
		root = rotateLeft(root);
		++count;
	}
    
 	balancetree(root->l, count);
	balancetree(root->r, count);
}


// =====================================================

Huffnod* makeTree(vector<CharFreq> &charOccur) {
	priority_queue<Huffnod *, vector<Huffnod*>, My_compare> pq;
	int counter = 0;
	int sizeChar = charOccur.size();
	for (int i = 0; i < sizeChar; i++) {
		pq.push(new Huffnod(charOccur[i].character,charOccur[i].frequency, counter++));
	}
	while (pq.size() > 1) {
		Huffnod *left_node = pq.top(); pq.pop(); 
		Huffnod *right_node = pq.top(); pq.pop();
		Huffnod *new_node = new Huffnod('~', left_node->val + right_node->val);
		new_node->l = left_node;
		new_node->r = right_node;
		int count = 0;
		int rotateMax = 3;
		while (rotateMax-- && count < 3) {
			balancetree(new_node, count);
		}
		new_node->appearance = counter++;
		pq.push(new_node);
	}
	Huffnod *res = pq.top(); pq.pop();
	if (res->letter != '~' && charOccur.size() > 1) {
		deletenodeHufftree(res);
		return nullptr;
	}
	else if (charOccur.size() == 1) {
		return res;
	}
	return res;
} 


class Hufftree{
	private:
		Huffnod *root;
	public:
		Hufftree() {root = nullptr;}
		void BuildTree(vector<CharFreq> &charOccur, int &success) {
			root = makeTree(charOccur);
			if (!root) {
				success = 0;
			}
			else if (root->isLeaf()) { //only 1 node
				success = -1;
			}
		}
		Huffnod *R() {return root;}
		void deleteTree(Huffnod *&root) {
			if (!root) {
				return;
			}
			deleteTree(root->l);
			deleteTree(root->r);

			delete root;
			
		}
	

		~Hufftree() {
			deleteTree(root);
			root = nullptr;
		}
};

//===================== Customer =============================
class Customer {
	public:
		string name;
		int Result;
		Hufftree *treeCus;
		Customer(){}
		Customer(string name, int Result, Hufftree *r) : name(name), Result(Result), treeCus(r) {}
		~Customer() {
			delete treeCus;
			
		}
		
};

//================== BINARY SEARCH TREE =======================
class BSTNode {
	public:
		Customer *r;
		BSTNode *pLeft;
		BSTNode *pRight;
	public:
		BSTNode(Customer *r) : r(r), pLeft(nullptr), pRight(nullptr) {}
		BSTNode() {}

		bool isLeaf() {
			return (this->pLeft == nullptr) && (this->pRight == nullptr);
		}
		~BSTNode() {
			delete r;
			
		}
};


class BSTtree {
	private:
		BSTNode *root;
		int num_of_node;
		queue<pair<string, int>> priority_order; 
		void deleteAllNode(BSTNode *&root) {
			if (!root) return;
			deleteAllNode(root->pLeft);
			deleteAllNode(root->pRight);
			delete root;
			
		}
		
		BSTNode *minValue(BSTNode *node) {
			BSTNode *curr = node;
			if (!curr) return nullptr;
			while (curr->pLeft != nullptr) {
				curr = curr->pLeft;
			}
			return curr;
		}

		BSTNode *insertNode(BSTNode *root, BSTNode *newnode) {
			if (!root) return newnode;
			if (newnode->r->Result < root->r->Result) {
				root->pLeft = insertNode(root->pLeft, newnode);
			}
			else if (root->r->Result <= newnode->r->Result) {
				root->pRight = insertNode(root->pRight, newnode);
			}
			return root;
		}

		BSTNode *removeNode(BSTNode *node, string name, int res) {
			if (!node) return nullptr;
			if (node->r->Result < res) {
				node->pRight = removeNode(node->pRight, name, res);
			}
			else if (node->r->Result > res) {
				node->pLeft = removeNode(node->pLeft, name, res);
			}
			else if (node->r->Result == res || node->r->name == name) {
				BSTNode *deletenode = node;
				if (node->isLeaf()) {
					node = nullptr;
				}
				else if (node->pRight == nullptr) {
					node = node->pLeft;
				}
				else if (node->pLeft == nullptr) {
					node = node->pRight;
				}
				else {
					BSTNode *temp = minValue(node->pRight);
					swap(temp->r, node->r);
					node->pRight = removeNode(node->pRight, name, res);
					return node;
				}
				delete deletenode;
				
 			}
			return node;
		}
		
		BSTNode *searchNode(BSTNode *rootsearch, string name, int res) {
			if (!rootsearch) return nullptr;
			if (rootsearch->r->name == name && rootsearch->r->Result == res) {
				return rootsearch;
			}
			else if (res < rootsearch->r->Result) {
				return searchNode(rootsearch->pLeft, name, res);
			}
			else if (res > rootsearch->r->Result) {
				return searchNode(rootsearch->pRight, name, res);
			}
			return nullptr;
		}
	
	public:		
		BSTtree() {root = nullptr; num_of_node = 0;}
		void insertintotree(BSTNode *newnode) {
			root = insertNode(root, newnode);
			priority_order.push(make_pair(newnode->r->name, newnode->r->Result));
			++num_of_node;
		}

		void deleteFIFO(ull Y) {
			if (Y < 0) return;
			Y = Y % MAXSIZE;
			if (Y >= (ull)num_of_node) {			
				deleteAllNode(root);
				root = nullptr;
				num_of_node = 0;
				while (!priority_order.empty()) priority_order.pop();
				return;
			}
			else {
				while (Y--) {
					string name = priority_order.front().first;
					int res = priority_order.front().second;
					priority_order.pop();
					
					BSTNode *found = searchNode(root, name, res);
					if (found) {
						deleteNodeinTree(name, res);
					}
				}
			}
		}

		BSTNode *Root() {
			return this->root;
		}

		int numOfGojoCus() const {
			return num_of_node;
		}

		int height(BSTNode *r) {
			if (r == nullptr) return 0;
			else {
				int lheight = height(r->pLeft);
				int rheight = height(r->pRight);

				if (lheight > rheight) return lheight + 1;
				else return rheight + 1;
			}
		}

		int getHeight() {
			return height(root);
		}

		void deleteNodeinTree(string name, int res) {
			this->root = removeNode(this->root, name, res);
			--num_of_node;
		}
		
		void clear() {
			if (num_of_node) {
				deleteAllNode(root);
				while (!priority_order.empty()) {
					priority_order.pop();
				}	
			}
			root = nullptr;
			num_of_node = 0;

		}

		~BSTtree() {
			clear();
		}
};


//=================== Gojo Restaurant: Hash Table ==========================
enum status {NIL = 0, NON_EMPTY = 1};


class GojoRestaurant {
	private:	
		int capacity;
		BSTtree **Gojoarea;
		status *update;
		int **postorderlist;
		int sizeGojoArea;
		int HashID(int result) {
			return result % capacity + 1;
		}
		void traversePostOrder(int *postorder, BSTNode *root, int &idx) {
			if (root) {
				traversePostOrder(postorder, root->pLeft, idx);
				traversePostOrder(postorder, root->pRight, idx);
				postorder[idx++] = root->r->Result;
			}
		}	
		
		ull Count(vector<int> &arr, vector<vector<ull>> &C) {
			int num_node = arr.size();
			if (num_node <= 2) return 1;
			vector<int> leftsub;
			vector<int> rightsub;
			int root = arr[0];
			for (int i = 1; i < num_node; i++) {
				if (arr[i] < root) leftsub.push_back(arr[i]);
				else rightsub.push_back(arr[i]);
			}
			long long num_node_left = leftsub.size();
			ull countleft = Count(leftsub, C);
			ull countright = Count(rightsub, C);
			return ((C[num_node - 1][num_node_left] * countleft) % MAXSIZE * countright) % MAXSIZE;
		}

		ull CountWays(vector<int> &arr) {
			int n = arr.size();
			vector<vector<ull>> C(n + 1, vector<ull>(n + 1));
			C[0][0] = 1;
			for (int i = 1; i <= n; i++) {
				C[i][0] = 1;
				for (int j = 1; j <= i; j++) {
					C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MAXSIZE;
				}
			}
			return Count(arr, C);
		}
		void printInOrderLIMITLESS(BSTNode *root) {
			if (root) {
				printInOrderLIMITLESS(root->pLeft);
				cout << root->r->Result << "\n";
				printInOrderLIMITLESS(root->pRight);
			}
		}

	public:
		GojoRestaurant(int MAXSIZE) {
			capacity = MAXSIZE;
			sizeGojoArea = 0;
			Gojoarea = new BSTtree*[capacity]; 
			update = new status[capacity]; 
			postorderlist = new int*[capacity]; 
			for (int i = 0; i < capacity; i++) {
				update[i] = NIL;
				Gojoarea[i] = nullptr;
			}
			
		}
		
		void InsertCustomer(Customer *cus) {
			int ID = HashID(cus->Result);
			if (update[ID - 1] == NIL) {
				Gojoarea[ID - 1] = new BSTtree();
				sizeGojoArea++;
 				update[ID - 1] = NON_EMPTY;
			}
			BSTNode *newnode = new BSTNode(cus);
			Gojoarea[ID - 1]->insertintotree(newnode);
		}

		void KOKUSENimplement() {
			for (int i = 0; i < capacity; i++) {
				if (update[i] == NON_EMPTY && Gojoarea[i]->numOfGojoCus()) {
					postorderlist[i] = new int[Gojoarea[i]->numOfGojoCus()]; 
					int idx = 0;
					traversePostOrder(postorderlist[i], Gojoarea[i]->Root(), idx);
					vector<int> reverseorder;
					for (int j = Gojoarea[i]->numOfGojoCus() - 1; j >= 0; j--) {
						reverseorder.push_back(postorderlist[i][j]);
					}
					ull result = CountWays(reverseorder);
					Gojoarea[i]->deleteFIFO(result);
					delete[] postorderlist[i];
					
				}
			}
		}

		void LIMITLESSimplement(int NUM) {
			if (1 <= NUM && NUM <= capacity) {
				if (update[NUM - 1] == NIL || !Gojoarea[NUM - 1]->numOfGojoCus()) {	
					return;
				}
				if (update[NUM - 1] == NON_EMPTY && Gojoarea[NUM - 1]->numOfGojoCus()) {
					printInOrderLIMITLESS(Gojoarea[NUM - 1]->Root());
				}		
			}
		}

		~GojoRestaurant() {
			for (int i = 0; i < capacity; i++) {
				if (update[i] == NON_EMPTY) {
					
					delete Gojoarea[i];
					
				}
			}
			delete[] postorderlist; 
			delete[] update; 
			delete[] Gojoarea; 
		}
};





//======================== Sukuna restaurant: Heap ============================
static ull first_appearance_Sukuna = 0;
class SuArea{
	public:
		int label;
		int updatePosInHeap = -1;
		ull appearance_order;
		deque<Customer*> area;
		int NUM;
		SuArea(int label, int updatePosInHeap) {
			this->updatePosInHeap = updatePosInHeap;
			appearance_order = 0;
			NUM = 0;
			this->label = label;
		}

		void insertSuCus(Customer *r) {
			area.push_back(r);
			++NUM;
		}

		void setNUM(int num) {
			NUM = num;
		}

		~SuArea() {
			while (area.size()) {
				Customer *tmp = area.front();
				area.pop_front();
				delete tmp;
				
			}
			NUM = 0;
			label = 0;
			appearance_order = 0;
		}
};

class AppearanceCompare {
	public: 
		bool operator() (SuArea *a, SuArea *b) {
			if (a->NUM == b->NUM) return a->appearance_order > b->appearance_order;
			return a->NUM > b->NUM;
		}
};

class SukunaRestaurant {
	private:
		SuArea **heap;
		status *update;
		int capacity;
		int sizeHeap;
		int countLabel = 0;
		int HashID(int result) {
			return result % capacity + 1;
		}

		void reHeapUp(int pos) {
			int n = (pos - 1) / 2;
			if (pos <= 0 || heap[n]->NUM < heap[pos]->NUM) {
				return;
			}
			else if (heap[n]->NUM > heap[pos]->NUM) {	
				swap(heap[n], heap[pos]);
				swap(heap[n]->updatePosInHeap, heap[pos]->updatePosInHeap);
				reHeapUp(n);
			}
		}

		void reHeapDown(int pos) {
			int l = 2 * pos + 1;
			int r = 2 * pos + 2;
			if (l < sizeHeap) {
				int smallest = l;
				if (r < sizeHeap && ((heap[r]->NUM < heap[smallest]->NUM) || (heap[r]->NUM == heap[smallest]->NUM && heap[r]->appearance_order < heap[smallest]->appearance_order))) { 
					smallest = r;
				}
				if (heap[pos]->NUM > heap[smallest]->NUM) {
					swap(heap[smallest], heap[pos]);
					swap(heap[smallest]->updatePosInHeap, heap[pos]->updatePosInHeap);
					reHeapDown(smallest);
				}
				else if (heap[pos]->NUM == heap[smallest]->NUM && heap[smallest]->appearance_order < heap[pos]->appearance_order) {
					swap(heap[smallest], heap[pos]);
					swap(heap[smallest]->updatePosInHeap, heap[pos]->updatePosInHeap);
					reHeapDown(smallest);
				}
			}
		}
		void PrintDQueCLEAVE(deque<Customer*> q, int ID, int NUM) {
			while (NUM-- && q.size()) {
				cout << ID << "-" << q.back()->Result << "\n";
				q.pop_back(); 
			}
		}

	public:
		SukunaRestaurant(int MAXSIZE){
			this->capacity = MAXSIZE;
			heap = new SuArea*[this->capacity]; 
			update = new status[this->capacity]; 
			sizeHeap = 0;
			for (int i = 0; i < this->capacity; i++) {
				heap[i] = nullptr;
				update[i] = NIL;
			}
		}
		
		void InsertCustomer(Customer *r) {
			int ID = HashID(r->Result); 
			if (update[ID - 1] == NIL) {
				if (sizeHeap == capacity) return;
				heap[sizeHeap] = new SuArea(ID, sizeHeap);
				heap[sizeHeap]->appearance_order = first_appearance_Sukuna++;
				heap[sizeHeap]->insertSuCus(r);
				update[ID - 1] = NON_EMPTY;
			}
			else if (update[ID - 1] == NON_EMPTY) {
				for(int i = 0; i < sizeHeap; i++) {
					if (heap[i]->label == ID) {
						heap[i]->appearance_order = first_appearance_Sukuna++;
						heap[i]->insertSuCus(r);
						reHeapDown(i);
						return;
					}
				}
			}
			reHeapUp(sizeHeap);
			++sizeHeap;
		}

		void KEITEIKENimplement(int NUM) {
			if (!sizeHeap) return;
			queue<pair<int, int>> printRes;
			
			priority_queue<SuArea*, vector<SuArea*>, AppearanceCompare> p;
			queue<SuArea*> pq;
			for (int i = 0; i < sizeHeap; i++) {
				p.push(heap[i]);
			}
			int sizeTodelete;
			if (sizeHeap < NUM) sizeTodelete = sizeHeap;
			else sizeTodelete = NUM;
			for (int i = 0; i < sizeTodelete; i++) {
				pq.push(p.top());
				p.pop();
			}
			while (p.size()) {
				p.pop();
			}
			
			while(!pq.empty()) {
				SuArea *tmp = pq.front(); pq.pop();
				
				if (tmp->NUM < NUM) {
					
					while (tmp->area.size()) {
						Customer *popout = tmp->area.front();
						tmp->area.pop_front();
						printRes.push(make_pair(popout->Result, tmp->label));
						delete popout;
						
					}
					tmp->NUM = 0;
				}
				else {
					for (int i = 1; i <= NUM; i++) {
						Customer *popout = tmp->area.front();
						tmp->area.pop_front();
						printRes.push(make_pair(popout->Result, tmp->label));
						delete popout;
						
						--tmp->NUM;
					}
				}
				tmp->appearance_order = first_appearance_Sukuna++;
				int idx = tmp->updatePosInHeap;
				int ID = heap[idx]->label;
				if (heap[idx]->NUM == 0) {
					swap(heap[idx], heap[sizeHeap - 1]);
					swap(heap[idx]->updatePosInHeap, heap[sizeHeap - 1]->updatePosInHeap);
					delete heap[sizeHeap - 1]; 
					heap[sizeHeap - 1] = nullptr;
					update[ID - 1] = NIL;
					--sizeHeap;
				}	
				reHeapDown(idx);
			}

			while (!printRes.empty()) {
				cout << printRes.front().first << "-" << printRes.front().second << endl;
				printRes.pop();
			}
		}

		void CLEAVEimplement(int idx, int NUM) {
			if (!sizeHeap) return;
			if (idx < sizeHeap) {
				PrintDQueCLEAVE(heap[idx]->area, heap[idx]->label, NUM);
				CLEAVEimplement(2 * idx + 1, NUM);
				CLEAVEimplement(2 * idx + 2, NUM);
			}
		}

		~SukunaRestaurant() {
			if (sizeHeap) {
				for (int i = 0; i < sizeHeap; i++) {
					delete heap[i];
					
				}
			}
			delete[] heap;
			delete[] update;
			
		}
};


//====================== Helper function ===================================
void Caesar(vector<CharFreq> &charOccur) {
	int sizeChar = charOccur.size();
	for (int i = 0;  i < sizeChar; i++) {
		char s = charOccur[i].character;
		if ('a' <= s && s <= 'z') {
			s = char(int(s + charOccur[i].frequency - 97) % 26 + 97);
		}
		else if ('A' <= s && s <= 'Z') {
			s = char(int(s + charOccur[i].frequency - 65) % 26 + 65);
		}
		charOccur[i].character = s;
	}
}

void getValue(Huffnod *root, string s, vector<pair<char, string>> &vtr) {
	if (!root) {
		return;
	}
	if (root->root_char() != '~') {
		vtr.push_back(make_pair(root->root_char(), s));
		return;
	}
	else {
		getValue(root->l, s + "0", vtr);
		getValue(root->r, s + "1", vtr);
	}	
}

char CaesarTranslate(char c, int freq) {
	if ('a' <= c && c <= 'z') {
		c = char(int(c + freq - 97) % 26 + 97);
	}
	else if ('A' <= c && c <= 'Z') {
		c = char(int(c + freq - 65) % 26 + 65);
	}
	return c;
}

int BtD(string binary, int i = 0) {
	int n = binary.length();
	int tot = 0;
	if (i < n) {
		if (binary[n - 1 - i] == '1') {
			tot = pow(2, i);
		}
		return tot + BtD(binary, ++i);
	}
	return 0;
}

bool compare2CharFreq(const CharFreq& a, const CharFreq& b) {
    if (a.frequency == b.frequency) {
        if (('a' <= a.character && a.character <= 'z') && ('A' <= b.character && b.character <= 'Z')) {
            return true;
        } else if (('a' <= a.character && a.character <= 'z') && ('a' <= b.character && b.character <= 'z')) {
            return a.character < b.character;
        } else if (('A' <= a.character && a.character <= 'Z') && ('A' <= b.character && b.character <= 'Z')) {
            return a.character < b.character;
        }
    }
    return a.frequency < b.frequency;
}

void sortCharacter(vector<CharFreq>& arr) {
    sort(arr.begin(), arr.end(), compare2CharFreq);
}

//============================================================

class Implement{
	private:
	GojoRestaurant *gojo;
	SukunaRestaurant *sukuna;
	string recentCustomer;
	int HashAlpha[52];
public:
	int BtD(string binary, int i = 0) {
		int n = binary.length();
		int tot = 0;
		if (i < n) {
			if (binary[n - 1 - i] == '1') {
				tot = pow(2, i);
			}
			return tot + BtD(binary, ++i);
		}
		return 0;
	}
	
	void initHashAlphabet() {
		memset(HashAlpha, 0, sizeof(HashAlpha));
	}
	
	void init() {
		gojo = new GojoRestaurant(MAXSIZE);
		sukuna = new SukunaRestaurant(MAXSIZE); 
	}
	
	Implement() {
		init();
	}
	
	void setHashAl(char c, int freq) {
		if ('A' <= c && c <= 'Z') {
			HashAlpha[c - 65] = freq;
		}
		else if ('a' <= c && c <= 'z') {
			HashAlpha[c - 97 + 26] = freq;
		}
	}
	
	int HashAl(char c) {
		if ('A' <= c && c <= 'Z') return HashAlpha[c - 65];
		if ('a' <= c && c <= 'z') return HashAlpha[c - 97 + 26];
		return -1;
	}

	void LAPSE(string name)	{
		if (name.length() < 3) return;
			string copy_recentCustomer = recentCustomer;
			recentCustomer = "";
			vector<CharFreq> charOccur;
			unordered_map<char, int> frequencyChar;
			//O(N)
			int nameSize = name.length();
			for (int i = 0; i < nameSize; i++) {
				if (frequencyChar.find(name[i]) == frequencyChar.end()) {
					frequencyChar.insert(make_pair(name[i], 1));
				}
				else frequencyChar[name[i]]++;
			}

			//kick out if no more than 3 differenent character
			if (frequencyChar.size() < 3) {
				recentCustomer = copy_recentCustomer;
				return;
			}
			for (unordered_map<char, int>::iterator it = frequencyChar.begin(); it != frequencyChar.end(); ++it) {
				charOccur.push_back({it->first, it->second});
			}
			int sizeChar = charOccur.size();

			for (int i = 0; i < sizeChar; i++) {
				setHashAl(charOccur[i].character, charOccur[i].frequency);
			}
			Caesar(charOccur);
			frequencyChar.clear();
			vector<CharFreq> listFreqEncrypted;
			//O(N)
			sizeChar = charOccur.size();
			for (int i = 0; i < sizeChar; i++) {
				if (frequencyChar.find(charOccur[i].character) == frequencyChar.end()) {
					frequencyChar.insert(make_pair(charOccur[i].character, charOccur[i].frequency));
				}
				else {
					frequencyChar[charOccur[i].character] += charOccur[i].frequency;
				}
			}
			for (unordered_map<char, int>::iterator it = frequencyChar.begin(); it != frequencyChar.end(); ++it) {
				listFreqEncrypted.push_back({it->first, it->second});
			}
			//O(NlogN)
			sortCharacter(listFreqEncrypted);
			
			Hufftree *tree = new Hufftree();
			int success = 1;
			vector<pair<char, string>> vtr;
			tree->BuildTree(listFreqEncrypted, success);
			if (!success) {
				delete tree; 
				recentCustomer = copy_recentCustomer;
				return;
			}
			else if (success == -1) {
				vtr.push_back(make_pair(tree->R()->letter, "0"));
				printHuff(tree->R(), recentCustomer);
			}
			else {
				getValue(tree->R(), "", vtr);
				printHuff(tree->R(), recentCustomer);
			}
			string nameEncrypted = "";
			
			unordered_map<char, string> HashCharacter_Res;
			int vtrsize = vtr.size();
			for (int i = 0; i < vtrsize; i++) {
				if (HashCharacter_Res.find(vtr[i].first) == HashCharacter_Res.end()) {
					HashCharacter_Res.insert(make_pair(vtr[i].first,vtr[i].second));
				}
			}

			//O(N^2)?
			for (int i = nameSize - 1; i >= 0; i--) {
				char s = CaesarTranslate(name[i], HashAl(name[i]));
				string res = HashCharacter_Res[s];
				reverse(res.begin(), res.end());
				nameEncrypted += res;
				if (nameEncrypted.length() >= 10) {
					nameEncrypted = nameEncrypted.substr(0, 10);
					break;
				}
			}

			int Result = BtD(nameEncrypted);
			Customer *newCus = new Customer(name, Result, tree);
			
			if (Result % 2) {
				gojo->InsertCustomer(newCus);
			}
			else {
				sukuna->InsertCustomer(newCus);
			}
	}	

	void KOKUSEN() {
		gojo->KOKUSENimplement();	
	}
	void LIMITLESS(int num){
		gojo->LIMITLESSimplement(num);
	}
	
	void KEITEIKEN(int num){
		sukuna->KEITEIKENimplement(num);
	}
	void CLEAVE(int num){
		int idx = 0;
		sukuna->CLEAVEimplement(idx, num);
	}

	void printHuff(Huffnod *root, string &str) {
		if (root) {
			printHuff(root->l, str);
			if (root->letter == '~') str += to_string(root->val) + "\n";
			else if (root->letter != '~') {
				str += root->letter;
				str += "\n";
			}
			printHuff(root->r, str);
		}
	}

	void HAND(){
		cout << recentCustomer;
	}
	~Implement() {
		delete gojo; 
		delete sukuna; 
	}
};



//======================= END ===========================
void simulate(string filename)
{
	ifstream ss(filename);
	string str, maxsize, name, num;
	Implement *r;
	ss >> str;
	ss >> maxsize;
	MAXSIZE = stoi(maxsize);
	r = new Implement();
	while(ss >> str) { 
		if (str == "LAPSE") {
			ss >> name;
			//cout << "LAPSE: " << name << endl;
			r->LAPSE(name);
		}
		else if (str == "KOKUSEN") {
			//cout << "KOKUSEN" << endl;
			r->KOKUSEN();
		}
		else if (str == "KEITEIKEN") {
			ss >> num;
			r->KEITEIKEN(stoi(num));
		}
		else if (str == "HAND") {
			r->HAND();
		}
		else if (str == "LIMITLESS") {
			ss >> num;
			r->LIMITLESS(stoi(num));
		}
		else if (str == "CLEAVE") {
			ss >> num;
			r->CLEAVE(stoi(num));
		}
	}
 	delete r;
	
}

