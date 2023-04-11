
public class Rostock extends Pizzeria{

	private String zutaten;

	public Rostock(String zutaten) {
		super(zutaten);
	}

	@Override
	public String stadt() {
		String temp = "Rostock";
		return temp;
	}

	@Override
	public String zutaten() {
		return this.zutaten;
	}
}

