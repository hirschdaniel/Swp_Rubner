public class Hamburg extends Pizzeria{

	private String zutaten;

	public Hamburg(String zutaten) {
		super(zutaten);
	}

	@Override
	public String stadt() {
		String temp = "Hamburg";
		return temp;
	}

	@Override
	public String zutaten() {
		return this.zutaten;
	}
}
