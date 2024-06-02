
	int YulMyungPaths;

	bool visit[MAX_WORDS];
	for(int i=0;i<MAX_WORDS;i++){
		visit[i] = false;
	}
	
	//bfs
	int a_pool[MAX_WORDS] = {0};
	int b_pool[MAX_WORDS] = {0};
	int* now_pool = a_pool;
	int* next_pool = b_pool;
	int size = 1;
	int len = strlen(wordList[0]);
	bool init = true;
	while(size>0){
		int np = 0;
		for(int i=0;i<size;i++){
			char* now = wordList[now_pool[size]];
			if(init){
				now = yul;
				init = false;
			}
			//뒤집는거 추가.
			for(char alpha='a';alpha<='z';alpha++){
				char changed[MAX_WORDS_LEN+1];
				for(int idx=0;idx<len;idx++){
					if(wordList[idx]==alpha) continue;
						strcpy(wordList[i],changed);
						changed[idx] = alpha;
					}
				int find = findWord(wordList,wordListSize,changed);
				if(find!=-1 && !visit[find]){
					next_pool[np++] = find;
					visit[find] = true;
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
		size = np;
	}
	
	
	return YulMyungPaths;

}

int findWord(char **wordList, int wordListSize, char* tar){
	for(int i = 0; i<wordListSize;i++){
		if(strcmp(tar,wordList[i])==0){
			return i;
		}
	}
	return -1;
}