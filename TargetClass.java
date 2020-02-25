package trainingcode;


import com.me.giuseppe;
import com.me.alessandro;
import com.me.TargetClass;


/**
 * Classe Target per l'analisi
 */
public class TargetClass {

    //Variabile int
    public static int ONE_BILLION = 1000000000;
    //Variabile literalInt
    public static int TWO_BILLION = 2_000_000_000;

    /*
    Altre due variabili
     */
    private int a = 1000;
    private String str  = "Ciao";


    public int GetA(){
       return a;
    }

    public void SetA(int _a) {
        this.a = _a;
    }

    public String GetStr(){
        return str;
    }

    public void SetStr(String _str) {
        this.str = _str;
    }
}
