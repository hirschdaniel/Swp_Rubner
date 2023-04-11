package observer_pattern;


public class Anzeige implements Observer {

	private String name;
	private Observable obs;
	
	public Anzeige(String name){
		this.name=name;
	}
	@Override
	public void update() {
		String msg = (String) obs.getUpdate(this);
		if(msg == null){
			System.out.println("Keine Aenderung");
		}else
		System.out.println(name+", Temperatur und Luftfeuchtigkeit betragen:"+msg);
	}

	@Override
	public void setObserver(Observable sub) {
		this.obs=sub;
	}
}


