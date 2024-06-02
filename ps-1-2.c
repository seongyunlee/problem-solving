#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_WORD_LENGTH 5
#define MAX_WORDS 500


int findYulMyungPaths(const char *yul, const char *myung, char **wordList, int wordListSize);
int isOneDiff(char* a,char* b);
int findMyung(char** wordList,int wordListSize,char* myung);
int isReverse(char* a, char* b);

void clear_input_buffer();

int main() {
    char yul[MAX_WORD_LENGTH+1], myung[MAX_WORD_LENGTH+1];
	  char line[(MAX_WORDS+1)*(MAX_WORD_LENGTH + 1)+1];
    char *wordList[MAX_WORDS];
    int wordListSize = 0;

    printf("Enter yul: ");
    scanf("%s", yul);
    clear_input_buffer();  // Clear the newline left by scanf

    printf("Enter myung: ");
    scanf("%s", myung);
    clear_input_buffer();  // Clear the newline left by scanf


    printf("Enter words separated by spaces: ");
    if (fgets(line, sizeof(line), stdin)) {
        // Remove trailing newline, if any
        line[strcspn(line, "\n")] = 0;

        // Tokenize the input string
        char *token = strtok(line, " ");
        while (token != NULL && wordListSize < MAX_WORDS) {
            wordList[wordListSize] = malloc(strlen(token) + 1);
            if (wordList[wordListSize] == NULL) {
                fprintf(stderr, "Memory allocation failed\n");
                return 1;
            }
            strcpy(wordList[wordListSize], token);
            wordListSize++;
            token = strtok(NULL, " ");
        }
    }

    
    int result = findYulMyungPaths(yul, myung, wordList, wordListSize);
    printf("Total paths with minimum word transformation: %d\n", result);

    // Free allocated memory
    for (int i = 0; i < wordListSize; i++) {
        free(wordList[i]);
    }

    return 0;
}
void clear_input_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { }
}

int findYulMyungPaths(const char *yul, const char *myung, char **wordList, int wordListSize){

	int YulMyungPaths;

	int myung_idx = findMyung(wordList,wordListSize,myung);

	if(myung_idx==-1) return 0;

	bool visit[MAX_WORDS];
	for(int i=0;i<MAX_WORDS;i++){
		visit[i] = false;
	}
	
	//bfs
	char* a_pool[MAX_WORDS];
	char* b_pool[MAX_WORDS];
	char** now_pool = a_pool;
	char** next_pool = b_pool;
	a_pool[0] = yul;
	int size = 1;
	int len = strlen(wordList[0]);
	int ans = 0;
	while(size>0 && ans==0){
		int next_size = 0;
		for(int i=0; i < size; i++) {
			char* now = now_pool[i];
			for (int idx = 0; idx < wordListSize; idx++){
				if (visit[idx]) continue;
				if (isOneDiff(wordList[idx],now) || isReverse(wordList[idx],now)){
					next_pool[next_size++] = wordList[idx];
					if(idx==myung_idx){
						ans++;
					}
				}
			}
		}
		if(now_pool==a_pool){
			now_pool = b_pool;
			next_pool = a_pool;
		}
		else{
			now_pool = a_pool;
			next_pool = b_pool;
		}
		size = next_size;
	}
	
	
	return ans;

}


int isOneDiff(char* a, char* b) {
	int cnt = 0;
	for(int i =0; i<strlen(a); i++){
		if(a[i]!=b[i]){
			cnt+=1;
		}
		if (cnt == 2){
			return 0;
		}
	}
	return 1;
}

int isReverse(char* a, char* b){
	int len = strlen(a);
	for(int i = 0; i<len; i++){
		if(a[i]!=b[len-i-1]) return 0;
	}
	return 1;
}

int findMyung(char** wordList,int wordListSize,char* myung){
	for(int i = 0; i< wordListSize; i++){
		if (strcmp(myung,wordList[i])==0){
			return i;
		}
	}
	return -1;
}