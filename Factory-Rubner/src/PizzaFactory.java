
public class PizzaFactory {

	public static Pizzeria getPizza(String zutaten, String stadt){
		if(stadt.equalsIgnoreCase("Berlin")) {
			return new Berlin(zutaten);
		}else if(stadt.equalsIgnoreCase("Hamburg")) {
			return new Hamburg(zutaten);
		}else if(stadt.equalsIgnoreCase("Rostock")) {
			return new Rostock(zutaten);
			
		}else {
			return null;
		}
	}
}