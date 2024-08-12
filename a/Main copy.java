import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.run();
    }
}

    
class Pair {
        int r;
        int c;
    Pair(int r, int c){
            this.r = r;
            this.c = c;
    }
}

class State {
        int fruits = 0;
        Pair pos;
        
        State(int row, int col, int fruits){
            pos = new Pair(row,col);
            this.fruits = fruits;
        }
}

class Solution {

    int M,N;
    List<List<Integer>> trees;
    static int maxFruit = 20*20*100+1;

    static int[][] drdc = {
            {0,1},
            {0,-1},
            {1,0},
            {-1,0}
    };

    public boolean isValid(List<State> states, int[] moves){
        List<Integer> list = new ArrayList<Integer>();

        
        for(int i = 0; i < states.size(); i++){

            //print list
            int new_r = states.get(i).pos.r + drdc[moves[i]][0];
            int new_c = states.get(i).pos.c + drdc[moves[i]][1];
            if(!(0<=new_r && new_r < N && 0<= new_c && new_c < N)){
                return false;
            }
            for(Integer pos: list){
                if(pos == new_r * N + new_c ) return false;
            }
            list.add(new_r * N + new_c);
        }
        return true;
    }

    public void solve(List<Pair> pos){
        List<State> states = new ArrayList<>();
        
        for(int i=0; i<pos.size(); i++){
            states.add(new State(pos.get(i).r,pos.get(i).c, trees.get(pos.get(i).r).get(pos.get(i).c)));
            trees.get(pos.get(i).r).set(pos.get(i).c,0);
        }

         System.out.println(dfs(states,0));

    }


    public int dfs(List<State> states, int depth){

        if(depth == 3) return states.stream().mapToInt(state->state.fruits).sum();
        

        List<Integer> fruits = new ArrayList<>();

        int[] move = new int[M];
        Arrays.fill(move,0);
        while(true){
            if(!isValid(states,move)){
                if(!nextMove(move)) break;
                continue;
            }
            List<Pair> orgPos = new ArrayList<>();
            List<Integer> orgFruit = new ArrayList<>();
            
            for(int i = 0; i < M; i++){
                int new_r = states.get(i).pos.r + drdc[move[i]][0];
                int new_c = states.get(i).pos.c + drdc[move[i]][1];
                orgFruit.add(trees.get(new_r).get(new_c));
                orgPos.add(states.get(i).pos);
                states.get(i).pos = new Pair(new_r,new_c);
                states.get(i).fruits += trees.get(new_r).get(new_c);
                trees.get(new_r).set(new_c,0);
            }
            fruits.add(dfs(states,depth+1));
            for(int i = 0; i < M; i++){
                int org_r = orgPos.get(i).r;
                int org_c = orgPos.get(i).c;
                trees.get(states.get(i).pos.r).set(states.get(i).pos.c,orgFruit.get(i));
                states.get(i).fruits -= orgFruit.get(i);
                states.get(i).pos = orgPos.get(i);
            }
            if(!nextMove(move)) break;
        }
        int max = 0;
        for(int k: fruits){
            max = max < k ? k : max;
        }
        
        return  max;
    }   

    public boolean nextMove(int[] now){
        for(int i = 0; i<M; i++){
            if(now[i] == 3){
                now[i] = 0;
            }
            else{
                now[i]++;
                return true;
            }
        }
        return false;
    }
    
    public void run(){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        trees = new ArrayList<List<Integer>>();
        List<Pair> pos = new ArrayList<Pair>();
        
        for(int i = 0; i<N; i++){
            List<Integer> rows = new ArrayList<>();
            for(int j = 0; j<N; j++){
                rows.add(sc.nextInt());
            }
            trees.add(rows);
        }
        for(int i=0;i<M;i++){
            int x = sc.nextInt()-1;
            int y = sc.nextInt()-1;
            pos.add(new Pair(x,y));
        }

        solve(pos);

        
        
    }    

    
}
