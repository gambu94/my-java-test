package Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.me.giuseppe;
import com.me.alessandro;
import com.me.Target;


public class Target {

    private static class Person {
        private String nome;
        private int eta;

        public Person(String n, int e) {
            nome = n; eta = e;
        }

        public String getNome() {
            return nome;
        }

        public int getEta() {
            return eta;
        }

        public void print(){
            System.out.println();
        }
    }


    public void method(){

        int[] a = new int[] {5, 9, 2, 3, 4};
        int[] b = new int[] {1, 3, 9, 4, 2};
        List<Integer> c = new ArrayList<>();
        Person[] p = new Person[5];
        Person person = new Person("Antonio", 25);

        for(int i = 0; i < a.length; i++){
            a[i] = b[i];
        }

        for(Integer e : a){
            if(e < 5){
                c.add(e);
            }
        }
    }

}
