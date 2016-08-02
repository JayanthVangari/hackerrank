import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
   static class Node
        {
        public char curalpha;
        public HashMap<Character,Node> child;
        public int count;
        public Node()
            {
            child=new HashMap<Character,Node>();
            }
    }
    static class Trie{
        private Node root;
         public Trie()
            {
            root=new Node();
        }
        void add(String word)
            { 
               Node current=root;
                for(int i=0;i<word.length();i++ )
                    {
                    Node children=current.child.get(word.charAt(i));
                    if(children==null)
                        {
                            Node node=new Node();
                            node.curalpha=word.charAt(i);
                            current.child.put(word.charAt(i),node);
                            node.count=1;
                            current=node;
                    }
                    else{
                        current=children;
                        current.count=current.count+1;
                        //System.out.println(current.count);
                    }
                 }
            
        }
         int find(String word)
             {
                Node current=root;
                for(int i=0;i<word.length();i++ )
                 {
                    if(current.child.get(word.charAt(i))==null)
                      {
                        return 0;
                      }
                    current=current.child.get(word.charAt(i));
             }
             return current.count;
        }
    }
    public static void main(String[] args) throws Exception {
        Trie t=new Trie();
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int in=Integer.parseInt(br.readLine());
            for(int i=0;i<in;i++)
            {
                String prob=br.readLine();
                String[] splt=prob.split(" ");  
                if(splt[0].contains("add"))
                 {
                    t.add(splt[1]);
                }
                if(splt[0].contains("find"))
                    {
                    System.out.println(t.find(splt[1]));
                }
                
        }
      }
}