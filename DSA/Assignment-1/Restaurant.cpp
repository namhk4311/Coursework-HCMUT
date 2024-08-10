#include "main.h"

const int INF = 2e9 + 7;


class imp_res : public Restaurant
{
	private:
		//customer *table;
		customer *X; //tail
		customer *front;
		customer *rear;

		customer *order_of_cus_front;
		customer *order_of_cus_rear;
		int order_size;

		int queue_size;
		int num_of_cus;
		int N_shellsort;
	public:	
		imp_res() {
			num_of_cus = 0;
			N_shellsort = 0;
			queue_size = 0;
			order_size = 0;
		};

		//============================SOME HELPER FUNCTION=================================
		/*1. CHECK NAME*/
		bool check_name_queue(const string& name) {
			if (!queue_size) return false;
			customer *tmp = front;
			while (tmp) {
				if (tmp->name == name) return true;
				tmp = tmp->next;
			}	
			return false;
		};

		bool check_name_table(const string&name) {
			customer *tmp = X;
			for (int i = 0; i < num_of_cus; i++) {
				if (tmp->name == name) return true;
				tmp = tmp->next;
			}
			return false;
		}

		/*2. ADD TO THE TABLE*/
		void insert(customer *r) {
			if (!num_of_cus) {
				X = r;
				++num_of_cus;
				return;
			}
			
			else if (num_of_cus < MAXSIZE / 2) {
				customer *tmp = X;
				if (num_of_cus == 1) {
					r->prev = tmp;
					r->next = tmp;
					tmp->next = r;
					tmp->prev = r;
				}
				else if (r->energy >= tmp->energy) {
					r->prev = tmp;
					r->next = tmp->next;
					tmp->next->prev = r;
					tmp->next = r;	
				}
				else {
					r->prev = tmp->prev;
					r->next = tmp;
					tmp->prev->next = r;
					tmp->prev = r;
				}

			} 

			else if (num_of_cus >= MAXSIZE / 2) {
				int res, count = 1, max_res = -1;
				customer *tmp = X;
				// 	//just fixed here
				if (num_of_cus == 1) {
					r->prev = tmp;
					r->next = tmp;
					r->next = r;
					tmp->prev = r;
				}
				else { // num >= 1
					for (int i = 0; i < num_of_cus; i++) {
						res = abs(r->energy - tmp->energy);
						max_res = max(max_res, res);
						tmp = tmp->next;
					}

					for (int i = 0; i < num_of_cus; i++) {
						res = abs(r->energy - tmp->energy);
						if (res == max_res) {
							if (r->energy < tmp->energy) { 
								r->prev = tmp->prev;
								r->next = tmp;
								tmp->prev->next = r;
								tmp->prev = r;
							}
							else {
								r->prev = tmp;
								r->next = tmp->next;
								tmp->next->prev = r;
								tmp->next = r;
							}
							break;
						}
						tmp = tmp->next;
					}
				}
				
			}
			X = r;
			++num_of_cus;
		}

		/*3. enqueue to queue and enqueue to time_order*/
		void enqueue(const string& name, const int& energy) {
			//cout << "queu check";
			if (!queue_size) {
				front = rear = new customer(name, energy, nullptr, nullptr);
			}
			else {
				if (queue_size == MAXSIZE) return;
				rear->next = new customer(name, energy, rear, nullptr);
				rear = rear->next;
			}
			++queue_size;
		}

		void insert_order(const string& name, const int& energy) {
			if (!order_size) {
				order_of_cus_front = order_of_cus_rear = new customer(name, energy, nullptr, nullptr);
			}
			else {
				if (order_size == 2 * MAXSIZE) return;
				order_of_cus_rear->next = new customer(name, energy, order_of_cus_rear, nullptr);
				order_of_cus_rear = order_of_cus_rear->next;
			}
			++order_size;
		}

		/*4. DEQUEUE ORDER*/
		void dequeue() {
			if (!queue_size) return;
			customer *tmp = front;
			if (queue_size == 1) {
				front = rear = nullptr;
			}
			else {
				front = front->next;
				front->prev = nullptr;
			}
			--queue_size;
			delete tmp;
		}

		void remove_first_order() { 
			
			if (!order_size) return;
			customer *tmp = order_of_cus_front;
			if (order_size == 1) order_of_cus_front = order_of_cus_rear = nullptr;
			else {
				order_of_cus_front = order_of_cus_front->next;
				order_of_cus_front->prev = nullptr;
			}
			delete tmp;
			--order_size;
		}

		/*5. DELETE ITEM IN THE TABLE AND QUEUE*/
		void get_out(customer *r, int table_or_queue) { //delete size at another place, not here
			if (!table_or_queue) { // remove people at the table
				customer *tmp = X;
				if (!num_of_cus) return;
				else if (num_of_cus == 1) {
					if (tmp->name == r->name && tmp->energy == r->energy) {
						delete tmp;
						X = nullptr;
					}
				}
				else {
					for (int i = 0; i < num_of_cus; i++) {
						//if (r != tmp) cout << r->name << endl;
						if (tmp->name == r->name && tmp->energy == r->energy) {
							tmp->next->prev = tmp->prev;
							tmp->prev->next = tmp->next;
							//RESET THE X
							if (tmp->energy > 0) X = tmp->next;
							else X = tmp->prev;
							//==============
							delete tmp;		
							break;
						}
						tmp = tmp->next;
					}
				}
				--num_of_cus;
			}
			else { //remove people at queue
				customer *tmp_queue = front;
				if (!queue_size) return;
				else if (queue_size == 1) {
					if (tmp_queue->name == r->name && tmp_queue->energy == r->energy) {
						front = rear = nullptr;
						delete tmp_queue;
					}
				}
				else {
					for (int i = 0; i < queue_size; i++) {
						customer *next_ptr = tmp_queue->next;
						if (tmp_queue->name == r->name && tmp_queue->energy == r->energy) {
							if (tmp_queue == rear) {
								rear = rear->prev;
								rear->next = nullptr;
							}
							else if (tmp_queue == front) {
								front = front->next;
								front->prev = nullptr;
							}
							else {
								if (tmp_queue->prev) tmp_queue->prev->next = tmp_queue->next;
								if (tmp_queue->next) tmp_queue->next->prev = tmp_queue->prev;
							}
							delete tmp_queue;
							break;
						}
						tmp_queue = next_ptr;
					}
				}
				--queue_size;
			}
		}

		/*6 SWAP AND SORT FUNCTION*/
		bool compare2Node(customer *former, customer *latter) {
			if (abs(former->energy) < abs(latter->energy)) return true;
			if (abs(former->energy) > abs(latter->energy)) return false;

			int idx = 0, idx1 = -1, idx2 = -1;
			bool update1 = false, update2 = false;
			customer *head_order = order_of_cus_front;
			while (head_order) {
				if (head_order->name == former->name && head_order->energy == former->energy) {
					idx1 = idx;
					update1 = true;
				}	
				else if (head_order->name == latter->name && head_order->energy == latter->energy) {
					idx2 = idx;
					update2 = true;
				}
				if (update1 && update2) break;
				head_order = head_order->next;
				++idx;
			}
			if (idx1 > idx2) return true;
			return false; 
		}

		void swap2Node(customer *&node1, customer *&node2) {
            if (node1->next == node2 && node2->prev == node1) {
				
                node2->prev = node1->prev;
                if (node1->prev) node1->prev->next = node2;
                node1->next = node2->next;
                if (node2->next) node2->next->prev = node1;
                node2->next = node1;
                node1->prev = node2;
                customer *tmp = node1;
                node1 = node2;
                node2 = tmp;
                return;
            }
			else if (node2->next == node1 && node1->prev == node2) {
				node1->prev = node2->prev;
				if (node2->prev) node2->prev->next = node1;
				node2->next = node1->next;
				if (node1->next) node1->next->prev = node2;
				node1->next = node2;
				node2->prev = node1;
				customer *tmp = node2;
				node2 = node1;
				node1 = tmp;
				return;
			}

            customer *tmp = node1;
			node1 = node2;
			node2 = tmp;

            
			customer *prev_1 = node1->prev;
			customer *next_1 = node1->next;

            
			if (prev_1) prev_1->next = node2; 
			if (next_1) next_1->prev = node2;
			node1->prev = node2->prev;
			node1->next = node2->next;
			if (node2->prev) node2->prev->next = node1;
			if (node2->next) node2->next->prev = node1;
			node2->prev = prev_1;
			node2->next = next_1;
		}

		void move_next_step(customer *&queue, int incr) {
			if (!queue) return;
			while (incr--) {
				queue = queue->next;
			}
		}

		void move_prev_step(customer *&queue, int incr) {
			if (!queue) return;
			while (incr--) {
				queue = queue->prev;
			} 
		}

		void inssort(customer *tmp, int n, int incr) {
            if (n == 1) return;
            customer *tmp1 = tmp;
            move_next_step(tmp1, incr);
            if (!tmp1) return;
            customer *node_i = tmp1;
            customer *tmp2 = tmp1;
            bool first_i = true;
            //int count = 0;
            for (int i = incr; i < n; i += incr) {
                if (!first_i) {
                    move_next_step(node_i, incr);
                    if (!node_i) break;
                    tmp1 = node_i;
                    tmp2 = tmp1;
                } 
                bool first = true;
                bool swap_ok = false;
                for (int j = i; (j >= incr); j -= incr) {
                    if (first) {
                        move_prev_step(tmp2, incr);
                        first = false;
                    }
                    else {
                        tmp1 = tmp2;
                        move_prev_step(tmp2, incr);
                    }

                    if (!tmp1 || !tmp2) break;
                    if (compare2Node(tmp2,tmp1)) {
					    if (tmp2 == front) {
                            front = tmp1;
                        }
                        if (tmp1 == rear) {
                            rear = tmp2;
                        }
                        if (tmp1 == node_i) {
                            node_i = tmp2;
                        }
                        swap2Node(tmp2, tmp1);
                        swap_ok = true;
						++N_shellsort;
                    }
                    
                }
                first_i = false;
            }
        }

		void shellSort(int n) {
            for (int gap = n / 2; gap > 2; gap /= 2) {
                customer *tmp = front;
				customer *node_j;
                for (int j = 0; j < gap; j++) {
                    node_j = tmp->next;
					inssort(tmp, n - j, gap);
 					tmp = node_j;
                }
            }
            customer *tmp = front;
            inssort(tmp, n, 1);
        }


		//=================================================

		void RED(string name, int energy)
		{
			if (!energy || check_name_queue(name) || check_name_table(name)) {
				return;
			}
			customer *cus = new customer (name, energy, nullptr, nullptr);
			
			if (num_of_cus < MAXSIZE) { //ADD TO THE TABLE
				 
				insert(cus);
				insert_order(cus->name, cus->energy);
			}
			
			else { //ADD TO THE QUEUE
				enqueue(cus->name, cus->energy);
				insert_order(cus->name, cus->energy);
				delete cus;
				cus = nullptr;
			}
		};
		

		
		void BLUE(int num)
		{
			if (!num_of_cus) return;
			customer *cus = order_of_cus_front;
			int num_copy = num;
			if (num >= num_of_cus || num >= MAXSIZE) {
				while (cus) {
					customer *next_ptr = cus->next;
					if (!num_of_cus) break;
					if (check_name_table(cus->name)) {
						get_out(cus, 0);
						if (cus == order_of_cus_front) {
							if (num_of_cus + queue_size == 0) {
								order_of_cus_front = order_of_cus_rear = nullptr;
								order_size = 0;
								delete cus;
								break;
							}
							else {
								cus->next->prev = nullptr;
								order_of_cus_front = cus->next;
							}
						}
						else if (cus == order_of_cus_rear) {
							if (num_of_cus + queue_size == 0) {
								order_of_cus_front = order_of_cus_rear = nullptr;
								order_size = 0;
								delete cus;
								break;
							}
							else {
								cus->prev->next = nullptr;
								order_of_cus_rear = cus->prev;
							}
						}
						else {
							if (cus->prev) cus->prev->next = cus->next;
							if (cus->next) cus->next->prev = cus->prev;
						}
						delete cus;
						--order_size;
					}
					cus = next_ptr;
				}
			}
			else {
				while (num_copy && cus) {
					customer *next_ptr = cus->next;
					if (!num_of_cus) break;
					if (check_name_table(cus->name)) {
						--num_copy;
						get_out(cus, 0);
						if (cus == order_of_cus_front) {
							if (num_of_cus + queue_size == 0) {
								order_of_cus_front = order_of_cus_rear = nullptr;
								order_size = 0;
								delete cus;
								break;
							}
							else {
								cus->next->prev = nullptr;
								order_of_cus_front = cus->next;
							}
						}
						else if (cus == order_of_cus_rear) {
							if (num_of_cus + queue_size == 0) {
								order_of_cus_front = order_of_cus_rear = nullptr;
								order_size = 0;
								delete cus;
								break;
							}
							else {
								cus->prev->next = nullptr;
								order_of_cus_front = cus->prev;
							}
						}
						else {
							if (cus->prev) cus->prev->next = cus->next;
							if (cus->next) cus->next->prev = cus->prev;
						}
						delete cus;
						--order_size;
					}
					cus = next_ptr;
				}		
			}

			while (queue_size && num_of_cus < MAXSIZE) { //just fixed num_of_cus
				string front_name = front->name;
				int front_energy = front->energy;
				customer *_cus_from_queue = new customer(front_name, front_energy, nullptr, nullptr);
				dequeue();  //TAKE OUT FIRST ELEMENT FROM THE QUEUE
				insert(_cus_from_queue); //ADD TO THE TABLE
			}
		}
		void PURPLE()
		{
			if (!queue_size) return;
			customer *tmp = front;
			N_shellsort = 0;
			int max_energy = -1, idx = 0, max_idx = 0;
			while (tmp != rear->next) {
				if (max_energy <= abs(tmp->energy)) {
					max_energy = abs(tmp->energy);
					max_idx = idx;
				}
				idx++;
				tmp = tmp->next;
			}
			
			shellSort(max_idx + 1);
			BLUE(N_shellsort % MAXSIZE);
		}

				
		void REVERSAL()
		{
			if (num_of_cus <= 1) return;
			//consider energy < 0
			customer *head = X;
			customer *tmp = X->next;
			customer *curr = head; 
			int cnt1 = 1, cnt2 = 1;
			while (1) {
				while (curr->energy > 0 && curr != tmp && cnt1 + cnt2 <= num_of_cus) {
					curr = curr->prev;
					cnt1++;
				}
				while (tmp->energy > 0 && curr != tmp && cnt1 + cnt2 <= num_of_cus) {
					tmp = tmp->next;
					cnt2++;
				}
				if (curr == tmp) break;
				if (curr->energy < 0 && tmp->energy < 0) {
					swap2Node(curr, tmp);
					if (tmp == X) X = curr; // chu y cho nay
				}
				curr = curr->prev; cnt1++;
				tmp = tmp->next; cnt2++;
				if (cnt1 + cnt2 > num_of_cus) break;
			}
			//consider energy > 0
			curr = X;
			tmp = X->next;
			cnt1 = 1, cnt2 = 1;
			while (1) {
				while (curr->energy < 0 && curr != tmp) {
					curr = curr->prev;
					cnt1++;
				}
				while (tmp->energy < 0 && curr != tmp) {
					tmp = tmp->next;
					cnt2++;
				}
				if (curr == tmp) break;
				if (curr->energy > 0 && tmp->energy > 0) {
					
					swap2Node(curr, tmp);
					if (tmp == X) X = curr;
				}
				curr = curr->prev; cnt1++;
				tmp = tmp->next; cnt2++;
                if (cnt1 + cnt2 > num_of_cus) break;
            }
			X = head;
		}
		
		void UNLIMITED_VOID()
		{
			if (num_of_cus < 4) return;
			customer *head = X;
			int sum = 0;
			int min_value = INF;
			customer *startIdx = nullptr;
			customer *endIdx = nullptr;
			int max_len = -1;
			for (int start = 0; start < num_of_cus; start++) {
				customer *curr = head;
				for (int i = 0; i < 4; i++) {
					sum += curr->energy;
					if (i < 3) curr = curr->next;
					
				}

				for (int len = 4; len <= num_of_cus; len++) {
					if (len != 4) sum += curr->energy; 
					//cout << sum << endl;
					if (min_value > sum) {
						startIdx = head;
						endIdx = curr;
						min_value = sum;
						max_len = len;
						//cout << min_value << endl;
					}
					else if (min_value == sum && max_len <= len) { // neu co nhieu day bang nhau thi chon day cuoi cung 
						startIdx = head;
						endIdx = curr;
						min_value = sum;
						max_len = len;
					}
					curr = curr->next;
				}
				
				head = head->next;
				sum = 0;
			}
			//cout << min_value << endl;
			customer *tmp = startIdx;
			int min_element = INF;
			customer *start_from_min = tmp;
			for (int i = 0; i < max_len; i++) {
				if (tmp->energy < min_element) { // tim phan tu dau tien cua day
					start_from_min = tmp;
					min_element = tmp->energy;
				}
				tmp = tmp->next;
			}
			if (start_from_min == startIdx) {
				while (start_from_min != endIdx) {
					start_from_min->print();
					start_from_min = start_from_min->next;
				}
				start_from_min->print();
			}
			else {
				customer *copy_s_f_m = start_from_min;
				while (start_from_min != endIdx) {
					start_from_min->print();
					start_from_min = start_from_min->next;
				}
				start_from_min->print();
				while (startIdx != copy_s_f_m) {
					startIdx->print();
					startIdx = startIdx->next;
				}
			}
		}



		void DOMAIN_EXPANSION() {
			if (num_of_cus == 0) return;
			customer *tmp = X;
			customer *tmp_queue = front;
			customer *stack_print_name = nullptr;
			int size_stack = 0;
			int sum_thuat_su = 0;
			int sum_abs_chu_linh = 0;
			for (int i = 0; i < num_of_cus; i++) {
				if (tmp->energy > 0) {
                    sum_thuat_su += tmp->energy;
                }
                else {
                    sum_abs_chu_linh += tmp->energy;
                    //check_chu_linh = true;
                }
                tmp = tmp->next;
			}
			
			for (int i = 0; i < queue_size; i++) {
				if (tmp_queue->energy > 0) {
					sum_thuat_su += tmp_queue->energy;
				}
				else sum_abs_chu_linh += tmp_queue->energy;
				tmp_queue = tmp_queue->next;  
			}
			if (sum_thuat_su >= abs(sum_abs_chu_linh)) {
				customer *oan_linh = order_of_cus_front;
				//int count = 1;
				int size1 = num_of_cus;
				while (oan_linh) {
					customer *next_ptr = oan_linh->next;
					if (oan_linh->energy < 0) {
						//add name to the stack for printing afterward
						if (!size_stack) { 
							stack_print_name = new customer(oan_linh->name, oan_linh->energy, nullptr, nullptr);
						}
						else {
							stack_print_name->next = new customer(oan_linh->name, oan_linh->energy, stack_print_name, nullptr);
							stack_print_name = stack_print_name->next;
						}
						++size_stack;
						//remove name from table
						if (check_name_table(oan_linh->name)) get_out(oan_linh, 0);
						else get_out(oan_linh, 1);
						//remove name from time order
						if (oan_linh == order_of_cus_front) {
							if (num_of_cus + queue_size == 0) {
								order_of_cus_front = order_of_cus_rear = nullptr;
								delete oan_linh;
								order_size = 0;
								break;
							}
							else {
								oan_linh->next->prev = nullptr;
								order_of_cus_front = oan_linh->next;
							}
						}
						else if (oan_linh == order_of_cus_rear) {
							if (num_of_cus + queue_size == 0) {
								order_of_cus_front = order_of_cus_rear = nullptr;
								delete oan_linh;
								order_size = 0;
								break;
							}
							else {
								oan_linh->prev->next = nullptr;
								order_of_cus_rear = oan_linh->prev;
							}
 						}
						else {
							if (oan_linh->prev) oan_linh->prev->next = oan_linh->next;
							if (oan_linh->next) oan_linh->next->prev = oan_linh->prev;
						}
						delete oan_linh;
						--order_size;
					}
					oan_linh = next_ptr;
					//++count;
				}
			}

			else {
				customer *thuat_su = order_of_cus_front;
				//int count = 1;
				int size1 = num_of_cus;
				while (thuat_su) {
					customer *next_ptr = thuat_su->next;
					if (thuat_su->energy > 0) {
						//add name to the stack for printing afterward
						if (!size_stack) { 
							stack_print_name = new customer(thuat_su->name, thuat_su->energy, nullptr, nullptr);
						}
						else {
							stack_print_name->next = new customer(thuat_su->name, thuat_su->energy, stack_print_name, nullptr);
							stack_print_name = stack_print_name->next;
						}
						++size_stack;
						//remove name from table
						if (check_name_table(thuat_su->name)) get_out(thuat_su, 0);
						else get_out(thuat_su, 1);
						if (thuat_su == order_of_cus_front) {
							if (num_of_cus + queue_size == 0) {
								order_of_cus_front = order_of_cus_rear = nullptr;
								delete thuat_su;
								order_size = 0;
								break;
							} 
							else {
								thuat_su->next->prev = nullptr;
								order_of_cus_front = thuat_su->next;
							}
						}
						else if (thuat_su == order_of_cus_rear) {
							if (num_of_cus + queue_size == 0) {
								order_of_cus_front = order_of_cus_rear = nullptr;
								delete thuat_su;
								order_size = 0;
								break;
							}
							else {
								thuat_su->prev->next = nullptr;
								order_of_cus_rear = thuat_su->prev;
							}
						}
						else {
							if (thuat_su->prev) thuat_su->prev->next = thuat_su->next;
							if (thuat_su->next) thuat_su->next->prev = thuat_su->prev;
						}
						delete thuat_su;
						--order_size;
					}
					thuat_su = next_ptr;
					//++count;
				}
			}
		
			while (queue_size && num_of_cus < MAXSIZE) { //ADD PEOPLE FROM QUEUE TO THE TABLE
				//string front_name = front->name;
				//int front_energy = front->energy;
				customer *_cus_from_queue = new customer(front->name, front->energy, nullptr, nullptr);
				dequeue(); 
				insert(_cus_from_queue);
			}

			while (size_stack) {
                customer *tmp = stack_print_name;
				stack_print_name->print();
				stack_print_name = stack_print_name->prev;
                delete tmp;
				--size_stack;
			}
            stack_print_name = nullptr;
		}
		
        void LIGHT(int num)
		{
			customer *cus = X;
			if (num > 0) {
				if (!num_of_cus) return; 
				else {
					cus->print();
					
					if (num_of_cus == 1) return; 
					else {
						cus = cus->next;
						while (cus != X) {
							cus->print();
							cus = cus->next;
						}
					}
				}
			}
			else if (num < 0) {
				if (!num_of_cus) return; 
				else {
					cus->print();
					if (num_of_cus == 1) return; 
					else {
						cus = cus->prev;
						while (cus != X) {
							cus->print();
							cus = cus->prev;
						}
					}
				}
			}
			else {
				customer *queue_line = front;
				int size = queue_size;
				if (!size) return;
				while (size) {
					queue_line->print();
					queue_line = queue_line->next;
					--size;
				}
			}
		}

		void clear() {
			for (int i = 0; i < num_of_cus; i++) {
				customer *tmp = X;
				if (i < num_of_cus - 1) X = X->next;
				delete tmp;
			}
			for (int i = 0; i < queue_size; i++) {
				customer *tmp = front;
				if (i < queue_size - 1) front = front->next;
				delete tmp;
			}
			for (int i = 0; i < order_size; i++) {
				customer *tmp = order_of_cus_front;
				if (i < order_size - 1) order_of_cus_front = order_of_cus_front->next;
				delete tmp;
			}
		}

		~imp_res() {
			clear();
			X = nullptr;
			front = rear = nullptr;
			order_of_cus_front = order_of_cus_rear = nullptr;
		}
};