package observer_pattern;

public class Test {

	public static void main(String[] args) {

		Wetterstation ws = new Wetterstation();

		Observer anzeige1 = new Anzeige("Anzeige1");
		Observer anzeige2 = new Anzeige("Anzeige2");


		ws.register(anzeige1);
		ws.register(anzeige2);


		anzeige1.setObserver(ws);
		anzeige2.setObserver(ws);


		

		ws.postMessage(1,2);
		//anzeige1.update();
	}


}
