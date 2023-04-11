package observer_pattern;
import java.util.ArrayList;
import java.util.List;

public class Wetterstation implements Observable {
	private List<Observer> observers;
	private int temp;
	private int luftf;
	private boolean changed;
	
	public Wetterstation(){
		this.observers = new ArrayList<>();
	}
	
	@Override
	public void register(Observer obj) {
		 observers.add(obj);
		
	}

	@Override
	public void removeObs(Observer obj) {
		observers.remove(obj);
		
	}

	@Override
	public void notifyObservers() {
		List<Observer> observers = null;
			if (changed = true) {
			observers = new ArrayList<>(this.observers);
			this.changed=false;
			for (Observer obj : observers) {
				obj.update();
			}

			}
		
	}

	@Override
	public Object getUpdate(Observer obj) {
		String message = String.valueOf(temp)+" "+String.valueOf(temp);
		return message;
	}
	
	public void postMessage(int temp, int luftf){
		this.temp = temp;
		this.luftf = luftf;
		this.changed=true;
		notifyObservers();
	}
}


