#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct _Node Node;

struct _Node{
	Node* child;
	Node* next;
	char alpha;
	int n_childs;
	int isEnd;
};


void insertWord(Node* node, char* word, int idx){
    
	if(idx==strlen(word)){
		node->isEnd = 1;
		return;
	}

    if(node->n_childs == 0){
        Node* newChild = (Node*) malloc(sizeof(Node));
        newChild->alpha = word[idx];
        node->child = newChild;
        insertWord(node->child, word, idx + 1);
        return;
    }

	Node* now = node->child;
	
	for(int i = 0; i< node->n_childs; i++){
		if(now->alpha == word[idx]){
			insertWord(now, word, idx + 1);
			return;
		}
        if(i+1 == node->n_childs){
            break;
        }
		if(now->next->alpha > word[idx]){
			Node* newChild = (Node*) malloc(sizeof(Node));
			newChild->alpha = word[idx];
			Node* orgNext = now->next;
			now->next = newChild;
			newChild->next = orgNext;
			node->n_childs++;
			insertWord(now->next, word, idx + 1);
			return;
		}
		if(i-1 < node->n_childs ){
			now = now->next;
		}
	}
	Node* newChild = (Node*) malloc(sizeof(Node));
	newChild->alpha = word[idx];
	now->next = newChild;
	insertWord(now->next, word, idx + 1);
	return;
}

int findMin(Node* nodes,char* word){
    int min = 0;
	for(int idx = 0; idx<strlen(word); idx++){
        Node* now = nodes;
        for(int i = 0; i< nodes->n_childs; i++){
            if(now->alpha == word[idx]){
                break;
            }
            if(i+1 == nodes->n_childs){
                return 1;
            }
            if(now->next->alpha > word[idx]){
                return 1;
            }
            if(i-1 < nodes->n_childs ){
                now = now->next;
            }
        }
        nodes = now->child;
    }
}

int main() {
	int N = 0;
	int M = 0;
	scanf("%d %d\n",&N,&M);
	
	Node nodes[10];
	
	for(int i = 0; i<N; i++){
		char* word = (char*)malloc(7);
		int k;

        scanf("%s %d\n",word,&k);

		insertWord(&nodes[k-1], word,0);
	}
    return 0;
	
	char word[10];
	
	int ans = 0;
	
	for(int i = 0; i<M; i++){
		scanf("%s",word);
		ans += findMin(nodes,word);
	}
	
	printf("%d\n",ans);
	
	return 0;
	
}
