
public class Main {
	public static void main(String[] args)
	{
		Drucker druck = new Drucker_Proxy("SW");
		druck.drucken("1");
		
		Drucker druck2 = new Drucker_Proxy("Color");
		druck2.drucken("2");
		
		((Drucker_Proxy) druck2).switch_to_SW();
		druck2.drucken("2");
		
		((Drucker_Proxy) druck2).switch_to_Color();
		druck2.drucken("2");
	
	
	}


}
