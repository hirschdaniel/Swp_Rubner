
public class SW_Drucker implements Drucker {
	
	private String type;
	
	public  SW_Drucker(String type) {
		this.type = type;
	}

	@Override
	public void drucken(String file) {
		System.out.println("Es wurde "+file+" auf dem "+type+"-Drucker gedruckt");
		
	}

}
