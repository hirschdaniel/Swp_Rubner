
public class Drucker_Proxy implements Drucker{
	
	private String type;
	private Drucker druck;
	
	public  Drucker_Proxy(String type) {
		this.type = type;
	}

	@Override
	public void drucken(String file) {
		
		
		if(type == "Color" && druck==null ) {
			druck = new Color_Drucker(type);
			
		}else if(type == "SW" && druck ==null) {
			druck = new SW_Drucker(type); 
		}
		
		druck.drucken(file);
		
	}
	
	public void switch_to_SW() {
		druck = new SW_Drucker("SW");
	}
	
	public void switch_to_Color() {
		druck = new SW_Drucker("Color");
	}


}
