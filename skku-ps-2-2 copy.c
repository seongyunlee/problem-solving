#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_MAP_SIZE 60000

typedef struct _HashNode HashNode;

typedef struct _Item{
	char* word;
	int degree;
} Item;

struct _HashNode {
	char key[7];
	Item* item;
	struct HashNode* next;
};

HashNode* hashMap[HASH_MAP_SIZE];

unsigned int hashFunction(const char* key, int idx){
	unsigned int hash = 0;

	for (int i = 0; i < idx; i++) {
		hash = (hash << 5) + *key++;
	}
	return hash % HASH_MAP_SIZE;
}

void initHashMap(){
	for(int i = 0; i<HASH_MAP_SIZE; i++){
		hashMap[i] = NULL;
	}
}

HashNode* createNode(const char* key, Item* item, int idx){
	HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
	snprintf(newNode->key, idx+1, "%s", key);
	newNode->item = item;
	newNode->next = NULL;
	return newNode;
}

void insertNode(const char* key, Item* item, int idx){
	unsigned int hash = hashFunction(key, idx);
	HashNode* newNode = createNode(key, item,idx);
	if(hashMap[hash] == NULL){
		hashMap[hash] = newNode;
	}else{
		HashNode* now = hashMap[hash];
		while(now->next != NULL){
			now = now->next;
		}
		now->next = newNode;
	}
}

Item* findNode(const char* key, int idx){

	unsigned int hash = hashFunction(key, idx);
	HashNode* now = hashMap[hash];

	while(now != NULL){
		if(strncmp(now->key, key, idx) == 0){
			return now->item;
		}
		now = now->next;
	}
	return NULL;
}

void printHashMap(){
	for(int i = 0; i<HASH_MAP_SIZE; i++){
		HashNode* now = hashMap[i];
		while(now != NULL){
			printf("<%d> %s %d ,%s\n",i, now->key, now->item->degree, now->item->word);
			now = now->next;
		}
	}
}




void insertWord(char* word, int priority){

	for(int i = 1; i<=strlen(word); i++){
		Item* item = findNode(word, i);
		if(item == NULL) {
			Item* newItem = (Item*)malloc(sizeof(Item));
			newItem->word = word;
			newItem->degree = priority;
			insertNode(word, newItem, i);
		}
		else if (item->degree < priority || (item->degree == priority && strcmp(item->word, word) > 0)) {
			item->degree = priority;
			item->word = word;
		}
	}
}

int findMin(char* word){

	for(int i = 1; i<strlen(word); i++){
		Item* item = findNode(word, i);

		if(item == NULL){
			return strlen(word);
		}
		if(strcmp(word, item->word) == 0){
			return i+1;
		}
	}
	return strlen(word);
}

int main() {
	int N = 0;
	int M = 0;
	scanf("%d %d\n",&N,&M);
	
	initHashMap();

	for(int i = 0; i<N; i++){
		char* word = (char*)malloc(7);
		int k;

        scanf("%s %d\n",word,&k);

		insertWord(word, k);
	}

	//printHashMap();
	
	char word[10];
	
	int ans = 0;
	
	for(int i = 0; i<M; i++){
		scanf("%s",word);
		int t = findMin(word);
		printf("%s %d\n",word,t);
		ans += t;
	}
	
	printf("%d\n",ans + M - 1);
	
	return 0;
	
}
