package observer_pattern;

public interface Observable {
	public void register(Observer obj);
	public void removeObs(Observer obj);
	public void notifyObservers();
	public Object getUpdate(Observer obj);
}
